from datetime import datetime
import requests
import googlemaps as gm
import pandas as pd
from bokeh.io import output_notebook
import numpy as np

def find_trucks():
    api_key = "AIzaSyAkau57eJydssl5tsbmTUSDaUTbH-N-JEc"
    gmaps = gm.Client(key=api_key)
    trucks = gmaps.places("foodtrucks in Indianapolis")
    choices = []
    
    #print(trucks.get('results'))
    place_id = (trucks['results'][0])
    #print(place_id['place_id'])
    place_details = gmaps.place(place_id['place_id'])
    #print(place_details['result']['opening_hours'])
    for truck in trucks['results']:
        if int(truck['rating']) >= 4:
            place_id = truck['place_id']
            place_details = gmaps.place(place_id)
            print(place_details['result']['opening_hours'])
            print(truck['name'] +" rating:" +str(truck['rating']))
            choices.append(truck['name'])
            #print(truck)

            
    return choices

