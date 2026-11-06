from parte1.persona import Persona

class Fornitore(Persona):
    def __init__(self, nome, cognome, codiceFiscale, settori: list):
        super().__init__(nome, cognome, codiceFiscale)
        self.__settori = settori

    @property
    def settori(self):
        return self.__settori
    
    @settori.setter
    def settori(self, settori):
        self.__settori = settori

    def __str__(self):
        return f"Fornitore:\n" + super().__str__() + f"  Settore: {self.settori}\n"