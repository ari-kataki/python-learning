# PARTE 2 - CLASSE CHE COLLEGA DUE OGGETTI CON UNO STATO
# Collega un oggetto Utente e un oggetto Libro, e ha un proprio stato.

from parte1.utente import Utente
from parte1.libro import Libro

# DIZIONARIO DI MODULO - stati possibili del prestito
valoriStatoPrestito = {0: "attivo", 1: "chiuso"}

# CLASSE DI COLLEGAMENTO
class Prestito:
    # COSTRUTTORE CON PARAMETRO OPZIONALE
    def __init__(self, utente: Utente, libro: Libro, statoIniziale = None):
        self.__utente = utente
        self.__libro = libro

        if statoIniziale == None:
            # MODALITA' NUOVO PRESTITO
            # Controlla che il libro sia disponibile.
            # Se si: imposta stato attivo, cambia stato del libro,
            #        aggiunge il libro alla lista dell'utente.
            # Se no: stampa errore e imposta stato chiuso.
            if libro.isDisponibile():
                self.__stato = valoriStatoPrestito[0]   # stato = attivo
                self.__libro.prendiInPrestito()          # cambia stato del libro
                self.__utente.aggiungiLibro(self.__libro) # aggiunge alla lista utente
            else:
                print(f"Errore: il libro '{libro.titolo}' non e' disponibile per il prestito!")
                self.__stato = valoriStatoPrestito[1]   # stato = chiuso
        else:
            # MODALITA' CARICAMENTO DA FILE
            # Imposta direttamente lo stato senza eseguire la logica.
            # Il libro e l'utente sono gia' stati aggiornati in caricaDati().
            self.__stato = statoIniziale

    # PROPERTY SOLA LETTURA - utente e libro
    # Non hanno setter: un prestito non cambia utente o libro.
    @property
    def utente(self):
        return self.__utente

    @property
    def libro(self):
        return self.__libro

    # PROPERTY SOLA LETTURA - stato
    @property
    def stato(self):
        return self.__stato

    # METODO: chiude il prestito e ripristina lo stato degli oggetti collegati
    # Poi: ripristina il libro, rimuove dalla lista dell'utente, chiude il prestito.
    def restituisciLibro(self):
        if self.__stato == valoriStatoPrestito[0]:      # se attivo
            self.__libro.restituisci()                  # ripristina stato libro
            self.__utente.rimuoviLibro(self.__libro)    # rimuove da lista utente
            self.__stato = valoriStatoPrestito[1]       # chiude il prestito
        else:
            print("Errore: questo prestito e' gia' chiuso!")

    # METODO: controlla se il prestito e' ancora aperto
    # Restituisce True o False. Usato nel main per filtrare.
    def isAttivo(self):
        return self.__stato == valoriStatoPrestito[0]

    # __str__
    def __str__(self):
        return (f"~~~~~~~~~~~~~~~~\n"
                f"OGGETTO PRESTITO\n"
                f"Utente: {self.__utente.matricola} - {self.__utente.nome} {self.__utente.cognome}\n"
                f"Libro: {self.__libro.codice} - {self.__libro.titolo}\n"
                f"Stato: {self.__stato}\n"
                f"~~~~~~~~~~~~~~~~\n")

# BLOCCO DI TEST
if __name__ == "__main__":
    utente = Utente("MAT001", "Mario", "Rossi")
    libro = Libro("L001", "Il Nome della Rosa", "Umberto Eco", "Romanzo storico", 1980)

    print(f"Stato libro prima del prestito: {libro.stato}")
    prestito = Prestito(utente, libro)
    print(f"Stato libro dopo il prestito: {libro.stato}")
    print(prestito)
    prestito.restituisciLibro()
    print(f"Stato libro dopo la restituzione: {libro.stato}")
    print(prestito)
