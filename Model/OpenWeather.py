# pip install requests

import requests
import datetime


class Location:
    def __init__(self, city, street, street_number, lat, lon):
        self.city = city
        self.street = street
        self.street_number = street_number
        self.lat = lat
        self.lon = lon



    def GetWeatherData(self):
        api_key = 'c8b0afac8bc6ad190b6527d7d81cf0ae'
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={api_key}'
        
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