from Esercizio_1.ProcessoDiStringhe import estraiFrequenzaDi, ottieniSottostringaMaiuscola
from geometry.rettangle import perimeter, area
from geometry import circle

while True:
    esercizioUtente = int(input("Inserisci l'esercizio dell'U6 da svolgere (0 per uscire): "))
    if esercizioUtente == 0:
        break
    match esercizioUtente:
        case 1:
            print("Esercizio 1")

            stringaUtente = input("Inserisci una stringa: ")
            carattereUtente = input("Inserisci un carattere di cui cercare la frequenza nella stringa: ")[0]
            inizio = int(input("Inserisci l'indice di inizio della sottostringa:"))
            fine = int(input("Inserisci l'indice di fine della sottostringa:"))

            print(f"Frequenza del carattere {carattereUtente} in {stringaUtente}: {estraiFrequenzaDi(carattereUtente, stringaUtente)}")
            print(f"La stringa in carattere maiuscolo tra l'indice {inizio} incluso e l'indice {fine} escluso è: {ottieniSottostringaMaiuscola(inizio,fine,stringaUtente)}")
        
        case 2:
            print("Esercizio 2")
            baseUtente = float(input("Inserisci la base del rettangolo: "))
            altezzaUtente = float(input("Inserisci l'altezza del rettangolo: "))
            raggioUtente = float(input("Inserisci il raggio del cerchio: "))

            print(f"Il perimetro del rettangolo con base {baseUtente} e {altezzaUtente} è {perimeter(baseUtente,altezzaUtente)}")
            print(f"L'area del rettangolo con base {baseUtente} e {altezzaUtente} è {area(baseUtente,altezzaUtente)}")
            print(f"Il perimetro del cerchio con raggio {raggioUtente} è {circle.perimeter(raggioUtente)}")
            


