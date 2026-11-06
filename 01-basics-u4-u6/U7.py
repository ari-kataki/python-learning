def estraiFrequenzaDi(carattere, stringa):
    """Esercizio 1"""
    if type(carattere) != str or type(stringa) != str:
        print("I parametri formali inseriti non sono corretti!")
    else:
        frequenza = 0

        # # Versione 1
        # for c in stringa:
        #     if c == carattere:
        #         frequenza += 1

        # Versione 2
        frequenza = stringa.count(carattere)
        
        return frequenza

def ottieniSottostringaMaiuscola(inizio, fine, stringa):
    """Esercizio 1"""
    if inizio < 0 or inizio > len(stringa) - 1 or inizio > fine or fine < 0 or fine > len(stringa) - 1:
        print("I parametri formali inseriti non sono corretti!")
    else:
        sottoStringa = stringa[inizio:fine].upper()
        return sottoStringa

if __name__ == "__main__":
    print("Test del modulo ProcessoDiStringhe.py")

    stringaUtente = input("Inserisci una stringa: ")
    carattereUtente = input("Inserisci un carattere di cui cercare la frequenza nella stringa: ")[0]
    inizio = int(input("Inserisci l'indice di inizio della sottostringa: "))
    fine = int(input("Inserisci l'indice di fine della sottostringa: "))

    print(f"Frequenza del carattere {carattereUtente} in {stringaUtente}: {estraiFrequenzaDi(carattereUtente, stringaUtente)}")
    print(f"La stringa in maiuscolo tra l'indice {inizio} incluso e l'indice {fine} escluso è: {ottieniSottostringaMaiuscola(inizio, fine, stringaUtente)}")