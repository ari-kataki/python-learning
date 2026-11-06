# PARTE 1 - CLASSE BASE


class Persona:

    # COSTRUTTORE
    # Inizializza tutti gli attributi privati con doppio underscore.
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    # PROPERTY + SETTER
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovoNome):
        self.__nome = nuovoNome

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, nuovoCognome):
        self.__cognome = nuovoCognome

    # __str__
    # Stampa le informazioni dell'oggetto con bordo decorativo.
    def __str__(self):
        return (f"****************\n"
                f"OGGETTO PERSONA\n"
                f"Nome: {self.__nome}\n"
                f"Cognome: {self.__cognome}\n"
                f"****************\n")
