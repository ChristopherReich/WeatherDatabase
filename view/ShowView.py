import tkinter as tk
from tkinter import ttk
from view.View import View
from datetime import datetime
from tkinter import filedialog


"""
    View responsible for showing registered customers.
"""



class ShowView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 12
    COLUMN_WIDTH = 200
    TEMPERATURE = ""
    OBJECT_ID = ""
    
    BTN_CAPTION = [
        "Update Data",
        "Delete",
        "Data Export"
        
    ]

    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Time series data")
        self.showController = controller
    
        self._make_mainFrame()
        self._make_title()
        self._show_data()
        self._make_options()
        self._make_field_Temp()

        # Bind the method with TreeViewSelect event.
        self.treeview.bind('<<TreeviewSelect>>', self._on_treeview_select)

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    def _on_treeview_select(self,event):
        item_id = self.treeview.focus()
        data = self.treeview.item(item_id)
        self.showController.item_selected(self.getObjectID(data))
        self._display_selected_item(data)
        self.OBJECT_ID = self.getObjectID(data)

    def getObjectID(self,s):
        s = s["values"]
        result = str(s).split(',')[self.find_heading("ID")].replace("[","").replace("]","")
        return int(result)
    
    def getTemperature(self,s):
        s = s["values"]
        result = str(s).split(',')[self.find_heading("temperature")].replace("[","").replace("]","")
        return int(result)
      
    def find_heading(self,s):
        headings = self.treeview["columns"]
        count = 0
        for heading in headings:
            if heading == s:
                return count
            count = count + 1
     
  
    def _make_field_Temp(self):
        self.lblTemp = tk.Label(self, text="Temperature",font=('Helvetica', 11), width=10)  
        self.lblTemp.pack(side = "left")
        self.tbTemp= tk.Text(self,  height=1, width=3,bg='white') 
        self.tbTemp.pack(side = "left")
             
    def _save_path_dir(self):
        self.askFil = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        return self.askFil
    
    def _load_path_dir(self):
        self.askFil = filedialog.askopenfilename(initialdir = "/",title = "Select file")
        return self.askFil
    
         
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
        title = ttk.Label(self.mainFrame, text="Datenbank Name", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
    
    """
        Displays view's context menu.
        # todo: geht noch nicht
    """
    def _contextMenu_display(self, event):
        self.contextMenu = tk.Menu(self.mainFrame, tearoff=0)
        self.contextMenu.add_command(label="Edit", command=lambda: self.showTreeViewController.btnEdit(self.contextMenu_selectedId))
        self.contextMenu.add_command(label="Delete", command=self.showTreeViewController.btnDel)
        
        # Take data from the row that was clicked
        rowSelected = self.treeview.identify_row(event.y)

        # Check if some data was taken
        if rowSelected:
            # Take data selected and put them in a list
            self.contextMenu_selectedId = self.treeview.item(rowSelected)['text']
            
            # Let the row that was clicked as selected
            self.treeview.focus(rowSelected)
            self.treeview.selection_set(rowSelected)
            
            # Open context menu
            self.contextMenu.selection = self.treeview.set(rowSelected)
            self.contextMenu.post(event.x_root, event.y_root)
    
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
                btn = ttk.Button(frame_btn, text=caption, command=lambda txt=caption: self.showController.btnClicked(txt,self.create_dict()))
            btn.pack(side = "left")
    
    def create_dict(self):
            data = {
                'ID': self.OBJECT_ID,
                'temperature': self._get_updated_temperature()
                }
            return data
    
    """
        Display the selected item in the treeview
    """
    def _display_selected_item(self, item):        
        self.tbTemp.delete("1.0",tk.END)
        self.tbTemp.insert(tk.END, self.getTemperature(item))
        self.TEMPERATURE = self.getTemperature(item)
    
    def _get_updated_temperature(self):
        temp = self.tbTemp.get("1.0",'end-1c') # remove last character
        print(temp)
        return temp


    def _refresh_treeview(self):
        self.treeview.delete(self.treeview.get_children())

    """
        Displays data on screen.
    """
    def _show_data(self):
        data = self.showController.getData()
        self.frame_data = tk.Frame(self.mainFrame)
        self.frame_data.pack(fill="x")
        
        frame_dataView = tk.Frame(self.frame_data)
        frame_dataView.pack()
        
        # Show header
        lbl = ttk.Label(frame_dataView, text='Hier kommt noch der Collection name rein')
        lbl.grid(row=0, column=0, padx=self.PAD, pady=self.PAD)

        # Create a Treeview widget
        self.treeview = ttk.Treeview(frame_dataView)
        self.treeview["columns"] = (tuple(data[0]["metadata"].keys()))
        # Define columns
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
            self.treeview.column(column, width=100, anchor=tk.CENTER)

        # Insert data into the Treeview in the correct order
        for row in data:
            val=[]
            for col in self.treeview['columns']:
                val.append(row["metadata"][col])

            self.treeview.insert('', tk.END, values=val)


        # Put tree view on frame
        self.treeview.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        self.treeview.grid_rowconfigure(0, weight=1)
        self.treeview.grid_columnconfigure(0, weight=1)
        

        
               


        # Add listener for enable the context menu
        #self.treeview.bind("<Button-3>", self._contextMenu_display)
        
        
        #btn = ttk.Button(self.frame_customers, text="Update data", command=self.update)
        #btn.pack()


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
        