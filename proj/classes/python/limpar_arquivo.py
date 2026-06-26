def limpar_arquivo(origem, destino):
    entrada = open(origem, "r")
    saida = open(destino, "w")

    for linha in entrada:
        if linha.strip():
            saida.write(linha)

    entrada.close()
    saida.close()
























































    