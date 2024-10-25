from utils.table import Seat, Table
from utils.openspace import Openspace
import pandas as pd
from utils.file_utils import file

import pandas as pd
name_DataFrame = pd.read_excel(file, header= None)
name_list = list(name_DataFrame[0].values)

openspace_1 = Openspace()
openspace_1.organize(name_list)

openspace_1.display()

openspace_1.store("seating_plan")

