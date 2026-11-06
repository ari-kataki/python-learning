
class Album:
    def __init__(self, id, title, artist, year, tracks, sales):
        self.id = id
        self.title = title
        self.artist = artist 
        self.year = year
        self.tracks = tracks
        self.sales = sales

    def updateSales(self, sales):
        if sales < 0:
            print("Numero di vendite non valido")
            return
        self.sales += sales

    def __str__(self):
        return (
            f"ID Album: {self.id}\n"
            f"Titolo: {self.title}\n"
            f"Artista: {self.artist.id}\n"
            f"Anno: {self.year}\n"
            f"Tracce: {self.tracks}\n"
            f"Numero vendite: {self.sales}\n"
        )