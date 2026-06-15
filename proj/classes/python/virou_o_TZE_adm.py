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
            "Acesso negado! Apenas administradores podem entrosar.")

    print("você tem dado em casa com sucesso!")











































