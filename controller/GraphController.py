from core.Core import Core
from model import MongoDb
from core.Controller import Controller
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
        self.database = MongoDb.Database(self.databaseName)
        self.graphView = self.loadView('graph')
        self.core = Core()
        self.metadata = [
        'temperature',
        'humidity',
        'windspeed',
        'pressure'
        ]
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getData(self):
        data = self.database.getAll()
        return data
    
    """
        Close all figures when exiting the window
    """
    def closeAllWindows(self):
        plt.close('all')
    
    """
        @behaviour when a button is clicked
    """
    def btnClicked(self, caption):
        data = self.database.get_all_data()
        timestamps = []
        temperatures = []
        humidity = []
        windSpeed = []
        pressure = []

        for result in data:
            timestamps.append(result['timestamp'])
            temperatures.append(result['metadata']['temperature'])
            humidity.append(result['metadata']['humidity'])
            windSpeed.append(result['metadata']['windSpeed'])
            pressure.append(result['metadata']['pressure'])

        plt.clf()

        if caption == 'Show ' + self.metadata[0]:           
            plt.plot(timestamps, temperatures)
            metadata = self.metadata[0]
                             
        elif caption == 'Show ' + self.metadata[1]:
            plt.plot(timestamps, humidity)
            metadata = self.metadata[1]
            
        elif caption == 'Show ' + self.metadata[2]:
            plt.plot(timestamps, windSpeed)
            metadata = self.metadata[2]

        elif caption == 'Show ' + self.metadata[3]:
            plt.plot(timestamps, pressure)
            metadata = self.metadata[3]
        else:
            metadata = ''
        
        plt.xlabel('Timestamp')
        plt.ylabel(metadata) 
        plt.title(metadata + ' over time') 
        
        plt.xticks(rotation=45)
        plt.show()  

    """
        @Override
    """
    def main(self):
        self.graphView.main()