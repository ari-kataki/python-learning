import json
from Artists import Artist
from Albums import Album


class RecordLabel:
    def __init__(self):
        self.artists = []
        self.albums = []

    def addArtist(self):
        id = input("ID artista: ")
        name = input("Nome artista: ")
        genre = input("Genere musicale: ")
        albums = int(input("Numero album pubblicati: "))
        streams = int(input("Numero ascolti totali: "))

        artist = Artist(id, name, genre, albums, streams)
        self.artists.append(artist)

    def addAlbum(self):
        id = input("ID album: ")
        title = input("Titolo: ")
        artist_id = input("ID artista: ")

        artist = next((a for a in self.artists if a.id == artist_id), None)
        if not artist:
            print("Artista non trovato!")
            return

        year = int(input("Anno pubblicazione: "))
        tracks = int(input("Numero tracce: "))
        sales = int(input("Numero copie vendute: "))

        album = Album(id, title, artist, year, tracks, sales)
        self.albums.append(album)

    def saveDataToFile(self, fileName):
        data = {
            "artists": [
                {
                    "id": a.id,
                    "name": a.name,
                    "genre": a.genre,
                    "albums_published": a.albums_published,
                    "streams": a.streams,
                }
                for a in self.artists
            ],
            "albums": [
                {
                    "id": al.id,
                    "title": al.title,
                    "artist_id": al.artist.id,
                    "year": al.year,
                    "tracks": al.tracks,
                    "sales": al.sales,
                }
                for al in self.albums
            ],
        }

        with open(fileName, "w") as f:
            json.dump(data, f, indent=4)

    def loadDataFromFile(self, fileName):
        with open(fileName, "r") as f:
            data = json.load(f)

        self.artists = []
        self.albums = []

        for a in data["artists"]:
            artist = Artist(
                a["id"], a["name"], a["genre"],
                a["albums_published"], a["streams"]
            )
            self.artists.append(artist)

        for al in data["albums"]:
            artist = next((a for a in self.artists if a.id == al["artist_id"]), None)
            if artist:
                album = Album(
                    al["id"], al["title"], artist,
                    al["year"], al["tracks"], al["sales"]
                )
                self.albums.append(album)

        print("File caricato con successo!")

    def getBestSellingAlbums(self, threshold):
        best = [a for a in self.albums if a.sales > threshold]
        if not best:
            print("Nessun album best seller")
        return best

    def getMostStreamedArtists(self, threshold):
        top = [a for a in self.artists if a.streams > threshold]
        if not top:
            print("Nessun artista con ascolti elevati")
        return top

    def printAll(self):
        print("\n--- ARTISTI ---")
        for a in self.artists:
            print(a)

        print("\n--- ALBUM ---")
        for al in self.albums:
            print(al)