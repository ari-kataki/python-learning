from parte1.persona import Persona

class Cliente(Persona):

    def __init__(self, nome, cognome, codiceFiscale):
        super().__init__(nome, cognome, codiceFiscale)
        self.__livelloFedelta = ["bassa", "standard", "alta"]
        self.__totFatture = 0
        self.__fedelta = self.__livelloFedelta[0]
        
    @property
    def livelloFedelta(self):
        return self.__livelloFedelta

    @property
    def fedelta(self):
        return self.__fedelta
    
    @fedelta.setter
    def fedelta(self, fedelta):
        self.__fedelta = fedelta

    @property
    def totFatture(self):
        return self.__totFatture
    
    @totFatture.setter
    def totFatture(self, totFatture):
        self.__totFatture = totFatture
    
    def __str__(self):
        return f"Cliente:\n" + super().__str__() + f"  Fedeltà: {self.fedelta}\n"

if __name__ == "__main__":
    cliente = Cliente("ciao", "bro", "cf")

    print(cliente)
