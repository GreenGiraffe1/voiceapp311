from datetime import date, time, datetime, timedelta

import json
import requests

MBTA_API_KEY = "b7b42fecd47d416484ed1a3a4d67632a"
TEST_DEPARTURE_STATION = "place-north"
TEST_ARRIVAL_STATION = "Andover"
TEST_ROUTE = "CR-Haverhill"
TEST_DIRECTION = 0  #  The value 0 is for outbound trains

todays_date = date.today() # Use str() when I want to pass it as a string
# print("today's date is: " + str(todays_date) + ".")

current_time = datetime.now().time().strftime('%H:%M')
print(str(current_time))


url = "https://api-v3.mbta.com/schedules?"

payload = {
    "include" : "prediction",
    "page[limit]" : "2",
    "sort" : "departure_time",
    "filter[date]" : todays_date,
    "filter[direction_id]" : TEST_DIRECTION,
    "filter[min_time]" : current_time,
    "filter[route]" : TEST_ROUTE,
    "filter[stop]" : TEST_DEPARTURE_STATION,
    "api_key" : MBTA_API_KEY
}

r = requests.get(url, params=payload)

print(r.text)

print("The URL used for the request is:\n\n")
print(r.url)
# Un-adultered URL
# https://api-v3.mbta.com/schedules?page%5Blimit%5D=2&sort=departure_time&filter%5Bdate%5D=2018-06-05&filter%5Bdirection_id%5D=1&filter%5Bmin_time%5D=13%3A45&filter%5Broute%5D=CR-Haverhill&filter%5Bstop%5D=place-north&api_key=b7b42fecd47d416484ed1a3a4d67632a
print("\n\nThis returns the next 2 trains departing from North Station on the Haverhill Line of the Commter Rail.\n\n")

# Main Methods in the "Requests" Library
# r.status_code
# r.headers['cotent-type']
# r.encoding
# r.text
# r.json()


"""Grab and print the 'trip' identifier"""
response = r.json()
trip_id = response['data'][0]['relationships']['trip']['data']['id']
departure_time = response['data'][0]['attributes']['departure_time']

# TODO: ADD a test to see if there is a prediction / if it doesn't match the schedule

# print("The trip_id is: " + str(trip_id))






""" Now, use the trip_id to find the arrival time for this train to Andover """
arr_url = "https://api-v3.mbta.com/schedules?"
 
arr_payload = {
     "include" : "prediction",
     "filter[date]" : todays_date,
     "filter[stop]" : TEST_ARRIVAL_STATION,
     "filter[trip]" : trip_id,
     "api_key" : MBTA_API_KEY
}
 
#  Contains all the stops information for this trip
arr_req = requests.get(arr_url, params=arr_payload)
print("\n\n")
print(arr_req.url)
arr_response = arr_req.json()


arrival_time = arr_response['data'][0]['attributes']['arrival_time']

# TODO: ADD test to see if there is a prediction, and if different than schedule

# print(str(arrival_time))
print("\n\n")

"""Print out exactly what the Alexa Skill will speak to the user"""
print("The next train from North Station to Andover is scheduled to depart at " + str(departure_time) + " and to arrive at the Andover station at " + arrival_time + ".")