import os
from RecordLabel import RecordLabel

FILE_NAME = "record_label.json"
INITIAL_FILE = "initial_data.json"


def main():
    label = RecordLabel()

    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        print("File record_label.json non trovato o vuoto.")
        print("Caricamento dati iniziali...")
        label.loadDataFromFile(INITIAL_FILE)
        print("Puoi ora modificare i dati.")
    else:
        label.loadDataFromFile(FILE_NAME)
        label.printAll()

    while True:
        print("\nMENU")
        print("1. Aggiungi artista")
        print("2. Aggiungi album")
        print("3. Modifica numero album artista")
        print("4. Modifica ascolti artista")
        print("5. Modifica vendite album")
        print("6. Stampa archivio")
        print("7. Artisti più ascoltati")
        print("8. Album più venduti")
        print("9. Salva dati")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            label.addArtist()

        elif scelta == "2":
            label.addAlbum()

        elif scelta == "3":
            id = input("ID artista: ")
            artista = next((a for a in label.artists if a.id == id), None)
            if artista:
                n = int(input("Numero da aggiungere/togliere: "))
                artista.updateAlbums(n)

        elif scelta == "4":
            id = input("ID artista: ")
            artista = next((a for a in label.artists if a.id == id), None)
            if artista:
                n = int(input("Numero ascolti da aggiungere: "))
                artista.updateStreams(n)

        elif scelta == "5":
            id = input("ID album: ")
            album = next((a for a in label.albums if a.id == id), None)
            if album:
                n = int(input("Numero vendite da aggiungere: "))
                album.updateSales(n)

        elif scelta == "6":
            label.printAll()

        elif scelta == "7":
            t = int(input("Soglia ascolti: "))
            for a in label.getMostStreamedArtists(t):
                print(a)

        elif scelta == "8":
            t = int(input("Soglia vendite: "))
            for a in label.getBestSellingAlbums(t):
                print(a)

        elif scelta == "9":
            label.saveDataToFile(FILE_NAME)
            print("Dati salvati!")

        elif scelta == "0":
            print("Uscita dal programma.")
            break


if __name__ == "__main__":
    main()