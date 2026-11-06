from parte1.persona import Persona
from parte1.cliente import Cliente
from parte1.fornitore import Fornitore

class Fattura:

    __tipoFattura = ["acquisto", "vendita"]

    def __init__(self, numero, data, importo, persona: Persona):
        self.__numero = numero
        self.__data = data
        self.__importo = importo
        self.__persona = persona.codiceFiscale
        if isinstance(persona, Cliente):
            self.__tipo = self.__tipoFattura[0]
            persona.totFatture += 1
            if 10 <= persona.totFatture < 40:
                persona.fedelta = persona.livelloFedelta[1]
            elif persona.totFatture  >= 40:
                persona.fedelta = persona.livelloFedelta[2]
            else:
                persona.fedelta = persona.livelloFedelta[0]
        elif isinstance(persona, Fornitore):
            self.__tipo = self.__tipoFattura[1]

    @property
    def numero(self):
        return self.__numero

    @property
    def tipo(self):
        return self.__tipo
    
    # @tipo.setter
    # def tipo(self, tipo):
    #     self.__tipo = tipo
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def importo(self):
        return self.__importo
    
    @importo.setter
    def importo(self, importo):
        self.__importo = importo

    @property
    def persona(self):
        return self.__persona
    
    def __str__(self):
        return (
            f"Fattura:\n"
            f" Numero: {self.numero}\n"
            f" Tipo: {self.__tipo}\n"
            f" Data: {self.data}\n"
            f" Importo: {self.importo}\n"
            f" {self.persona}\n"
        )
        

if __name__ == "__main__":

    listaFatture = list()

    lengthLista = int(input("Quante fatture vuoi aggiungere? "))

    for _ in range(lengthLista):
        numero = int(input("Inserisci il numero: "))
        tipo = str(input(f"Inserisci il tipo tra {Fattura.__tipoFattura}: "))
        data = str(input("Inserisci la data: "))
        importo = float(input("Inserisci l'importo: "))
        fattura = Fattura(numero, tipo, data, importo)
        listaFatture.append(fattura)

    for fattura in listaFatture:
        print(fattura)