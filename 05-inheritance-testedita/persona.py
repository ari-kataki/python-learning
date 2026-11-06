class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome 
        self.cognome = cognome 

    def mangia(self, cibo):
        print(f"{self.nome} sta mangiando {cibo}")
              
    def dorme(self):
        print(f"{self.nome} sta dormendo")

    def __str__(self):
        stringa = "Ogetto Persona\n"
        stringa += f"Nome->{self.nome}\n"
        stringa += f"Cognome->{self.cognome}\n"
        return stringa