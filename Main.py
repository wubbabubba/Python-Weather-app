import os
import json
import requests
from urllib.request import urlopen
print("Welcome to the weather app, you will be able to find the live weather data for any city")
cityName = input("What is the name of the city you'd like to choose?")
print(cityName)
response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=Paris,FR&limit=5&appid=78e3a6f3ae62901bfa2fcc723df53324")
data = response.json()
print(data)
new_json = json.dumps(data, indent=2)
option1 = data['name'][4]
#lat = response['lat']
#longitude = data['lon']
print(option1)
#print(longitude)