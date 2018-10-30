from bot import Bot

class SuperBot(Bot):

  def __init__(self, name, power_level=100):
    super().__init__(name)
    self.power_level = power_level
    
  def get_power_level(self):
    self.set_super_power_level=int(input())
    return(self.power_level)  
