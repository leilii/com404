from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 10
        self.ball_y_pos = 300
        self.ball_x_change = 10
        self.ball_y_change = -10
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        #top
        if (self.ball_y_pos<=0):
            self.ball_y_change=self.ball_y_change* -1
        #right
        if (self.ball_x_pos>=450):
            self.ball_x_change=self.ball_x_change* -1
        #botton
        if (self.ball_x_pos<=0): 
           self.ball_x_change=self.ball_x_change* -1
        # left
        if (self.ball_y_pos>=450):
           self.ball_y_change=self.ball_y_change* -1
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)

        self.after(100, self.tick)
    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()
