#server

import pandas as pd
import os

from utils import article


url_container = os.getcwd()+'/url-container.csv' #URL container

DataFrame = pd.read_csv(url_container) #URL - container -> automise by ()

print(DataFrame)