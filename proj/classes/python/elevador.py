class ElevadorSobrecargadoError(Exception):
	pass

class Elevador:
	def __init__(self):
		self.peso_total = 0
	
	def entrar_pessoa(self, peso_pessoa):
		if self.peso_total + peso_pessoa > 400:
			raise ElevadorSobrecargadoError("Elevador com muitos gurizes!")
























































