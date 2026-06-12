from rpg import Hero, Character

class Mago( Character ):

  def __init__(self, nome:str):
    super().__init__(nome, vida = 90)
