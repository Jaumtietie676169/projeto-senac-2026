class Playlist:
    def __init__(self, nome):
        self.nome   = nome
        self.musicas = [] 

    def adicionar_musica(self, nome_musica):
        self.musicas.append(nome_musica)

    def remover_musica(self, nome_musica):
        if nome_musica in self.musicas:
            self.musicas.remove(nome_musica)
        else:
            print("'{nome_musica}' não encontrada na playlist do TCHê TCHê.")

    def mostrar_playlist(self):
        print(f"Playlist: {self.nome}")
        for musica in self.musicas:
            print("- {musica}")
















































