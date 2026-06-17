def calcular_medias_alunos():

    nomes_e_medias = []

    try:
        with open('proj/classes/python/notas.txt') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) < 3:
                    continue
                nome = dados[0]
                nota1 = float(dados[1])
                nota2 = float(dados[2])
                media = (nota1 + nota2) / 2

                nomes_e_medias.append({'nome': nome, 'media': media})
    except FileNotFoundError:
        print('Arquivo não encontrado!!!')
        return
    finally:
        if not nomes_e_medias:
            return None

        with open('medias_finais.txt', 'w') as arquivo:
            for objeto in nomes_e_medias:
                arquivo.write(f"{objeto.get('nome')}, {objeto.get('media')}\n")








































