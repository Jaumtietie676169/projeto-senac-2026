class Documento:
    def exibir(self):
        return 'Texto genérico do tche'

## chora não but vo fzr duas "paginas" pra essa bomba não butzin
class PDF(Documento):
    def exibir(self):
        return 'Exibindo arquivo PDFCAGADO'


class Imagem(Documento):
    def exibir(self):
        return 'Mostrando action figure cagado'


documentos = [PDF(), Imagem()]

for documento in documentos:
    print(documento.exibir())















































    