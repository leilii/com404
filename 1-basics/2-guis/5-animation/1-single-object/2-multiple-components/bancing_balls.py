        
    # the timer tick function    
    def tick(self):
        self.ball1_x_pos = self.ball1_x_pos + self.ball1_x_change
        self.ball1_y_pos = self.ball1_y_pos + self.ball1_y_change
        #top
        if (self.ball1_y_pos<=0):
            self.ball1_y_change=self.ball1_y_change* -1
        #right
        if (self.ball1_x_pos>=450):
            self.ball1_x_change=self.ball1_x_change* -1
        #botton
        if (self.ball1_x_pos<=0): 
           self.ball1_x_change=self.ball1_x_change* -1
        # left
        if (self.ball1_y_pos>=450):
           self.ball1_y_change=self.ball1_y_change* -1
        self.ball1_image_label.place(x=self.ball1_x_pos, 
                                    y=self.ball1_y_pos)



        self.ball2_x_pos = self.ball2_x_pos + self.ball2_x_change
        self.ball2_y_pos = self.ball2_y_pos + self.ball2_y_change
        #top
        if (self.ball2_y_pos<=0):
            self.ball2_y_change=self.ball2_y_change* -1
        #right
        if (self.ball2_x_pos>=450):
            self.ball2_x_change=self.ball2_x_change* -1
        #botton
        if (self.ball2_x_pos<=0): 
           self.ball2_x_change=self.ball2_x_change* -1
        # left
        if (self.ball2_y_pos>=450):
           self.ball2_y_change=self.ball2_y_change* -1
        self.ball2_image_label.place(x=self.ball2_x_pos, 
                                    y=self.ball2_y_pos)
        

        self.after(100, self.tick)
    # the ball1 image
    def add_ball1_image_label(self):
        self.ball1_image_label = Label()
        self.ball1_image_label.place(x=self.ball1_x_pos,
                                    y=self.ball1_y_pos)
        self.ball1_image_label.configure(image=self.ball1_image)
            # the ball2 image
    def add_ball2_image_label(self):
        self.ball2_image_label = Label()
        self.ball2_image_label.place(x=self.ball2_x_pos,
                                    y=self.ball2_y_pos)
        self.ball2_image_label.configure(image=self.ball2_image)


     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()
