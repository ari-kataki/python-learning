from parte1.utente import Utente
from parte1.libro import Libro

valoriStatoPrestito = {0: "attivo", 1: "chiuso"}

class Prestito:
    def __init__(self, utente: Utente, libro: Libro):
        if not libro.isDisponibile():
            raise Exception(f"Il libro '{libro.titolo}' non e' disponibile per il prestito!")

        self.__utente = utente
        self.__libro = libro
        self.__stato = valoriStatoPrestito[0]

        self.__libro.prendiInPrestito()
        self.__utente.aggiungiLibro(self.__libro)

    @property
    def utente(self):
        return self.__utente

    @property
    def libro(self):
        return self.__libro

    @property
    def stato(self):
        return self.__stato

    def restituisciLibro(self):
        if self.__stato == valoriStatoPrestito[1]:
            raise Exception("Questo prestito e' gia' chiuso!")
        self.__libro.restituisci()
        self.__utente.rimuoviLibro(self.__libro)
        self.__stato = valoriStatoPrestito[1]

    def isAttivo(self):
        return self.__stato == valoriStatoPrestito[0]

    def __str__(self):
        return (f"---------------\n"
                f"OGGETTO PRESTITO\n"
                f"Utente: {self.__utente.matricola} - {self.__utente.nome} {self.__utente.cognome}\n"
                f"Libro: {self.__libro.codice} - {self.__libro.titolo}\n"
                f"Stato: {self.__stato}\n"
                f"---------------\n")

if __name__ == "__main__":
    from parte1.utente import Utente
    from parte1.libro import Libro

    utente = Utente("MAT001", "Lewis", "Hamilton")
    libro = Libro("L001", "Il Nome della Rosa", "Umberto Eco", "Romanzo storico", 1980)

    print(f"Stato libro prima del prestito: {libro.stato}")
    prestito = Prestito(utente, libro)
    print(f"Stato libro dopo il prestito: {libro.stato}")
    print(prestito)
    prestito.restituisciLibro()
    print(f"Stato libro dopo la restituzione: {libro.stato}")
    print(prestito)
