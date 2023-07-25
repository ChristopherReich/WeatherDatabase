from pymongo import MongoClient
from datetime import datetime , timedelta
import numpy as np
from model import OpenWeather
from bson.objectid import ObjectId


import pandas as pd
import plotly.graph_objects as go

class Database:

    def __init__(self, name):
        self.database_name = name
        self.Connect_Database() # working on local database, because cloud database needs static ip adress
        
    def Connect_Database(self):
        client = MongoClient('mongodb://127.0.0.1:27017')
        if self.database_name in client.list_database_names():
            self.db = client[self.database_name]
        else:
            client.get_database(self.database_name)
            print('Database created...')

    def Connect_Cloud_Database(self):
        from pymongo.mongo_client import MongoClient
        password = '2DgdV25hHbguPSTY'
        uri = f'mongodb+srv://Simon:{password}@sampleweather.dklv8xc.mongodb.net/?retryWrites=true&w=majority'
        # Create a new client and connect to the server
        client = MongoClient(uri)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        if self.database_name in client.list_database_names():
            self.db = client[self.database_name]
            pass
        else:
            client.get_database(self.database_name)
            self.db = client[self.database_name]
            print('Cloud Database created...')

    def Create_Collection(self, collection_name):
        if collection_name in self.db.list_collection_names():
            pass
        else:
            self.db.create_collection(
                collection_name,
                timeseries= {
                    'timeField': 'timestamp',
                    'metaField': 'metadata',
                    'granularity': 'seconds'
                }
            )
            print('Collection created...')
        self.collection = self.db[collection_name]

    def Insert_OpenWeather_Data(self, location, collection_name):
        data = location.GetWeatherData()
        collection_name = self.db[collection_name]
        collection_name.insert_one(data)
        print('Insert 1 dataset...')

    def Insert_Sample_Data(self, location, collection_name):
        data = {
            'location': {
                'city': location.city,
                'street' : location.street,
                'street number' : location.street_number
            },
            'timestamp': datetime.now(),
            'temperature': np.random.randint(0, 30),
            'humidity' : np.random.randint(0,100),
            'windSpeed' : np.random.randint(0,50),
            'pressure' : np.random.randint(1000, 1050)           
        }

        collection_name = self.db[collection_name]
        collection_name.insert_one(data)
        print('Insert 1 sample dataset...')

    def Create_Sample_Dataset(self, location, collection_name):
        dataList = []
        for i in range(24*4,0,-1):
            timeOffset = timedelta(minutes = i*15)
            
            data = {
                'metadata': {   'ID': i,
                                'temperature': np.random.randint(0, 30),
                                'humidity' : np.random.randint(0,100),
                                'windSpeed' : np.random.randint(0,50),
                                'pressure' : np.random.randint(1000, 1050),
                                'city': location.city,
                                'street' : location.street,
                                'street number' : location.street_number,
                                'time': datetime.now() - timeOffset
                                }, 
                'timestamp': datetime.now() - timeOffset
            }
            dataList.append(data)

        collection_name = self.db[collection_name]
        collection_name.insert_many(dataList)
        print('Create test dataset...')

    def findData(self, collection_name, query):
        collection_name = self.db[collection_name]
        results = collection_name.find(query)
        return results

    def getAll(self, collection_name):
        collection_name = self.db[collection_name]
        results = collection_name.find()
        return results
      
    def update_item_by_id(self, collection_name, view_dict):
        temperature = view_dict["temperature"]
        id = view_dict["ID"]
        #temperature = 0
        collection_name = self.db[collection_name]
        collection_name.update({'metadata.ID': id } , {"$set": { 'metadata.temperature': temperature}},multi=True)
        
    def delete_item_by_id(self, collection_name, view_dict):
        collection_name = self.db[collection_name]
        id = view_dict["id"]
        collection_name.delete_many({'metadata.ID': id })
