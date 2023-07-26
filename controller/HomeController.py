# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core
from model import MongoDb
from model import OpenWeather

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("home")
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """
    def btnClicked(self, caption):
        if caption == "Show data":
            c = Core.openController("show")
            c.main()
        elif caption == "Show graph":
            c = Core.openController("graph")
            c.main()
        elif caption == "Create sample data":
            self.database = MongoDb.Database('WeatherDatabase')
            self.database.Create_Collection('WeatherCollection')
            self.database.Create_Sample_Dataset()
            
    """
        @Override
    """
    def main(self):
        self.homeView.main()