from Model import MongoDb


database = MongoDb.Database('WeatherDatabase')
database.Connect_Database()
database.Create_Collection('Weather')
database.Insert_Sample_Data('Weather')

database.Create_Sample_Dataset('Weather')