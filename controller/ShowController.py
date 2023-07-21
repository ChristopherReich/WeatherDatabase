from core.Core import Core
from model import MongoDb
from core.Controller import Controller
from tkinter import messagebox


"""
    Responsible for ShowView behavior.
"""
class ShowController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.database = MongoDb.Database('WeatherDatabase')
        self.showView = self.loadView("show")
        self.core = Core()
        
    def btnClicked(self, caption):
        if caption == "Get Selection":
            self.showView._get_item()
        elif caption == "Update Data":
            self.showView._update_data()
       
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getData(self):
        data = self.database.getAll('WeatherCollection')
        return data
    
    """
        Opens EditController
        
        @param id_customer Customer id that will be edited
    """
    def btnEdit(self, id_customer):
        #customer = self.database.get(id_customer)
        #c = self.core.openController("edit")
        #c.main(customer, self.showView)
        messagebox.showinfo("Edit data")
    
    """
        Deletes the chosen customer and updates the ShowView
        
        @param id_customer Customer id that will be edited
    """    
    def btnDel(self, id_customer):
        #self.database.delete(id_customer)
        #self.showView.update()
        messagebox.showinfo("Delete data", "Data deleted with success!")
        
    """
        @Override
    """
    def main(self):
        self.showView.main()