from persona import Persona

class Dipendente (Persona):
    def __init__(self, nome, cognome, lavoro):
        super().__init__(nome, cognome)
        self.lavoro = lavoro

    def lavora(self):
        print(f"{self.nome} lavora come {self.lavoro}")

    def __str__(self):
        stringa = super().__str__()
        stringa += f"lavora ->{self.lavoro}"
        return stringa 

if __name__ == "__main__":
    dipendente1 = Dipendente("Paolo","Rossi","Mathteach")
    dipendente1.mangia("Mela")
    dipendente1.lavora()
    dipendente1.dorme()