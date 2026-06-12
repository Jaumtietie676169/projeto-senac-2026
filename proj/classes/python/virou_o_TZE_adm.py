class Usuario:
    pass


class TZE(Usuario):
    pass


class Comum(Usuario):
    pass


class Admin(Usuario):
    pass


def deletar_banco_de_dados(usuario_objeto):
    if not isinstance(usuario_objeto, Admin):
        raise PermissionError(
            "Acesso negado! Apenas administradores podem deletar o banco de dados."
        )

    print("Banco de dados deletado com sucesso!")


# Testes
admin = Admin()
comum = Comum()

try:
    deletar_banco_de_dados(admin)
except PermissionError as erro:
    print(erro)

try:
    deletar_banco_de_dados(comum)
except PermissionError as erro:
    print(erro)