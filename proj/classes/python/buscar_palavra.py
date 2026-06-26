def buscar_palavra_no_texto(palavra_alvo):
    with open("documento.txt", "r") as arquivo:
        for indice, linha in enumerate(arquivo):
            if palavra_alvo.lower() in linha.lower():
                numero_linha = indice + 1
                texto = linha.txt()
                print(f"Linha {numero_linha}: {texto}")

