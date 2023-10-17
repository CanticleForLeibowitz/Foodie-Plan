from datetime import datetime
import requests
import googlemaps as gm
import pandas as pd
from bokeh.io import output_notebook
import numpy as np


dataframe = pd.read_csv('Example-Data.csv')
dataframe.head()
print(dataframe.loc[:,"Rating"])
api_key = "AIzaSyAkau57eJydssl5tsbmTUSDaUTbH-N-JEc"
gmaps = gm.Client(key=api_key)
now = datetime.now()
directions_result = gmaps.directions("The Night Owl Food Truck","IUPUI",mode="transit",departure_time=now)
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

print(directions_result)