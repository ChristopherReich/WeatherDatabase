# https://github.com/williamniemiec/MVC-in-Python/tree/master/example

import tkinter as tk
from tkinter import ttk
from view.View import View


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class HomeView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    BTN_CAPTION = [
        "Show data",
        "noch keine funktion",
        "noch keine funktion",
        "Exit"
    ]
    
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Customers Manager")
        self.homeController = controller
        
        self._make_mainFrame()
        self._make_title()
        self._make_options()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Database Manager", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
        
    """
        Creates view's options.
    """
    def _make_options(self):
        frame_btn = ttk.Frame(self.mainFrame)
        frame_btn.pack(fill="x")
        
        for caption in self.BTN_CAPTION:
            if caption == "Exit":
                btn = ttk.Button(frame_btn, text=caption, command=self.destroy)
            else:
                btn = ttk.Button(frame_btn, text=caption, command=lambda txt=caption: self.homeController.btnClicked(txt))
            
            btn.pack(fill="x")
            
    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return