from rpg import Character

class Combatente(Character):

  def __init__(self, nome:str):
    super().__init__(nome, vida = 167)
