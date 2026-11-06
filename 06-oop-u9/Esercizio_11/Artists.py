class Artist:
    def __init__(self, id, name, genre, albums_published, streams):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums_published = albums_published
        self.streams = streams

    def updateAlbums(self, numAlbums):
        if self.albums_published + numAlbums < 0:
            print("Number of albums published cannot be negative")
            return
        self.albums_published += numAlbums

    def updateStreams(self, numStreams):
        if numStreams < 0:
            print("Number of streams cannot be negative")
            return
        self.streams += numStreams

    def __str__(self):
        return (
            f"Id Artist: {self.id}\n"
            f"Name: {self.name}\n"
            f"Genere: {self.genre}\n"
            f"Album published: {self.albums_published}\n"
            f"total streams: {self.streams}\n"
        )