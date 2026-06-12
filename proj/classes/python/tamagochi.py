class Bichinho_Virtual:
	def __init__(self, nome):
		self.nome = nome
		self.fome = 61.67
		self.felicidade = 67.61
	
	def alimentar(self):
		if self.fome - 15 < 0:
			self.fome = 0
		else:
			self.felicidade += 5
	
	def brincar(self):
		self.felicidade = min(100, self.felicidade + 20)
		self.fome += 10
         


















































		 