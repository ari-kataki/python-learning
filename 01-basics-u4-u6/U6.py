def ottieniLunghezzaStringhe(l):
    """Esercizio 1"""
    dizionario = dict()
    
    if(type(l) == list):
        for stringa in l:
            if(type(stringa) == str):dizionario[stringa] = len(stringa)
    else:
        print("Il parametro passato in ingresso non è una lista")

    return dizionario

def ottieniStringaLungaInTabella(t, rigaInizio = 0, rigaFine = -1):
    """"Esercizio 2"""
    errore = False

    inizioRicerca = 0
    fineRicerca = 0

    if type(t) != list and type(t) != tuple:
        errore = True
    else:
        for riga in t:
            if type(riga) != list and type(riga) != tuple:
                errore = True
                break
            else:
                for colonna in riga:
                    if type(colonna) != str:
                        errore = True
                        break
                if errore == True:
                    break

        if rigaFine == -1:
            fineRicerca = len(t) - 1
        elif rigaFine >= 0 and rigaInizio >= 0:
            if rigaInizio > rigaFine:
                inizioRicerca = rigaFine
                fineRicerca = rigaInizio
            else:
                if rigaInizio > len(t) - 1 or rigaFine > len(t) - 1:
                    errore = True
                else:
                    inizioRicerca = rigaInizio
                    fineRicerca = rigaFine

    if errore == True:
        print("Parametri formali non validi!")
    else:
        stringaMassima = ""
        for indiceRiga in range(inizioRicerca, fineRicerca + 1):
            for indiceColonna in range(0, len(riga)):
                if len(stringaMassima) < len(t[indiceRiga][indiceColonna]):
                    stringaMassima = t[indiceRiga][indiceColonna]

        return stringaMassima
    
def filtraEOrdina(d):
    """Esercizio 3"""
    errore = False

    if type(d) != dict:
        errore = True
    else:
        for chiave in d.keys():
            if type(chiave) != str:
                errore = True
                break

            if type(d[chiave]) != int:
                errore = True
                break

    if errore:
        print("Parametri formali non validi!")
    else:
        listaDizionario = list(d.items())
        listaMaggiorenni = list()

        # # Versione 1
        # for elemento in listaDizionario:
        #     if elemento[1] >= 18:
        #         listaMaggiorenni.append(elemento)

        # Versione 2
        listaMaggiorenni = list(filter(lambda elemento: elemento[1] >= 18, listaDizionario))
        listaMaggiorenni.sort(key=lambda elemento: elemento[1])

        listaNomiDaRitornare = [elemento[0] for elemento in listaMaggiorenni]
        return listaNomiDaRitornare
def ottieniStatistiche(l):
    errore = False
    if type(l) != list:
        errore = True
    else:
        for elemento in l:
            if type(elemento) != int and type(elemento) != float:
                errore = True
                break   # ← optional but good to stop early

    if errore:
        print("Parametri formali non validi!")
    else:
        #v1
        minimo = min(l)
        massimo = max(l)
        medio = sum(l) / len(l)
        listaDaRitornare = [minimo, massimo, medio]

        #v2
        listaFunzioni = [min, max, lambda lista: sum(lista) / len(lista)]
        listaDaRitornare = list(map(lambda funzione: funzione(l), listaFunzioni))

        return listaDaRitornare
def stampaTriangoloTartaglia(n):
    """esc 5"""
    errore = False

    if type(n) != int or n < 0:
        errore = True

    if errore:
        print("parametri formali non validi")
    else:
        #phase 1
        listaTartaglia = list()
        for riga in range(0, n):
            listaRiga = list()
            for colonna in range(0,n):
                if colonna == 0:
                    listaRiga.append(1)
                else:
                    listaRiga.append(0)
            listaTartaglia.append(listaRiga)
        #phase 2
        for riga in range(1,n):
            for colonna in range(1, riga + 1):
                listaTartaglia[riga][colonna] = listaTartaglia[riga - 1][colonna - 1] + listaTartaglia[riga - 1][colonna]
                
        #phase 3
        for riga in range(0, n):
            for colonna in range(0,riga + 1):
                if colonna == riga:
                    print(listaTartaglia[riga][colonna])
                else:
                    print(listaTartaglia[riga][colonna], end= "\t")

def ritornaRigaTartaglia(n):
    """esc 6"""
    if n < 0: 
        print("parametri formali non validi!")
    else:
        rigaTartaglia = list()

        if n == 0:
            rigaTartaglia.append(1)
        else:
            rigaTartagliaPrecendete =ritornaRigaTartaglia(n - 1)
            rigaTartaglia.append(1)
            # rigaTartaglia.append(rigaTartagliaPrecendete[0] + rigaTartagliaPrecendete[1])
            # rigaTartaglia.append(rigaTartagliaPrecendete[1] + rigaTartagliaPrecendete[2])
            for colonna in range(1, n):
                 rigaTartaglia.append(rigaTartagliaPrecendete[colonna - 1] + rigaTartagliaPrecendete[colonna])
            rigaTartaglia.append(1)

        return rigaTartaglia
    
while True:
    esercizioUtente = int(input("Inserisci l'esercizio dell'U6 da svolgere (0 per uscire): "))

    if esercizioUtente == 0:
        break

    match esercizioUtente:
        case 1:
            print("Esercizio 1")
            numeroUtente = int(input("Inserisci il numero di stringhe da digitare: "))
            listaUtente = list()

            for i in range(numeroUtente):
                stringaUtente = input(f"Inserisci la stringa numero {i + 1}: ")
                listaUtente.append(stringaUtente)

            print(f"La lista di stringhe dell'utente è: {listaUtente}")

            dizionarioUtente = ottieniLunghezzaStringhe(listaUtente)
            print(f"Il dizionario ottenuto dalla funzione ottieniLunghezzaStringhe() è:{dizionarioUtente}")
        case 2:
            print("Esercizio 2")
            # Creazione tabella
            tabella = list()
            numeroRighe = int(input("Inserisci il numero di righe della tabella: "))
            numeroColonne = int(input("Inserisci il numero di colonne della tabella: "))

            for indiceRiga in range(0, numeroRighe):
                listaRiga = list()
                for indiceColonna in range(0, numeroColonne):
                    listaRiga.append(input(f"Inserisci la string in posizione [{indiceRiga + 1}][{indiceColonna + 1}]: "))
                tabella.append(listaRiga)

            # Stampa tabella
            print("La tabella dell'utente è:")
            for indiceRiga in range(0, numeroRighe):
                for indiceColonna in range(0, numeroColonne):
                    if indiceColonna == numeroColonne - 1:
                        print(tabella[indiceRiga][indiceColonna])
                    else:
                        print(tabella[indiceRiga][indiceColonna], end="\t")

            # Ricerca della stringa più lunga
            stringaMassima = ottieniStringaLungaInTabella(tabella)
            print(f"La stringa più lunga è {stringaMassima}")
        case 3:
            print("Esercizio 3")
            # Creazione del dizionario
            dizionario = dict()
            numeroPersone = int(input("Inserisci il numero di persone del dizionario: "))
            for indice in range(0, numeroPersone):
                nomeUtente = input(f"Inserisci il nome numero {indice + 1}: ")
                dizionario[nomeUtente] = int(input(f"Inserisci l'età della persona numero {indice + 1}: "))

            # Stampa del dizionario
            print(dizionario)

            # Stampa la lista di maggiorenni in ordine crescente
            print(filtraEOrdina(dizionario))
        case 4:
            print("esc 4")
            #creazione della lista di numeri
            listaUtente = list()
            numeroUtente = int(input(f"inserisci il numero di elementi della lista: "))
            for indice in range(0, numeroUtente):
                listaUtente.append(float(input(f"inserisci il numero (float o int) in posizione {indice+1}: ")))
        case 5:
            print("esc 5")
            numeroUtente = int(input("inserisci la base del triangolo di tartaglia: "))
            print(f"triangolo di tartaglia con base {numeroUtente}:")
            stampaTriangoloTartaglia(numeroUtente)
        case 6:
            print("Esc 6")
            numeroUtente = int(input("inserisci la base del triangolo di tartaglia: "))
            for riga in range(0, numeroUtente +1):
                print(*ritornaRigaTartaglia(riga),sep="\t")
