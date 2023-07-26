import tkinter as tk
from tkinter import ttk
from view.View import View
from tkinter import filedialog


"""
    View responsible for showing registered customers.
"""
class ShowView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Global variables
    #-----------------------------------------------------------------------
    PAD = 12
    COLUMN_WIDTH = 300
    
    BTN_CAPTION = [
        'Update Data',
        'Delete',
        'Insert',
        'Data Export'
    ]

    COLUMNS = {
        'nr'            : 'Nr',
        'temperature'   : 'Temperature',
        'humidity'      : 'Humidity',
        'pressure'      : 'Pressure',
        'windSpeed'     : 'Wind speed',
        '_id'           : 'Object ID'
    }

    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title('Time series data')
        self.showController = controller
    
        self._make_mainFrame()
        self._make_title()
        self._make_treeview()
        self._make_options()
        self._make_fields()
        self._show_data_in_treeview()


    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------      
                 
    """
        Make the textboxes and labels
    """
    def _make_fields(self):
        color = 'white'
        side = 'left'
        
        self.lblObjectId = tk.Label(self, text='Object Id',font=('Helvetica', 11), width=10)  
        self.lblObjectId.pack(side = side)
        self.tbObjectId= tk.Text(self,  height=1, width=15,bg='gray90') 
        self.tbObjectId.pack(side = side)

        self.lblTemp = tk.Label(self, text='Temperature',font=('Helvetica', 11), width=10)  
        self.lblTemp.pack(side = side)
        self.tbTemp= tk.Text(self,  height=1, width=6,bg=color) 
        self.tbTemp.pack(side = side)  

        self.lblHum = tk.Label(self, text='Humidity',font=('Helvetica', 11), width=10)  
        self.lblHum .pack(side = side)
        self.tbHum = tk.Text(self,  height=1, width=6,bg=color) 
        self.tbHum .pack(side = side)           
        
        self.lblpre = tk.Label(self, text='Pressure',font=('Helvetica', 11), width=10)  
        self.lblpre .pack(side = side)
        self.tbpre = tk.Text(self,  height=1, width=6,bg=color) 
        self.tbpre .pack(side = side)
              
        self.lblWi = tk.Label(self, text='Wind speed',font=('Helvetica', 11), width=10)  
        self.lblWi .pack(side = side)
        self.tbWi = tk.Text(self,  height=1, width=6,bg=color) 
        self.tbWi .pack(side = side)



    """
        Open path
    """ 
    def _save_path_dir(self):
        self.askFil = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        return self.askFil
    
    def _load_path_dir(self):
        self.askFil = filedialog.askopenfilename(initialdir = '/',title = 'Select file')
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
        title = ttk.Label(self.mainFrame, text='Datenbank Name', font=('Helvetica', 20))
        title.pack(padx=self.PAD, pady=self.PAD)
    


    """
        Creates view's options.
    """
    def _make_options(self):
        frame_btn = ttk.Frame(self.mainFrame)
        frame_btn.pack(fill='x')
        
        for caption in self.BTN_CAPTION:
            if caption == 'Exit':
                btn = ttk.Button(frame_btn, text=caption, command=self.destroy)
            else:
                btn = ttk.Button(frame_btn, text=caption, command=lambda txt=caption: self.showController.btnClicked(txt))
            btn.pack(side = 'left')
    


    """
        creates the dict from all inputs
    """
    def create_dict_from_input(self):
            data = {
                'temperature': self.tbTemp.get('1.0','end-1c'),
                'humidity': self.tbHum.get('1.0','end-1c'),           
                'windSpeed': self.tbWi.get('1.0','end-1c'),
                'pressure': self.tbpre.get('1.0','end-1c'),
                }
            return data
    


    """
        Display the selected item in the treeview
    """
    def display_selected_item(self, item):  
        self.tbObjectId.delete('1.0',tk.END)      
        self.tbTemp.delete('1.0',tk.END)
        self.tbWi.delete('1.0',tk.END)
        self.tbpre.delete('1.0',tk.END)
        self.tbHum.delete('1.0',tk.END) 

        self.tbObjectId.insert(tk.END, item['_id'])
        self.tbTemp.insert(tk.END, item['metadata']['temperature'])
        self.tbWi.insert(tk.END, item['metadata']['windSpeed'])
        self.tbpre.insert(tk.END, item['metadata']['pressure'])
        self.tbHum.insert(tk.END, item['metadata']['humidity'])


    """
        Creates the treeview
    """
    def _make_treeview(self):
        self.frame_data = tk.Frame(self.mainFrame)
        self.frame_data.pack(fill='both')
        
        frame_dataView = tk.Frame(self.frame_data)
        frame_dataView.pack()
        
        # Create a Treeview widget
        self.treeview = ttk.Treeview(frame_dataView)
        self.treeview['columns'] = list(self.COLUMNS.keys())
        self.treeview['show']='headings'

        for key, value in self.COLUMNS.items():
            self.treeview.column(key,width=200,anchor='c')
            self.treeview.heading(key, text=value)



    """
        Show the data in the treeview
    """
    def _show_data_in_treeview(self):
        data = self.showController.get_data_from_database()
        # Insert data into the Treeview in the correct order
        for idx, row in enumerate(data):
            val=[idx]
            val.append(row['metadata']['temperature'])
            val.append(row['metadata']['humidity'])
            val.append(row['metadata']['pressure'])
            val.append(row['metadata']['windSpeed'])
            val.append(row['_id'])

            self.treeview.insert('',tk.END, iid=idx, values=val)

        # Put tree view on frame
        self.treeview.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        self.treeview.grid_rowconfigure(0, weight=1)
        self.treeview.grid_columnconfigure(0, weight=1)



    """
        Refresh treeview after updating, deleting, inserting
    """
    def refresh_Treeview(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        self._show_data_in_treeview()


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
        