# PARTE 1 - CLASSE FIGLIA CON LISTA DI OGGETTI COLLEGATI
# Eredita da Persona e aggiunge attributi propri.

from parte1.persona import Persona

# VARIABILE DI MODULO - limite numerico
# Usata per controllare quanti oggetti collegati puo' avere
# un oggetto di questa classe.
limiteLibriInPrestito = 3

# CLASSE FIGLIA
class Utente(Persona):

    # COSTRUTTORE CLASSE FIGLIA
    # Chiama sempre super().__init__() con i parametri del padre.
    # Aggiunge i nuovi attributi propri della classe figlia.
    def __init__(self, matricola, nome, cognome):
        super().__init__(nome, cognome)         # chiama il costruttore del padre
        self.__matricola = matricola
        self.__libriInPrestito = list()   # parte sempre vuota

    # PROPERTY + SETTER - matricola
    @property
    def matricola(self):
        return self.__matricola

    @matricola.setter
    def matricola(self, nuovaMatricola):
        self.__matricola = nuovaMatricola

    # PROPERTY SOLA LETTURA - libriInPrestito
    # Non ha setter perche' la lista si modifica solo tramite metodi.
    @property
    def libriInPrestito(self):
        return self.__libriInPrestito

    # METODO: aggiunge un oggetto alla lista con controllo limite
    def aggiungiLibro(self, libro):
        if len(self.__libriInPrestito) < limiteLibriInPrestito:
            self.__libriInPrestito.append(libro)    # aggiunge alla lista
        else:
            print(f"Errore: l'utente {self.__matricola} ha gia' raggiunto il limite di {limiteLibriInPrestito} libri in prestito!")

    # METODO: rimuove un oggetto dalla lista con controllo esistenza
    def rimuoviLibro(self, libro):
        if libro in self.__libriInPrestito:
            self.__libriInPrestito.remove(libro)
        else:
            print("Errore: il libro non risulta in prestito per questo utente!")

    # METODO: restituisce il numero di oggetti nella lista
    def numeroLibriInPrestito(self):
        return len(self.__libriInPrestito)

    # __str__
    def __str__(self):
        return (f"****************\n"
                f"OGGETTO UTENTE\n"
                f"Matricola: {self.__matricola}\n"
                f"Nome: {self.nome}\n"
                f"Cognome: {self.cognome}\n"
                f"Libri in prestito: {self.numeroLibriInPrestito()}/{limiteLibriInPrestito}\n"
                f"****************\n")

# BLOCCO DI TEST - eseguito solo se il file viene avviato direttamente
if __name__ == "__main__":
    numeroUtenti = int(input("Inserisci il numero di oggetti Utente da creare: "))
    listaUtenti = list()

    for i in range(numeroUtenti):
        matricola = input(f"Inserisci la MATRICOLA dell'utente numero {i + 1}: ")
        nome = input(f"Inserisci il NOME dell'utente numero {i + 1}: ")
        cognome = input(f"Inserisci il COGNOME dell'utente numero {i + 1}: ")
        utente = Utente(matricola, nome, cognome)
        listaUtenti.append(utente)

    for utente in listaUtenti:
        print(utente)
