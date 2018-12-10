from tkinter import *
from tkinter import messagebox
class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()
    self.x=-1
    self.animat=0
    self.newtext=['Weekly','Monthly','Yearly']
    self.my_message=['each Monday','on the first day of each month','at the start of each year']
    self.animation_status=['Start Animation','Stop Animation']
    # resourses
    
    self.filled_image=PhotoImage("filled.jpg")
    self.empty_image=PhotoImage("empty.gif")
    self.weekly_image=PhotoImage("weekly.gif")
    self.monthly_image=PhotoImage("monthly.gif")
    self.yearly_image=PhotoImage("yearly.gif")
    self.gray_image=PhotoImage("gray.gif")

    # set window attributes
    self.title("Newsletter")
    self.configure(bg="#eee",
                   height=500, 
                   width=500,
                   pady=10)
   
                 
    self.add_heading_label()
    self.add_message_label()
    self.add_email_frame()
    self.add_email_label()
    self.add_entry()
    self.add_image_label()
    self.add_type_frame()
    self.add_type_label()
    self.add_period_type_button()
    self.add_subscribe_button()
    self.add_animation_button()
    self.add_animation_image()
    
  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.pack(fill=X)
    
    # style
    self.heading_label.configure(font="Arial 14",
                                 text="RECEIVE OUR NEWSLETTER",pady=10)

    

  def add_message_label(self):
    # create   
    self.message_label = Label()
    self.message_label.pack(fill=X)
    
    # style
    self.message_label.configure(font="Arial 10",
                                 text="Please enter your email below to receive our newsletter.",pady=10)

  def add_email_frame(self):
    self.email_frame = Frame()
    self.email_frame.pack(fill=X)
    
  def add_email_label(self):
    # create   
    self.email_label = Label(self.email_frame)
    self.email_label.pack(side=LEFT)
        
    # style
    self.email_label.configure(font="Arial 10",
                                 text="Email",padx=10)
  def add_entry(self):
    # create   
    self.entry = Entry(self.email_frame)
    self.entry.pack(sid=LEFT)
    self.entry.configure(fg="#f00")
    self.entry.bind("<KeyRelease>",self.email_released)
    self.entry.bind("<BackSpace>",self.email_removed)
    self.your_email=self.entry.get()

  def add_image_label(self):
    self.image_label=Label(self.email_frame)  
    self.image_label.pack(side=RIGHT)
    self.image_label.configure(image=self.gray_image, height=50,
                                             width=50, pady=10)

    
    
  def add_subscribe_button(self):
      # create
     self.subscribe_button=Button()
     self.subscribe_button.pack(fill=X)
     self.subscribe_button.configure(font="Arial 12", text="subscribe", bg="#F0E0E0")
      # bind events
     self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

  def subscribe_button_clicked(self,event):
      #create
      if len(self.entry.get())==0:
        messagebox.showinfo("NewsLetter", "Please enter your email")
      elif self.x==-1:
        messagebox.showinfo("NewsLetter", "Please select subscribe type")
      else:
        messagebox.showinfo("NewsLetter", "You have sbscribed "+ self.newtext[self.x]+" newsletter! You will receive this "+self.my_message[self.x])

  def email_released(self,event):
      self.image_label.configure(image=self.filled_image, height=50,
                                             width=50, pady=10)
  def add_type_frame(self):
    self.type_frame = Frame()
    self.type_frame.pack(fill=X)
        
  def add_type_label(self):
    # create   
    self.type_label = Label(self.type_frame)
    self.type_label.pack(side=LEFT)
        
    # style
    self.type_label.configure(font="Arial 10",
                                 text="Type",padx=10)
  def add_period_type_button(self):
    # create 
     self.period_type_button = Button(self.type_frame)
     self.period_type_button.pack(side=LEFT)
     
    # style
     self.period_type_button.configure(text="subscribtion type",font="Arial 10",padx=10,width= 30)
     #bind event
     self.period_type_button.bind("<ButtonRelease-1>",self.change_option)

  def change_option(self,event):
      if self.x<2:
       self.x=self.x+1
      else:
        self.x=0
      self.period_type_button.configure(text=self.newtext[self.x])

   
  def email_removed(self,event):
         user_text=self.entry.get()
         if len(user_text)==0:
           self.image_label.configure(image=self.empty_image, height=50,
                                             width=50, pady=10)
           messagebox.showinfo("NewsLetter", "Please don't go")
      
     
  def add_animation_button(self):
      # create
     self.animation_button=Button()
     self.animation_button.pack(fill=X)
     self.animation_status="Start Animation"
     self.animation_button.configure(font="Arial 12", text=self.animation_status, bg="#F0E0E0")
      # bind events
     self.animation_button.bind("<ButtonRelease-1>", self.animation_button_clicked)


  def animation_button_clicked(self,event):    
        if self.animation_status=="Start Animation":
            self.animation_status="Stop Animation"
            if self.newtext[self.x]=="Weekly":
               self.animation_image_label.configure(text="weekly",
                                                #image=self.weekly_image, height=50, width=50,
                                                )
            elif self.newtext[self.x]=="Monthly":
               self.animation_image_label.configure(text="Mothly",
                                                #image=self.weekly_image, height=50, width=50,
                                                )
            else:
               self.animation_image_label.configure(text="Yearly",
                                                #image=self.weekly_image, height=50, width=50,
                                                )
        else:
          self.animation_status="Start Animation"
          #self.animation_image_label.delete(0, END)
          #self.animation_image_label.configure(fg="#eee")

        self.animation_button.configure(text=self.animation_status)

  def add_animation_image(self):

      self.animation_image_label=Label()

      self.animation_image_label.pack()
      self.animation_image_label.configure(text="Weekly",
                                           padx=10,pady=10
                                           #image=self.weekly_image, height=50, width=50,
                                           )
    
      
  # the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop()
