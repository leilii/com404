from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
         # load resources
        self.map_image = PhotoImage(file="map.png")
        
        self.bus_image = PhotoImage(file="bus.png")
        

        

        # add components
        self.add_title_label()  
        self.add_map_image_frame()
        self.add_map_image_label()
        #self.add_bus_image_label()

    def add_title_label(self):
        self.title_label=Label()
        self.title_label.pack()
        self.title_label.configure(text="Bus Journey",font="Arial 16")
        
    def add_map_image_frame(self):
        self.map_frame=Frame()
        self.map_frame.pack()
        

    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0 , y=0)
        self.map_image_label.configure(width=400,height=400,image=self.map_image)

    def add_bus_image_label(self):
        self.bus_image_label=Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image,width=50, height=30)
        self.bus_image_label.bind("<Button-1>",self.bus_move)


    def bus_move(self, event):
        self.bus_image_label.place(x=event.x , y=event.y)
