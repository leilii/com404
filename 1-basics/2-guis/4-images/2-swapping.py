from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
         # load resources
        self.cucti_image = PhotoImage(file="cucti.png")
        
        self.mycucti_image = PhotoImage(file="mycucti.png")
        

        

        # add components
        self.add_title_label()  
        self.add_cactus_image_label()
        self.add_flip_button()

    def add_title_label(self):
        self.title_label=Label()
        self.title_label.grid(row=0, column=0)
        self.title_label.configure(text="Cactus Leaves",font="Arial 16")
        
    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cucti_image,
                                             height=200,
                                             width=300)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(text="Flip",font="Arial 16")
        self.flip_button.bind("<ButtonRelease-1>",self.left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>",self.right_button_clicked)

    def left_button_clicked(self,event):
        self.cactus_image_label.configure(image=self.cucti_image)

    def right_button_clicked(self,event):
        self.cactus_image_label.configure(image=self.mycucti_image)
        
