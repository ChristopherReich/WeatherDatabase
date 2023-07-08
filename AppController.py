from Model import MongoDb
from Model import OpenWeather

# coordinates for Wippenham/Bruck 8
lat = '48.21447505047061'
lon = '13.399023258618133'

home = OpenWeather.Location('Wippenham', 'Bruck', 8, lat, lon)



database = MongoDb.Database('WeatherDatabase')
database.Connect_Database()
database.Create_Collection('Weather')
#database.Insert_Sample_Data('Weather')
#database.Create_Sample_Dataset('Weather')
database.Insert_OpenWeather_Data(home, 'Weather')
