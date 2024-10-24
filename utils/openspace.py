from table import Table
from random import sample
import matplotlib.pyplot as plt

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
        table_coords = []
        for table in self.tables:
            number_occupants = table.capacity - table.left_capacity()
            number_occupants_side = table.capacity- table.capacity // 2
            table_length = number_occupants_side * 2 + 2
            for col in range(self.number_of_tables):
                center_table_x = col * 25 + 12.5
                for row in range(4):

            
            center_table_y = (table_length / 2 + 5) + (row_ind * (table_length + 10))

    def store(self, filename: str) -> None:
        ...