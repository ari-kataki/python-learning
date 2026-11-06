class Orologio:
    def __init__(self, ore, minuti, secondi):
        if type(ore) != int or type(minuti) != int or type(secondi) != int:
            raise Exception
        else:
            self.ore = ore
            self.minuti = minuti
            self.secondi = secondi

    def __str__(self):
        stringa = "Oggetto Orologio:\n"
        stringa += f"Ore->{self.ore}\n"
        stringa += f"Minuti->{self.minuti}\n"
        stringa += f"Secondi->{self.secondi}"
        return stringa

    def contaSecodiDaMezzanotte(self):
        secondiTotali = self.ore*3600 + self.minuti*60 + self.secondi

    def aggiungiTempo(self, ore, minuti, secondi):
        secondiDaAumentare = secondi % 60
        minutiDaAumentare = minuti % 60 + (secondi // 60)
        oreDaAumentare = (ore % 24) + (minuti // 60 + secondi // 3600)

        temporaneo1 = (self.secondi + secondiDaAumentare) // 60
        self.secondi = (self.secondi + secondiDaAumentare) % 60
        temporaneo2 = (self.minuti + minutiDaAumentare + temporaneo1) // 60
        self.minuti = (self.minuti + minutiDaAumentare + temporaneo1) % 60
        self.ore = (self.ore + oreDaAumentare + temporaneo2) % 24

    def verificaMomento(self):
        stringa = ""

        if 8 <= self.ore <= 12 and 0 <= self.minuti <= 59 and 0 <= self.secondi <= 59:
            stringa = "Mattina"
        elif 13 <= self.ore <= 19 and 0 <= self.minuti <= 59 and 0 <= self.secondi <= 59:
            stringa = "Pomeriggio"
        elif 20 <= self.ore <= 22 and 0 <= self.minuti <= 59 and 0 <= self.secondi <= 59:
            stringa = "Sera"
        else:
            stringa = "Notte"

        return stringa
    
if __name__ == "__main__":
    orologio = Orologio(3, 14, 22)
    print(orologio)
    print(f"I secondi passati dalla mezzanotte sono {orologio.contaSecodiDaMezzanotte()}")
    print(f"Momento della giornata->{orologio.verificaMomento()}")
    oreDaAggiungere = int(input("Inserisci le ore da aggiungere all'orologio: "))
    minutiDaAggiungere = int(input("Inserisci iminuti da aggiungere all'orologio: "))
    secondiDaAggiungere = int(input("Inserisci i secondi da aggiungere all'orologio: "))
    orologio.aggiungiTempo(oreDaAggiungere, minutiDaAggiungere, secondiDaAggiungere)
    print(orologio)