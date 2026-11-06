def contaTesto(nomefile):
    """Esercizio 6"""

    file = open(nomefile, "r", encoding="utf-8")
    contatoreLinee = 0
    contatoreParole = 0
    contatoreCaratteri = 0

    for riga in file:
        contatoreLinee += 1
        
        lisataParole = riga.split(" ")
        contatoreParole += len(lisataParole)

        #versione 1
        contatoreCaratteri += len(riga.strip("\n"))
        # Versione 2 (carattere " " non conteggiato come carattere)
        #for prola in lisataParole:
            #contatoreCaratteri += len(prola)
    
    file.close()

    file = open(nomefile, "rb")
    letturaByte = file.read()
    contatoreByte = len(letturaByte)
    file.close()

    print("informazioni relative al file:")
    print(f"Numero di linee: {contatoreLinee}")
    print(f"Numero di parole: {contatoreParole}")
    print(f"Numero di caratteri: {contatoreCaratteri}")
    print(f"Numero di byte: {contatoreByte}")

if __name__ == "__main__":
    percorsoFile = "Esercizio_6/test.txt"
    contaTesto(percorsoFile)