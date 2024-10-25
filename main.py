from utils.table import Seat, Table
from utils.openspace import Openspace
import pandas as pd
from utils.file_utils import file

namelist = ["Jean", "KEvin", "Franck", "Evris", "Tom", "Dick", "arr"]

openspace_1 = Openspace()
openspace_1.organize(namelist)

print(openspace_1)
print(openspace_1.tables[0].seats[3])
print(openspace_1.tables[0])
openspace_1.display()

openspace_1.store("test1")

