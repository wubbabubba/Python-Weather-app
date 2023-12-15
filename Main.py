import os
import json
import requests
from urllib.request import urlopen
import array as arr
print("Welcome to the weather app, you will be able to find the live weather data for any city")
cityName = input("What is the name of the city you'd like to choose?")
print(cityName)
response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=Paris,FR&limit=5&appid=78e3a6f3ae62901bfa2fcc723df53324")
data = response.json()

new_json = json.dumps(data, indent=2)
for x in data:  
    if x == name:
     print(x)
options = arr.data('i'[2])
print(options)
#option1 = data['name']
#lat = response['lat']
#longitude = data['lon']
#print(data['name'])
#print(longitude)