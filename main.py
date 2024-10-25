from utils.table import Seat, Table
from utils.openspace import Openspace
import pandas as pd
from utils.file_utils import file

name_DataFrame = pd.read_excel(file, header=None)
name_list = list(name_DataFrame[0].values)

openspace_1 = Openspace()
openspace_1.organize(name_list)

openspace_1.display()
openspace_1.store("seating_plan")

# Create an infinite loop to allow changes in the seating plan or quitting the program
while True:
    question = input(
        "Do you want to request information on the seating plan or occupancy? (y/n) :"
    )
    if question == "y":
        disp = input(
            "Display number of remaining seats, total seats in the room,\n number people in the room or graphic seating plan? (left_seat/tot_seat/people/graph) :"
        )
        if disp == "left_seat":
            openspace_1.number_remaining_seats()
        elif disp == "tot_seat":
            print(
                f"There are {openspace_1.number_of_tables * openspace_1.number_of_seats_per_table} seats in this openspace."
            )
        elif disp == "people":
            openspace_1.occupant_list()
        elif disp == "graph":
            openspace_1.display()
        else:
            print("Invalid input.")
    change = input(
        "Do you want to update the seating plan? (y/n)\nOr quit the program? (q) :"
    )
    if change == "y":
        what = input("New arrival or departure? (arrival/departure) :")
        who = input("Input name :")
        openspace_1.handle_changes(what, who)
    elif change == "n":
        pass
    elif change == "q":
        break
    else:
        print("Invalid input")
