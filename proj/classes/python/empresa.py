class Empresa:

	def __init__(self, nome_empresa):
		self.nome_empresa = nome_empresa
		self.funcionarios = []
	
	def contratar(self, nome_funcionario):
		self.funcionarios.append(nome_funcionario)
	
	def demitir(self, nome_funcionario):
		if nome_funcionario in self.funcionarios:
			self.funcionarios.remove(nome_funcionario)
	
	def verificar_funcionario(self, nome_funcionario):
		return nome_funcionario in self.funcionarios
	


















































	