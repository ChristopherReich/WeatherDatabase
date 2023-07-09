# pip install requests

import requests
from requests.structures import CaseInsensitiveDict
import datetime
from geopy.geocoders import Nominatim


class Location:
    def __init__(self, city, street, street_number):
        self.api_key = 'c8b0afac8bc6ad190b6527d7d81cf0ae'
        self.city = city
        self.street = street
        self.street_number = street_number
        self.lat, self.lon = self.GetCoordinates()



    def GetCoordinates(self):
        #address we need to geocode
        loc = f'{self.city}, {self.street} {self.street_number}'

        #making an instance of Nominatim class
        geolocator = Nominatim(user_agent="my_request")
        
        #applying geocode method to get the location
        location = geolocator.geocode(loc)
        
        return location.latitude, location.longitude







    def GetWeatherData(self):
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}'
        
        r = requests.get(url).json()
        data = {
            'location': {
                'city': self.city,
                'street' : self.street,
                'street number' : self.street_number
                },
            'timestamp' : datetime.datetime.now(),
            'temperature' : round((r['main']['temp']-273.15),1),
            'humidity' : r['main']['humidity'],
            'windSpeed' : round(r['wind']['speed']*3.6,1),
            'pressure' : r['main']['pressure']
        }
        return data









#print(GetWeatherData(lat, lon))