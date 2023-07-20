from core.Core import Core
from model import MongoDb
from core.Controller import Controller
from tkinter import messagebox
import matplotlib.pyplot as plt


"""
    Responsible for GraphView behavior.
"""
class GraphController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.databaseName = 'WeatherDatabase'
        self.collectionName = 'WeatherCollection'
        self.database = MongoDb.Database(self.databaseName)
        self.graphView = self.loadView("graph")
        self.core = Core()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getData(self):
        data = self.database.getAll(self.collectionName)
        return data
    
    def closeAllWindows(self):
        plt.close('all')
    
    def btnClicked(self, caption):
        data = self.database.getAll(self.collectionName)
        timestamps = []
        temperatures = []
        humidity = []
        windSpeed = []

        for result in data:
            timestamps.append(result['timestamp'])
            temperatures.append(result['temperature'])
            humidity.append(result['humidity'])
            windSpeed.append(result['windSpeed'])

        plt.clf()
        
        if caption == "Show temperature":           
            plt.plot(timestamps, temperatures)
            plt.ylabel('Temperature')       
            
        elif caption == "Show humidity":
            plt.plot(timestamps, humidity)
            plt.ylabel('humidty')
            
        elif caption == "Show windspeed":
            plt.plot(timestamps, temperatures)
            plt.ylabel('windspeed')
      
        plt.xlabel('Timestamp')
        plt.title('Temperature over Time in Wippenham')
        plt.xticks(rotation=45)
        plt.show()  

    """
        @Override
    """
    def main(self):
        self.graphView.main()