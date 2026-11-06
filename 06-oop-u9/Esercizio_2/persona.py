class Persona:
    listaGeneri = ["F", "M", "U"]

    def __init__(self, nome, genere, eta):
        self.nome = nome
        self.genere = self.settaGenere(genere)

        self.eta = 0
        for anno in range(eta):
            self.invecchia()

    def settaGenere(self, genereDaVerificare):
        if genereDaVerificare in Persona.listaGeneri:
            return genereDaVerificare
        else:
            return Persona.listaGeneri[2]
        
    def invecchia(self):
        self.eta += 1

    def saluta(self):
        if self.genere == Persona.listaGeneri[0]:
            return "signora"
        elif self.genere == Persona.listaGeneri[1]:
            return "signor"
        else:
            return "signor*"
        
if __name__ == "__main__":
    nomeP1 = "Augusto"
    genereP1 = "M"
    etaP1 = 47

    nomeP2 = "Marianna"
    genereP2 = "F"
    etaP2 = 44

    persona1 = Persona(nomeP1, genereP1, etaP1)
    persona2 = Persona(nomeP2, genereP2, etaP2)

    print(f"{persona1.saluta()} {persona1.nome}: genere->{persona1.genere}; età->{persona1.eta}")
    print(f"{persona2.saluta()} {persona2.nome}: genere->{persona2.genere}; età->{persona2.eta}")
