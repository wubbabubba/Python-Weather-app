import os
import json
import requests
from urllib.request import urlopen
import array as arr
print("Welcome to the weather app, you will be able to find the live weather data for any city ")
cityName = input("What is the name of the city you'd like to choose? ")
cityCountry = input("What country is the city in? (Use the Abbreviation please)")
print(cityName)
print(cityCountry)
response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + cityName + "," + cityCountry + "&limit=5&appid=78e3a6f3ae62901bfa2fcc723df53324")
data = response.json()

#new_json = json.dumps(data, indent=2)

count = 0
for x in data:  
    option1 = [x['name'], x['state'], x['country']] 
    count = count + 1
    print ("Option", count, option1)

choice = input("Choose an option 1 - " + str(count) + " ")  
choice = int(choice)
lat = (data[choice -1]['lat'])
lon = (data[choice -1]['lon'])
print(data[choice - 1]['lat'])
print(data[choice - 1]['lon'])   

print("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + "78e3a6f3ae62901bfa2fcc723df53324")

response1 = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + "78e3a6f3ae62901bfa2fcc723df53324")

data1 = response1.json()
print(data1)

#option1 = data['name']
#lat = response['lat']
#longitude = data['lon']

#print(data['name'])
#print(longitude)-iop