from tkinter import *

from tkinter import messagebox

class Gui(Tk):

  # initialise window

  def __init__(self):

    super().__init__()

      # resourses
    
    self.season_image=PhotoImage(file="season.gif")
    self.unknown_image=PhotoImage(file="unknown.gif")
    self.spring_image=PhotoImage(file="spring.gif")
    self.autumn_image=PhotoImage(file="autumn.gif")
    self.summer_image=PhotoImage(file="summer.gif")
    self.winter_image=PhotoImage(file="winter.gif")
    
    self.add_head_frame() 
    self.add_season_image_label()  
    self.add_heading_label()
    self.add_season_frame()
    self.add_season_label()
    self.add_season_entry()
    self.add_messag_frame()
    self.add_message_label()
    self.add_message_frame()
    self.add_message_entry()
    self.add_instruction_label()
    self.add_selected_season_label()
    self.add_send_button()


    self.season=["Summer","Spring","Automn","Winter"]
    self.season_images=[self.summer_image,self.spring_image,self.autumn_image,self.winter_image]
    self.season_num=-1
    self.typed_season=""

  
    # set window attributes

    self.title("Greetings")

    self.configure(bg="#fd6666",
                   height=300, 

                   width=300,

                   pady=10,
                   padx=10)
  def add_head_frame(self):

    self.head_frame = Frame()

    self.head_frame.pack(fill=X)
    self.head_frame.configure(bg="#ff4141",pady=10,
                   padx=10)
    
  def add_season_image_label(self):
      self.season_image_label=Label(self.head_frame)
      self.season_image_label.pack(fill=X)
      self.season_image_label.configure(image=self.season_image,bg="#ff4141")  

  def add_heading_label(self):

    # create   

    self.heading_label = Label()

    self.heading_label.pack(fill=X)
 

    

    # style

    self.heading_label.configure(font="Arial 16",

                                 text="SEND GREETING" ,padx=10,bg="#ff4141",fg="#fff")

  def add_season_frame(self):

    self.season_frame = Frame()

    self.season_frame.pack(fill=X)
    self.season_frame.configure(bg="#ff4141")

    

  def add_season_label(self):

    # create   

    self.season_label = Label(self.season_frame)

    self.season_label.pack(side=LEFT)

        

    # style

    self.season_label.configure(font="Arial 10",pady=10,padx=10,

                                 text="Season:",bg="#ff4141",fg="#fff")


      
  def add_season_entry(self):

    # create   

    self.season_entry = Entry(self.season_frame)

    self.season_entry.pack(side=LEFT)
    self.season_entry.configure()
    self.season_entry.bind("<KeyRelease>",self.selected_season)

  def selected_season(self,event):
      self.typed_season=self.season_entry.get()  
      if self.typed_season==self.season[0]:
        self.selected_season_label.configure(image=self.season_images[0])
      elif self.typed_season==self.season[1]:
        self.selected_season_label.configure(image=self.season_images[1])
      elif self.typed_season==self.season[2]:
        self.selected_season_label.configure(image=self.season_images[2])
      elif self.typed_season==self.season[3]:
        self.selected_season_label.configure(image=self.season_images[3])
      else:
        self.selected_season_label.configure(image=self.unknown_image)


  def add_message_frame(self):

    self.message_frame = Frame()

    self.message_frame.pack(fill=X)
    self.message_frame.configure(pady=10,padx=10,bg="#ff4141")


  def add_messag_frame(self):

    self.messag_frame = Frame()

    self.messag_frame.pack(fill=X)
    self.messag_frame.configure(pady=10,padx=10,bg="#ff4141")                             
  def add_message_label(self):
      self.message_label=Label( self.messag_frame)
      self.message_label.pack(side=LEFT)
      self.message_label.configure(font="Arial 10",padx=0,
                                 text="Message:         ",bg="#ff4141",fg="#fff" )

  def add_message_entry(self):

    # create   

    self.message_entry = Entry(self.message_frame)

    self.message_entry.pack(fill=X)
    self.message_entry.configure()

  def add_instruction_label(self):
      self.instruction_label=Label(self.message_frame)
      self.instruction_label.pack(fill=X)
      self.instruction_label.configure(font="Arial 10",pady=10,padx=10,
                                       text="Please complete all fields and then click send.",bg="#ff4141",fg="#fff" )
  def add_selected_season_label(self):
      self.selected_season_label=Label(self.message_frame)
      self.selected_season_label.pack()
      self.selected_season_label.configure(image=self.unknown_image)
  def add_send_button(self):
      self.send_button=Button(self.message_frame)
      self.send_button.pack(fill=X)
      self.send_button.configure(text="Send",font="Arial 10",bg="#ff0")
      self.send_button.bind("<ButtonRelease-1>",self.send_button_clicked)

  def send_button_clicked(self,event):
      if self.message_entry.get()=="":  
          messagebox.showinfo("Error!", "Please enter a message")        
      elif self.season_entry.get()=="Summer": 
             messagebox.showinfo("Sent!", "Your summer greeting is shining strong!")
      elif self.season_entry.get()=="Winter": 
             messagebox.showinfo("Sent!", "Your winter greeting is making its way..!")
      elif self.season_entry.get()=="Autumn": 
             messagebox.showinfo("Sent!", "Your autumn greeting is falling whit the leaves...!")
      elif self.season_entry.get()=="Spring":
             messagebox.showinfo("Sent!", "Your Spring greeting is blossoming...!")
      else: 
       messagebox.showinfo("Error!", "Please enter a valid season")
      
      # the object

if __name__ == "__main__":

    gui = Gui()    

    gui.mainloop()
