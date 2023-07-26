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
    #        Global variables
    #-----------------------------------------------------------------------
    PAD = 12
    COLUMN_WIDTH = 200
    OBJECT_ID = ""

    
    BTN_CAPTION = [
        "Update Data",
        "Delete",
        "Insert",
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
        self._make_fields()

        # Bind the method with TreeViewSelect event.
        self.treeview.bind('<<TreeviewSelect>>', self._on_treeview_select)

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    def _on_treeview_select(self,event):
        item_id = self.treeview.focus()
        data = self.treeview.item(item_id)
        self.OBJECT_ID = self.getObjectID(data)
        self._display_selected_item(self.showController.item_selected(self.create_dict()))
        
     
    """
        get the heading, because the treeview can be mixed up
    """    
    def find_heading(self,s):
        headings = self.treeview["columns"]
        count = 0
        for heading in headings:
            if heading == s:
                return count
            count = count + 1
            
    """
        Make the textboxes and labels
    """
    def _make_fields(self):
        color = "black"
        side = "left"
        
        self.lblTemp = tk.Label(self, text="Temperature",font=('Helvetica', 11), width=10)  
        self.lblTemp.pack(side = side)
        self.tbTemp= tk.Text(self,  height=1, width=4,bg=color) 
        self.tbTemp.pack(side = side)
        
        self.lblHum = tk.Label(self, text="Humidity",font=('Helvetica', 11), width=10)  
        self.lblHum .pack(side = side)
        self.tbHum = tk.Text(self,  height=1, width=4,bg=color) 
        self.tbHum .pack(side = side)
        
        self.lblCit = tk.Label(self, text="City",font=('Helvetica', 11), width=10)  
        self.lblCit .pack(side = side)
        self.tbCit = tk.Text(self,  height=1, width=10,bg=color) 
        self.tbCit .pack(side = side)
        
        self.lblpre = tk.Label(self, text="pressure",font=('Helvetica', 11), width=10)  
        self.lblpre .pack(side = side)
        self.tbpre = tk.Text(self,  height=1, width=4,bg=color) 
        self.tbpre .pack(side = side)
        
        self.lblstr = tk.Label(self, text="Street",font=('Helvetica', 11), width=10)  
        self.lblstr .pack(side = side)
        self.tbstr = tk.Text(self,  height=1, width=10,bg=color) 
        self.tbstr .pack(side = side)
        
        self.lblNo = tk.Label(self, text="Number",font=('Helvetica', 11), width=10)  
        self.lblNo .pack(side = side)
        self.tbNo = tk.Text(self,  height=1, width=4,bg=color) 
        self.tbNo .pack(side = side)
        
        self.lblWi = tk.Label(self, text="WindSpeed",font=('Helvetica', 11), width=10)  
        self.lblWi .pack(side = side)
        self.tbWi = tk.Text(self,  height=1, width=15,bg=color) 
        self.tbWi .pack(side = side)
             
    """
        Open path
    """ 
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
    """
        creates the dict from all inputs
    """
    def create_dict(self):
            data = {
                'ID': self.OBJECT_ID,
                'temperature': self.tbTemp.get("1.0",'end-1c'),
                'humidity': self.tbHum.get("1.0",'end-1c'),
                'city': self.tbCit.get("1.0",'end-1c'),
                'street': self.tbstr.get("1.0",'end-1c'),
                'street number': self.tbNo.get("1.0",'end-1c'),
                'windSpeed': self.tbWi.get("1.0",'end-1c'),
                'pressure': self.tbpre.get("1.0",'end-1c'),

                }
            return data
    
    """
        Display the selected item in the treeview
    """
    def _display_selected_item(self, data):        
        self.tbTemp.delete("1.0",tk.END)
        self.tbWi.delete("1.0",tk.END)
        self.tbCit.delete("1.0",tk.END)
        self.tbstr.delete("1.0",tk.END)
        self.tbpre.delete("1.0",tk.END)
        self.tbHum.delete("1.0",tk.END)
        self.tbNo.delete("1.0",tk.END)

        self.tbTemp.insert(tk.END, data[0]['metadata']['temperature'])
        self.tbWi.insert(tk.END, data[0]['metadata']['windSpeed'])
        self.tbCit.insert(tk.END, data[0]['metadata']['city'])
        self.tbstr.insert(tk.END, data[0]['metadata']['street'])
        self.tbpre.insert(tk.END, data[0]['metadata']['pressure'])
        self.tbHum.insert(tk.END, data[0]['metadata']['humidity'])
        self.tbNo.insert(tk.END, data[0]['metadata']['street number'])

    """
        finds the ID of the selected treeview Item
    """
    def getObjectID(self,s):
        s = s["values"]
        result = str(s).split(',')[self.find_heading("ID")].replace("[","").replace("]","")
        return int(result)
    
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
        