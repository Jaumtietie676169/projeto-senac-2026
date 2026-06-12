class AnatomiaError(Exception):
	pass


class Instrumento:
	def tocar(self):
		raise AnatomiaError("Classes teu não tocam som")


class Guitarra(Instrumento):
	def tocar(self):
		return "Guitarra: som gerado"


if __name__ == "__main__":
	try:
		inst = Instrumento()
		inst.tocar()
	except AnatomiaError as e:
		print(f"Erro: {e}")

	try:
		g = Guitarra()
		print(g.tocar())
	except AnatomiaError as e:
		print(f"Erro: {e}")
		







































