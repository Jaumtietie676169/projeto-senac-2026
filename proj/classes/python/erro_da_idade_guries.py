class IdadeInvalidaError(Exception):
    pass

def cadastrar_eleitor(idade):
    if idade < 16:
        raise IdadeInvalidaError("A idade mínima é 16 lil bro.")
    
    return "Eleitor tche tche + brabo, gg pra tu boi.!"


























































