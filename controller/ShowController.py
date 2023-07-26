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
        # Bind the method with TreeViewSelect event.
        self.showView.treeview.bind('<<TreeviewSelect>>', self.display_selected_item)


    """
        @behaviour when a button is clicked
    """   
    def btnClicked(self, caption):
        if caption == 'Update Data':
            self.update_data()

        if caption == 'Delete':
            self.delete_data()

        if caption == 'Data Export':
            self.database.export_To_CSV(self.showView._save_path_dir())

        if caption == 'Insert':
            self.insert_data()

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
        try:
            selected_item = self.get_selected_item()
            self.showView.display_selected_item(selected_item)
        except:
            pass

    """
        Update the selected item
    """
    def update_data(self):
        try:
            selected_item = self.get_selected_item()
            data = self.showView.create_dict_from_input()
            self.database.update_item_by_id(selected_item['metadata']['id'], data)
            self.showView.refresh_Treeview()
        except:
            print('Updating failed!')

    """
        Delete the selected item
    """
    def delete_data(self):
        try:
            selected_item = self.get_selected_item()
            self.database.delete_item_by_id(selected_item['metadata']['id'])          
            self.showView.refresh_Treeview()
        except:
            print('Deleting failed!')

    """
        Insert data from open cv
    """
    def insert_data(self):
        try:
            self.database.insert_OpenWeather_Data()
            self.showView.refresh_Treeview()
        except:
            print('Inserting failed!')

    """
        Returns the selected item
    """
    def get_selected_item(self):
        focused_item = self.showView.treeview.focus()
        raw_item = self.showView.treeview.item(focused_item)     
        item_id = raw_item['values'][5]   # Object ID of the item            
        return self.database.get_item_by_id(item_id)



    """
        @Override
    """
    def main(self):
        self.showView.main()