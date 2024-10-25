from table_kevin import Seat, Table
from openspace import Openspace

namelist = ["Jean", "KEvin", "Franck", "Evris", "Tom", "Dick", "arr"]

openspace_1 = Openspace()
openspace_1.organize(namelist)

openspace_1.display()

openspace_1.store("test1")

