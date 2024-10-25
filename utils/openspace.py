# Necessary imports
from .table import Table
from random import sample
from math import floor
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

# Define class openspace with __init__ method
class Openspace:
    """
    A class representing an openspace.
    """

    def __init__(self, number_of_tables: int = 6) -> None:
        """
        Create an openspace with specified number of tables.

        :param number_of_tables: (int, optional): Number of tables to create in the openspace. Defaults to 6.
        """
        self.number_of_tables: int = number_of_tables
        self.tables: list[Table] = [Table() for _ in range(self.number_of_tables)]

    def organize(self, people: list) -> None:
        """
        Randomly allocate people in specified list to free seats in the openspace.

        :param: people (list): A list of people to seat.
        """
        # Create list of total available seat indices
        total_seats = [i for i in range(0, self.number_of_tables * 4)]
        # Check enough seats for people in list
        if len(people) > len(total_seats):
            print("NOT ENOUGH SEATS !")
        else:
            # Loop over people list, randomly select free seat index and remove from list
            # Calculate table and seat-at-table index, assign person to obtained seat
            for person in people:
                random_sample = sample(total_seats, 1)
                total_seats.remove(random_sample[0])
                random_seat = random_sample[0] % 4
                random_table = random_sample[0] // 4
                self.tables[random_table].seats[random_seat].set_occupant(person)

    def display(self) -> None:
        """
        Create a seating plan of allocated seats.
        """

        # Create empty lists to contain table x and y coordinates, table length and the variable table width
        table_x_coords = []
        table_y_coords = []
        table_lengths = []

        # Loop over tables, assign column (4 rows of tables per column max), calculate x coordinate center table
        for i in range(self.number_of_tables):
            column = floor(i / 4)
            center_table_x = column * 25 + 12.5
            table_x_coords.append(center_table_x)

        # Create table index, go over all tables in groups of 4 (rows per column), calculate variable table length depending on
        # number of occupants, calculate y coordinate center table
        table_index = 0
        while table_index < self.number_of_tables:
            remaining_tables = self.number_of_tables - (table_index)
            if remaining_tables >= 4:
                for i in range(4):
                    number_occupants_side = (
                        self.tables[table_index].capacity
                        - self.tables[table_index].capacity // 2
                    )
                    table_length = number_occupants_side * 2 + 2
                    table_lengths.append(table_length)
                    center_table_y = (table_length / 2 + 5) + (i * (table_length + 10))
                    table_y_coords.append(center_table_y)
                    table_index += 1
            elif remaining_tables < 4:
                for i in range(remaining_tables):
                    number_occupants_side = (
                        self.tables[table_index].capacity
                        - self.tables[table_index].capacity // 2
                    )
                    table_length = number_occupants_side * 2 + 2
                    table_lengths.append(table_length)
                    center_table_y = (table_length / 2 + 5) + (i * (table_length + 10))
                    table_y_coords.append(center_table_y)
                    table_index += 1
        while len(table_y_coords) > len(table_x_coords):
            table_y_coords.pop(-1)

        # Create a list of shapely Point() objects from lists of x and y coordinates
        tables_points = []
        for x, y in zip(table_x_coords, table_y_coords):
            tables_points.append(Point(x, y))

        # Create a list of tables (polygons), each a list of 4 points (corners of each table)
        tables = []
        for index, center_point in enumerate(tables_points):
            point_1 = Point(
                center_point.x - 2.5, center_point.y + table_lengths[index] / 2
            )
            point_2 = Point(
                center_point.x - 2.5, center_point.y - table_lengths[index] / 2
            )
            point_3 = Point(
                center_point.x + 2.5, center_point.y - table_lengths[index] / 2
            )
            point_4 = Point(
                center_point.x + 2.5, center_point.y + table_lengths[index] / 2
            )
            tables.append(Polygon([point_1, point_2, point_3, point_4]))

        # Into GeoDataFrame
        tables_gdf = gpd.GeoDataFrame(geometry=tables)

        # Add central points to GDF
        tables_gdf["center"] = tables_points

        # Create list of remaining seats per table and add to GDF
        remaining_seats = []
        for table in self.tables:
            remaining_seats.append(table.left_capacity())
        tables_gdf["free_seats"] = remaining_seats

        # Create seating plan
        seating_plan = []
        for table in self.tables:
            table_names = ""
            for seat in table.seats:
                table_names += "\n" + seat.occupant
            seating_plan.append(table_names)
        tables_gdf["occupants"] = seating_plan

        # Create plot and visualise
        ax = tables_gdf.plot()

        placement_list = []
        for i, j in tables_gdf.iterrows():
            string = f"free seats:\n{j.iloc[2]}\noccupants:\n{j.iloc[3]}"
            placement_list.append(string)

        tables_gdf["display_text"] = placement_list

        x = [j["geometry"].centroid.coords[0] for i, j in tables_gdf.iterrows()]
        texts = [j["display_text"] for i, j in tables_gdf.iterrows()]
        new_df = pd.DataFrame({"x": x, "y": y, "texts": texts})

        for i, j in new_df.iterrows():
            ax.annotate(text=j["texts"], xy=j["x"], ha="center", va="center")
        plt.axis('off')
        plt.show()

    def store(self, filename: str) -> None:
        """
        Store the current seating plan in an Excel file.

        :param filename: (str): String specifying the filename to export to.
        """
        names_placing = []
        table_number = []
        seat_number = []
        # Create lists of names, table number and seat number, store in dict
        for table_index, table in enumerate(self.tables):
            for seat_index, seat in enumerate(table.seats):
                names_placing.append(seat.occupant)
                seat_number.append(seat_index + 1)
                table_number.append(table_index + 1)
        placement = {
            "Name": names_placing,
            "table_number": table_number,
            "seat_number": seat_number,
        }
        # Create pandas df based on dict and export to excel
        placement_df = pd.DataFrame(placement)
        placement_df.to_excel(filename + ".xlsx")

    def __str__(self) -> str:
        number_free_tables = 0
        number_free_seats = 0
        for table in self.tables:
            number_free_tables += table.has_free_spot()
            number_free_seats += table.left_capacity()
        return f"This is an openspace organizer.\nThere are {number_free_tables} tables with free seats.\nThere are {number_free_seats} free seats left."
