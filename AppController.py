from Model import MongoDb
from Model import OpenWeather
import matplotlib.pyplot as plt


home = OpenWeather.Location('Wippenham', 'Bruck', 8)
work = OpenWeather.Location('Thalheim', 'Günter-Fronius-Straße', 1)


database = MongoDb.Database('WeatherDatabase')
database.Connect_Cloud_Database()
database.Create_Collection('WeatherCollection')

#database.Insert_Sample_Data(home,'WeatherCollection')
#database.Create_Sample_Dataset(home,'WeatherCollection')
#database.Insert_OpenWeather_Data(home, 'WeatherCollection')

#database.Insert_Sample_Data(work,'WeatherCollection')
#database.Create_Sample_Dataset(work,'WeatherCollection')
#database.Insert_OpenWeather_Data(work, 'WeatherCollection')


query = {'location.city': 'Wippenham'}
queryResult = database.FindData('WeatherCollection',query)


# Extract temperature and timestamp data
timestamps = []
temperatures = []
for result in queryResult:
    print(result['timestamp'])
    timestamps.append(result['timestamp'])
    temperatures.append(result['temperature'])

# Create a line plot of temperature over time
plt.plot(timestamps, temperatures)
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.title('Temperature over Time in Wippenham')
plt.xticks(rotation=45)
plt.show()
