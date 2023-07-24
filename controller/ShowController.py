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
        if caption == "Update Data":
            pass
            #self.showView._update_data()          
            #self.updateData()


       
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getData(self):
        data = self.database.getAll('WeatherCollection')
        return data
    
    def updateData(self):
        self.database.update()

    def item_selected(self, event):
        # This method is bound with the <<TreeviewSelect>> event of the Treeview list.
        # This will call 'get_movie_detail' method of the DBHandler class to fetch the details
        # of selected movie.
        for selected_item in self.showView.treeview.selection():
                # Get the selected item
                item = self.showView.treeview.item(selected_item)
                # Get the document from the Mongo db collection matching with the name of the movie
                id = item['values'][5]               
                result = self.database.get_item_by_id('WeatherCollection', id)
                self.showView._display_selected_item(result)
           
    
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