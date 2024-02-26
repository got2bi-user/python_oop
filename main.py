class Plane(object):
  def __init__ (self, modele:str, color:str, weight:int, power_reserve:int):
    self.modele = modele
    self.color = color
    self.weight = weight
    self.power_reserve = power_reserve
  def fly(self):
    if self.power_reserve <= 0:
      print("Plane is not fly...fuel = 0..")
      return 1
    else:
      print("Fly...")
      self.power_reserve -= 1
      return 0
class Fighter_jet(Plane):
  def __init__(self, modele:str = "airobus", color:str="blue", weight:int= 575000, power_reserve:int = 5000, weapon:str = "minigan", number_missile:int = 5000, max_height:int = 5000, maneuverability:str = 'good'):
    self.weapon = weapon
    self.number_missile = number_missile
    self.max_height = max_height
    self.maneuverability = maneuverability
    super().__init__(modele, color, weight, power_reserve)
  def fire(self):
    if self.number_missile <= 0:
    print("not fire ...number_missile = 0..")
    return 1
  else:
    print("Fire!")
    self.number_missile -= 1
    return 0

obj = Fighter_jet()
obj.fire()
obj.fly()
print(obj.modele)
