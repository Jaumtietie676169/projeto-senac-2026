class ItemInutilException(Exception):
	pass

class InventarioCheioException(Exception):
	pass

class Item:
	def __init__(self, nome):
		self.nome = nome

class Espada(Item):
	pass

class Pocao(Item):
	pass

class PedraComum(Item):
	pass

class Inventario:
	def __init__(self):
		self.itens = []
	
	def guardar_item(self, objeto_item):
		if len(self.itens) >= 3:
			raise InventarioCheioException("Inventário cheio!")
		if isinstance(objeto_item, PedraComum):
			raise ItemInutilException("Pedra Comum não pode ser armazenada!")
		self.itens.append(objeto_item)