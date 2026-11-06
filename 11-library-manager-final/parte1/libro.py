# PARTE 1 - CLASSE CON STATO CONTROLLATO DAI METODI
# Lo stato non ha setter: cambia solo tramite metodi appositi.
# DIZIONARIO DI MODULO - valori possibili dello stato
valoriStatoLibro = {0: "disponibile", 1: "in prestito"}

# CLASSE SENZA EREDITARIETA'
class Libro:
    # COSTRUTTORE
    # Lo stato viene inizializzato sempre al valore di default (0).
    # Non viene passato come parametro: dipende dalla logica del programma.
    def __init__(self, codice, titolo, autore, genere, annoPubblicazione):
        self.__codice = codice
        self.__titolo = titolo
        self.__autore = autore
        self.__genere = genere
        self.__annoPubblicazione = annoPubblicazione
        self.__stato = valoriStatoLibro[0]      # stato iniziale sempre = default

    # PROPERTY + SETTER - un blocco per ogni attributo
    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self, nuovoCodice):
        self.__codice = nuovoCodice

    @property
    def titolo(self):
        return self.__titolo

    @titolo.setter
    def titolo(self, nuovoTitolo):
        self.__titolo = nuovoTitolo

    @property
    def autore(self):
        return self.__autore

    @autore.setter
    def autore(self, nuovoAutore):
        self.__autore = nuovoAutore

    @property
    def genere(self):
        return self.__genere

    @genere.setter
    def genere(self, nuovoGenere):
        self.__genere = nuovoGenere

    @property
    def annoPubblicazione(self):
        return self.__annoPubblicazione

    @annoPubblicazione.setter
    def annoPubblicazione(self, nuovoAnno):
        self.__annoPubblicazione = nuovoAnno

    # PROPERTY SOLA LETTURA - stato
    # Lo stato NON ha setter perche' non deve essere modificato
    # liberamente. Cambia solo tramite i metodi prendiInPrestito()
    # e restituisci().
    @property
    def stato(self):
        return self.__stato

    # METODO: porta lo stato da "disponibile" a "in prestito"
    def prendiInPrestito(self):
        if self.__stato == valoriStatoLibro[0]:
            self.__stato = valoriStatoLibro[1]
        else:
            print(f"Errore: il libro '{self.__titolo}' e' gia' in prestito!")

    # METODO: porta lo stato da "in prestito" a "disponibile"
    def restituisci(self):
        if self.__stato == valoriStatoLibro[1]:
            self.__stato = valoriStatoLibro[0]
        else:
            print(f"Errore: il libro '{self.__titolo}' non risulta attualmente in prestito!")

    # METODO: controlla se l'oggetto e' nel suo stato default
    # Restituisce True o False. Usato nel main e in Prestito.
    def isDisponibile(self):
        return self.__stato == valoriStatoLibro[0]
    
    # __str__
    def __str__(self):
        return (f"----------------\n"
                f"OGGETTO LIBRO\n"
                f"Codice: {self.__codice}\n"
                f"Titolo: {self.__titolo}\n"
                f"Autore: {self.__autore}\n"
                f"Genere: {self.__genere}\n"
                f"Anno di pubblicazione: {self.__annoPubblicazione}\n"
                f"Stato: {self.__stato}\n"
                f"----------------\n")

# BLOCCO DI TEST
if __name__ == "__main__":
    libro1 = Libro("L001", "Il Nome della Rosa", "Umberto Eco", "Romanzo storico", 1980)
    libro2 = Libro("L002", "1984", "George Orwell", "Distopia", 1949)
    print(libro1)
    print(libro2)
    libro1.prendiInPrestito()
    print(f"Stato libro1 dopo prestito: {libro1.stato}")
    libro1.restituisci()
    print(f"Stato libro1 dopo restituzione: {libro1.stato}")
