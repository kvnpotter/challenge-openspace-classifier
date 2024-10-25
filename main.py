from utils.table import Seat, Table
from utils.openspace import Openspace
import pandas as pd
from utils.file_utils import file

name_DataFrame = pd.read_excel(file, header= None)
name_list = list(name_DataFrame[0].values)

openspace_1 = Openspace()
openspace_1.organize(name_list)

openspace_1.display()
openspace_1.store("seating_plan")

# Create an infinite loop to allow changes in the seating plan or quitting the program
while True:
    change = input("Do you want to update the seating plan? (y/n)\nOr quit the program? (q) :")
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

