class canciones:
    titulo = ""
    artista = ""
    album = ""

    def show(self):
        print(f'La canción {self.titulo} es del artista {self.artista} y pertenece al album {self.album}')

cancion1 = canciones()
cancion1.titulo = "Father and Son"
cancion1.artista = "Cat Stevens"
cancion1.album = "Yusuf"

cancion1.show()