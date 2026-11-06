from parte1.persona import Persona

LIMITE_LIBRI_IN_PRESTITO = 3

class Utente(Persona):
    def __init__(self, matricola, nome, cognome):
        super().__init__(nome, cognome)
        self.__matricola = matricola
        self.__libriInPrestito = list()

    @property
    def matricola(self):
        return self.__matricola

    @matricola.setter
    def matricola(self, nuovaMatricola):
        self.__matricola = nuovaMatricola

    @property
    def libriInPrestito(self):
        return self.__libriInPrestito

    def aggiungiLibro(self, libro):
        if len(self.__libriInPrestito) >= LIMITE_LIBRI_IN_PRESTITO:
            raise Exception(f"L'utente {self.__matricola} ha gia' raggiunto il limite massimo di {LIMITE_LIBRI_IN_PRESTITO} libri in prestito!")
        self.__libriInPrestito.append(libro)

    def rimuoviLibro(self, libro):
        if libro in self.__libriInPrestito:
            self.__libriInPrestito.remove(libro)
        else:
            raise Exception("Il libro non risulta in prestito per questo utente!")

    def numeroLibriInPrestito(self):
        return len(self.__libriInPrestito)

    def __str__(self):
        return (f"****************\n"
                f"OGGETTO UTENTE\n"
                f"Matricola: {self.__matricola}\n"
                f"Nome: {self.nome}\n"
                f"Cognome: {self.cognome}\n"
                f"Libri in prestito: {self.numeroLibriInPrestito()}/{LIMITE_LIBRI_IN_PRESTITO}\n"
                f"****************\n")

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
