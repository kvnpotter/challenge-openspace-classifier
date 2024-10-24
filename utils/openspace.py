from table import Table
from random import sample
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import geopandas as gpd

class Openspace:
    ...

    def __init__(self, number_of_tables: int = 6) -> None:
        ...
        self.number_of_tables: int = number_of_tables
        self.tables: list[Table] = [Table for _ in range(self.number_of_tables)]

    def organize(self, people: list) -> None:
        ...
        total_seats = [i for i in range(0, self.number_of_tables * 4)]
        if len(people) > len(total_seats):
            print("NOT ENOUGH SEATS !")
        else:
            for person in people:
                random_sample = sample(total_seats,1)
                total_seats.remove(random_sample)
                random_seat = random_sample // 6
                random_table = random_sample // 4
                self.tables[random_table].assign_seat(person) #What is this for
                self.tables[random_table].seats[random_seat].set_occupant(person)

    def display(self) -> None:
        ...

        # Create empty lists to contain table x and y coordinates, table length and the variable table width
        table_x_coords = []
        table_y_coords = []
        table_lengths = []
        table_width = 5
        
        # Loop over tables, assign column (4 rows of tables per column max), calculate x coordinate center table
        for i in range(self.number_of_tables):
            column = round(i/4)
            center_table_x = column * 25 + 12.5
            table_x_coords.append(center_table_x)
        
        # Create table index, go over all tables in groups of 4 (rows per column), calculate variable table length depending on 
        # number of occupants, calculate y coordinate center table
        table_index = 0
        while table_index + 1 < self.number_of_tables :
            for i in range(4):
                number_occupants_side = self.tables[table_index].capacity - self.tables[table_index].capacity // 2
                table_length = number_occupants_side * 2 + 2
                table_lengths.append(table_length)
                center_table_y = (table_length / 2 + 5) + (i * (table_length + 10))
                table_y_coords.append(center_table_y)
                table_index += 1

        # Create a list of shapely Point() objects from lists of x and y coordinates
        tables_points = []
        for x, y in zip(table_x_coords, table_y_coords):
            tables_points.append(Point(x,y))

        # Create a list of tables (polygons), each a list of 4 points (corners of each table)
        tables = []
        for index, center_point in enumerate(tables_points):
                point_1 = Point(center_point.x - 2.5, center_point.y + table_lengths[index] / 2)
                point_2 = Point(center_point.x - 2.5, center_point.y - table_lengths[index] / 2)
                point_3 = Point(center_point.x + 2.5, center_point.y + table_lengths[index] / 2)
                point_4 = Point(center_point.x + 2.5, center_point.y - table_lengths[index] / 2)
                tables.append(Polygon[point_1, point_2, point_3, point_4])
        
        # Into GeoDataFrame
        tables_gdf = gpd.GeoDataFrame(geometry = tables)

        # Create plot and visualise

        f, ax = plt.subplots(1,1)
        tables_gdf.plot(ax = ax)

                table.append(tables_points[0])
                tables_points.pop(0)
                table_index += 1
            new_table = Polygon(table)
            tables.append(new_table)
            table=[]
            
        while point_counter < 4 :
            table.append(tables_points[0])
            tables_points.pop(0)
            point_counter += 1
        else:
            new_table = Polygon(table)
            tables.append(new_table)
            table = []
            point_counter = 0

        number_occupants = self.tables[table_index].capacity - self.tables[table_index].left_capacity()
            
            

    def store(self, filename: str) -> None:
        ...