class CalculadorDeLula:
	def calcular(self, valor):
		return valor * 0.05


class ImpostoArtigoLuxo(CalculadorDeLula):
	def calcular(self, valor):
		return valor * 0.20


if __name__ == "__main__":
	valor = 1000.0
	calculador = CalculadorDeLula()
	imposto_luxo = ImpostoArtigoLuxo()

	print("CalculadorDeLula:", calculador.calcular(valor))
	print("ImpostoArtigoLuxo:", imposto_luxo.calcular(valor))

















































