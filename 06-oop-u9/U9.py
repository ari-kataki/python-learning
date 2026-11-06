class CifrarioDiGC:
    def __init__(self, spiazzamento):
        self.spiazzamento = spiazzamento

    def cripta(self, messaggio):
        try:
            stringaCifrata = ""
            
            for carattere in messaggio.lower():
                carattereCifrata = chr((ord(carattere) - ord("a")) + (self.spiazzamento % 26) + ord("a"))
                stringaCifrata += carattereCifrata
            
            return stringaCifrata
        except:
            print("Errore nella cifratura")
            
    def decripta(self, messaggio):
        try:
            stringaDecifrata = ""
            
            for carattere in messaggio.lower():
                carattereDecifrata = chr((ord(carattere) - ord("a")) - (self.spiazzamento % 26) + ord("a"))
                stringaDecifrata += carattereDecifrata
            
            return stringaDecifrata
        except:
            print("Errore nella decifratura")

if __name__ == "__main__":
    spiazzamento = int(input("Inserisci lo spiazzamento: "))
    stringaInChiaro = input("Inserisci la stringa in chiaro: ")    
    stringaDecifrata = ""
    
    oggettoCifrario = CifrarioDiGC(spiazzamento)
    stringaCifrata = oggettoCifrario.cripta(stringaInChiaro)
    stringaDecifrata = oggettoCifrario.decripta(stringaCifrata)
    print(f"la stringa cifrata è: {stringaCifrata} e la stringa decifrata è: {stringaDecifrata}")