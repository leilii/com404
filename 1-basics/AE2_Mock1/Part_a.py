from tkinter import *
from tkinter import messagebox
class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Newsletter")
    self.configure(bg="#eee",
                   height=500, 
                   width=500,
                   pady=10)
   
    self.default_image=PhotoImage("default.png")               
    self.add_heading_label()
    self.add_message_label()
    self.add_email_frame()
    self.add_email_label()
    self.add_entry()
    self.add_image_label()
    self.add_subscribe_button()

  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.pack()
    
    # style
    self.heading_label.configure(font="Arial 14",
                                 text="RECEIVE OUR NEWSLETTER",pady=10)

    

  def add_message_label(self):
    # create   
    self.message_label = Label()
    self.message_label.pack()
    
    # style
    self.message_label.configure(font="Arial 10",
                                 text="Please enter your email below to receive our newsletter.",pady=10)

  def add_email_frame(self):
    self.email_frame = Frame()
    self.email_frame.pack()
    
  def add_email_label(self):
    # create   
    self.email_label = Label(self.email_frame)
    self.email_label.pack(side=LEFT)
        
    # style
    self.email_label.configure(font="Arial 10",
                                 text="Email",pady=10)
  def add_entry(self):
    # create   
    self.entry = Entry(self.email_frame)
    self.entry.pack(side=LEFT)
    self.entry.configure(fg="#f00")

  def add_image_label(self):
    self.image_label=Label(self.email_frame)  
    self.image_label.pack(side=RIGHT)
    self.image_label.configure(image=self.default_image, height=50,
                                             width=50, pady=10)
    
  def add_subscribe_button(self):
      # create
     self.subscribe_button=Button()
     self.subscribe_button.pack()
     self.subscribe_button.configure(font="Arial 12", text="subscribe", bg="#F0E0E0")
      # bind events
     self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

  def subscribe_button_clicked(self,event):
      #create
      messagebox.showinfo("NewsLetter", "Subscribe")
 
  
     
  # the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop()
