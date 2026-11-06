class CifrarioDiGC:
    def __init__(self, spiazzamento):
        self.spiazzamento = spiazzamento

    def cripta(self, messaggio):
        try:
            stringaCifrata = ""

            for carattere in messaggio.lower():
                carattereCifrato = chr((ord(carattere) - ord("a")) + (self.spiazzamento % 26) + ord("a"))
                stringaCifrata += carattereCifrato

            return stringaCifrata
        except:
            print("Errore nella cifratura!")

    def decripta(self, messaggio):
        try:
            stringaCifrata = ""

            for carattere in messaggio.lower():
                carattereCifrato = chr((ord(carattere) - ord("a")) - (self.spiazzamento % 26) + ord("a"))
                stringaCifrata += carattereCifrato

            return stringaCifrata
        except:
            print("Errore nella decifratura!")

if __name__ == "__main__":
    spiazzamento = int(input("Inserisci lo spiazzamento del cifrario: "))
    stringaInChiaro = input("Inserisci un messaggio con solo caratteri dell'alfabeto: ")

    oggettoCifrario = CifrarioDiGC(spiazzamento)
    stringaCifrata = oggettoCifrario.cripta(stringaInChiaro)
    print(f"La stringa cifrata è {stringaCifrata}")
    print(f"Prova della defifratura -> {oggettoCifrario.decripta(stringaCifrata)}")