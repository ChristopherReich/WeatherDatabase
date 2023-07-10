from Model import MongoDb
from Model import OpenWeather


home = OpenWeather.Location('Wippenham', 'Bruck', 8)
work = OpenWeather.Location('Thalheim', 'Günter-Fronius-Straße', 1)


database = MongoDb.Database('WeatherDatabase')
database.Connect_Cloud_Database()
database.Create_Collection('WeatherCollection')

#database.Insert_Sample_Data(home,'WeatherCollection')
database.Create_Sample_Dataset(home,'WeatherCollection')
#database.Insert_OpenWeather_Data(home, 'WeatherCollection')

#database.Insert_Sample_Data(work,'WeatherCollection')
database.Create_Sample_Dataset(work,'WeatherCollection')
#database.Insert_OpenWeather_Data(work, 'WeatherCollection')
