from .file_utils import file

import pandas as pd
name_DataFrame = pd.read_excel(file, header= None)
name_list = list(name_DataFrame[0].values)
name_list