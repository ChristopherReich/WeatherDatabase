from core.Core import Core
from model import MongoDb
from core.Controller import Controller
from tkinter import messagebox
import copy


"""
    Responsible for ShowView behavior.
"""
class ShowController(Controller):
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.database = MongoDb.Database('WeatherDatabase')
        #self.database.set_Collection('WeatherCollection')
        self.showView = self.loadView('show')
        self.core = Core()


    """
        @behaviour when a button is clicked
    """   
    def btnClicked(self, caption , data):
        if caption == 'Update Data':
            self.database.update_item_by_id(view_dict = data)
            self.showView._show_data()
        if caption == 'Delete':
            self.database.delete_item_by_id(view_dict= data)
            self.showView._show_data()
        if caption == 'Data Export':
            self.database.export_To_CSV(self.showView._save_path_dir())
        if caption == 'Insert':
            self.database.insert_item(view_dict = data)
            self.showView._show_data()

       
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def getData(self):
        data = self.database.getAll()
        return data

    def item_selected(self,data):
        return self.database.get_One_Data_by_id(view_dict = data)
    
           
    
    """
        Opens EditController
        
        @param id_customer Customer id that will be edited
    """
    def btnEdit(self, id_customer):
        messagebox.showinfo('Edit data')
    
    """
        Deletes the chosen customer and updates the ShowView
        
        @param id_customer Customer id that will be edited
    """    
    def btnDel(self, id_customer):
        #self.database.delete(id_customer)
        #self.showView.update()
        messagebox.showinfo('Delete data', 'Data deleted with success!')
        
    """
        @Override
    """
    def main(self):
        self.showView.main()