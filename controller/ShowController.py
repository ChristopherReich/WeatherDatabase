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
        self.showView = self.loadView('show')
        self.core = Core()


    """
        @behaviour when a button is clicked
    """   
    def btnClicked(self, caption):
        if caption == 'Update Data':
            selected_item = self.get_selected_item()
            data = self.showView.create_dict_from_input()
            self.database.update_item_by_id(selected_item['metadata']['id'], data)
            self.showView.refresh_Treeview()

        if caption == 'Delete':
            selected_item = self.get_selected_item()
            self.database.delete_item_by_id(selected_item['metadata']['id'])
            self.showView.refresh_Treeview()

        if caption == 'Data Export':
            self.database.export_To_CSV(self.showView._save_path_dir())

        if caption == 'Insert':
            self.database.insert_OpenWeather_Data()
            self.showView.refresh_Treeview()

       
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        @return All customers in database
    """
    def get_data_from_database(self):
        data = self.database.get_all_data()
        return data



    """
        This method is bound with the <<TreeviewSelect>> event of the Treeview list.
    """
    def display_selected_item(self,event):       
        #Get the selected item
        selected_item = self.get_selected_item()
        self.showView.display_selected_item(selected_item)


    """
        Returns the selected item
    """
    def get_selected_item(self):
        focused_item = self.showView.treeview.focus()
        raw_item = self.showView.treeview.item(focused_item)     
        item_id = raw_item['values'][5]   # Object ID of the item            
        return self.database.get_item_by_id(item_id)

    
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