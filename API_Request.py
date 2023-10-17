from datetime import datetime
import requests
import googlemaps as gm
import pandas as pd
from bokeh.io import output_notebook
import numpy as np
import food_truck_options as fto

dataframe = pd.DataFrame(pd.read_excel("FoodTruck Names.xlsx")) 
dataframe.head()
print(dataframe["Name"][0])
api_key = "AIzaSyAkau57eJydssl5tsbmTUSDaUTbH-N-JEc"
gmaps = gm.Client(key=api_key)
now = datetime.now()
name = dataframe["Name"][1]
print(type(name))
choices = fto.find_trucks()
print(choices)


directions_result = gmaps.directions("IUPUI",name,mode="transit",departure_time=now)


steps = directions_result[0]
add = steps['legs']
x = add[0]
start_address = x['start_address']
#print(directions_result)
