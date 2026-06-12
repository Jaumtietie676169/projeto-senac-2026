class Termometro:
	def __init__(self, temperatura_atual: float):
		self.temperatura_atual = float(temperatura_atual)

	def aumentar(self, graus: float):
		self.temperatura_atual += float(graus)

	def diminuir(self, graus: float):
		self.temperatura_atual -= float(graus)

	def alerta_clima(self) -> str:
		if self.temperatura_atual < 0:
			return "Congelando"
		if 0 <= self.temperatura_atual <= 25:
			return "Agradável"
		return "Muito Quente"
## tem duas atividades iguais que legal essa é uma dessas e a outra é "termometro"

















































