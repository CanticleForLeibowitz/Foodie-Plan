import googlemaps as gm

#Function used to find all food trucks in indy and sort them by rating and number of ratings 
def find_trucks():
    #API key generated using my google account to connect to API 
    api_key = "AIzaSyAkau57eJydssl5tsbmTUSDaUTbH-N-JEc"
    gmaps = gm.Client(key=api_key)
    #places() function used to find (20) food trucks in Indianapolis
    trucks = gmaps.places("foodtrucks in Indianapolis")
    #List initialized 
    choices = []
    #Loop iterates over 20 trucks  
    for truck in trucks['results']:
        #Logic statement that sorts trucks by rating of 4 stars or higher
        if int(truck['rating']) >= 4:
            place_id = truck['place_id']
            #the place_id is used to find more detailed info about hours of operation
            place_details = gmaps.place(place_id)
            #Results of detailed place function are appended to the intialized list above
            choices.append(place_details['result'])
            
    #After all trucks with a rating of 4 or higher are found I then sort by total number of ratings, high sample size is important to find
    sorted_list = sorted(choices, key=lambda x: x['user_ratings_total'])
    #Reverses the sorted list to have descending order from highest number of ratings to lowest
    sorted_list.reverse()
    print(len(sorted_list))        
    return choices

