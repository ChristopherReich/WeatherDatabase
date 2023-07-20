from core.Core import Core
from model import MongoDb
from core.Controller import Controller
from tkinter import messagebox


"""
    Responsible for GraphView behavior.
"""
class GraphController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.database = MongoDb.Database('WeatherDatabase')
        self.showView = self.loadView("Graph")
        self.core = Core()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getDataInJSON(self):
        data = self.database.getDataInJSON('WeatherCollection')
        return data
    

    """
        @Override
    """
    def main(self):
        self.showView.main()