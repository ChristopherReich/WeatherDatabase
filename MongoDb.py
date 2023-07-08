from pymongo import MongoClient
import datetime
import numpy as np



class Database:
    global db
    global database_name

    def __init__(self, name):
        self.database_name = name


    def Connect_Database(self):
        client = MongoClient('mongodb://127.0.0.1:27017')
        if self.database_name in client.list_database_names():
            self.db = client['WeatherDatabase']
            print('Database already exists.')
        else:
            client.get_database(database_name)
            print('Database created...')


    def Create_Collection(self, collection_name):
        if collection_name in self.db.list_collection_names():
            print('Collection already exists.')
        else:
            self.db.create_collection(
                collection_name,
                timeseries= {
                    'timeField': 'timestamp',
                    'metaField': 'location',
                    'granularity': 'seconds'
                }
            )
            print('Collection created...')



    def Insert_Sample_Data(self, collection_name):
        data = {
        'location': {
        'city': 'Wippeham',
        'street' : 'Bruck',
        'street number' : 8
        },
        'temperature': np.random.randint(0, 30),
        'windSpeed' : np.random.randint(0,50),
        'pressure' : np.random.randint(1000, 1050),
        'timestamp': datetime.datetime.now()
        }

        collection_name = self.db['Weather']
        collection_name.insert_one(data)
        print('Insert 1 dataset...')




