class Bot:
  def __init__(self, name, energy=100, shield=100):
    self.name = name
    self.age = 0
    self.energy = energy 
    self.shield = shield
  
  
  def display_name(self):
    print(self.name)
