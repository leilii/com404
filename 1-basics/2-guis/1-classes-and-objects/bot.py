# blue print
class Bot:
  def __init__(self, name, energy, shield):
    self.name = name
    self.age = 0
    self.energy = energy 
    self.shield = shield
    
  def display_name(self):
    print(self.name)

  def display_age(self):
    print(self.age) 

  def display_energy(self):
    print(self.energy) 

  def display_shield(self):
    print(self.shield)
     
  def __str__(self):
   self.display_name()
   self.display_age()
   self.display_energy()
   self.display_shield()
   return(self.name+" "+str(self.age)+" "+str(self.energy)+" "+str(self.shield))
 # object
beep = Bot("Beep", 100, 100)
print(beep)
