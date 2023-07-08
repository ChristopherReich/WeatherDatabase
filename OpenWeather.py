# pip install requests

import requests




def GetWeatherData(lat ,lon):
    api_key = 'c8b0afac8bc6ad190b6527d7d81cf0ae'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    
    r = requests.get(url).json()
    weather = {
        'lat' : lat,
        'lon' : lon,
        'temperature' : round((r['main']['temp']-273.15),1),
        'humidity' : r['main']['humidity'],
        'windSpeed' : round(r['wind']['speed']*3.6,1),
        'pressure' : r['main']['pressure']
    }
    return weather



lat = '48.21447505047061'
lon = '13.399023258618133'



#print(GetWeatherData(lat, lon))