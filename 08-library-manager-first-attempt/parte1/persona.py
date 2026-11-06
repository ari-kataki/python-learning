class Persona:
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

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

    def __str__(self):
        return (f"****************\n"
                f"OGGETTO PERSONA\n"
                f"Nome: {self.__nome}\n"
                f"Cognome: {self.__cognome}\n"
                f"****************\n")
