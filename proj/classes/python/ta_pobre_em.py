class SaldoInsuficienteError(Exception):
	def __init__(self, falta):
		super().__init__(f"Saldo insuficiente: faltam {falta}")
		self.falta = falta

class ContaBancaria:
	def __init__(self, saldo=0):
		self.saldo = saldo

	def sacar(self, valor):
		if valor > self.saldo:
			falta = valor - self.saldo
			raise SaldoInsuficienteError(falta)
		self.saldo -= valor
		return valor