class Persona:
    def __init__(self, nome, cognome, codiceFiscale):
        self.__nome = nome
        self.__cognome = cognome
        self.__codiceFiscale = codiceFiscale

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cognome(self):
        return self.__cognome
    
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome

    @property
    def codiceFiscale(self):
        return self.__codiceFiscale
    
    @codiceFiscale.setter
    def codiceFiscale(self, codiceFiscale):
        self.__codiceFiscale = codiceFiscale
    
    def __str__(self):
        return (
            f"  Nome: {self.nome}\n"
            f"  Cognome: {self.cognome}\n"
            f"  Codice Fiscale: {self.codiceFiscale}\n"
        )
    
if __name__ == "__main__":

    listaPersone = list()

    lengthLista = int(input("Quante persone vuoi aggiungere? "))

    for _ in range(lengthLista):
        nome = str(input("Inserisci il nome: "))
        cognome = str(input("Inserisci il cognome: "))
        codiceFiscale = str(input("Inserisci il codice fiscale: "))
        persona = Persona(nome, cognome, codiceFiscale)
        listaPersone.append(persona)

    for persona in listaPersone:
        print(persona)
    
