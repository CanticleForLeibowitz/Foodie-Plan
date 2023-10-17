from datetime import datetime
import requests
import googlemaps as gm
import pandas as pd
from bokeh.io import output_notebook
import numpy as np
import food_truck_options as fto


api_key = "AIzaSyAkau57eJydssl5tsbmTUSDaUTbH-N-JEc"
gmaps = gm.Client(key=api_key)
now = datetime.now()
count = 0.0
final_selection = []
choices = fto.find_trucks()
#print(choices)

for choice in choices:
        print(choice['formatted_address'])
        directions_result = gmaps.directions("IUPUI",choice['formatted_address'],mode="transit",departure_time=now)
        distance = float(directions_result[0]['legs'][0]['distance']['text'].replace(' mi', ''))
        if distance >= 7.0 and count < 7.0:
                if distance <= 1.0 and count < 7.0:
                    final_selection.append(choice)
                    count += 1.0

                



