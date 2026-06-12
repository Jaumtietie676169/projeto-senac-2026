class Conta:
    def __init__(self):
        self.saldo = 100


class ContaEstudante(Conta):
    def render_bonus(self):
        self.saldo += 10


conta = ContaEstudante()
print(conta.saldo)

conta.render_bonus()
print(conta.saldo)



















































