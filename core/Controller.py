import os
import importlib
from Config import APP_PATH
import abc


"""
    Responsible for the communication between views and models in addiction to
    being responsible for the behavior of the program.
"""
class Controller(metaclass=abc.ABCMeta):
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Executes controller and associated view with it.
    """
    @abc.abstractmethod
    def main(self):
        return
    
    """
        Given a view name, return an instance of it
    
        @param viewName:string View to be opened
    """
    def loadView(self, viewName):
        response = None
        
        # Set view name
        viewName = viewName[0].upper()+viewName[1:]+"View"
        
        # Check if file exists
        if os.path.exists(APP_PATH+"/view/"+viewName+".py"):
            module = importlib.import_module("view."+viewName)
            class_ = getattr(module, viewName)
            response = class_(self)
        
        return response
    