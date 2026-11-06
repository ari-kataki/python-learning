from parte1.allenatore import Allenatore
from parte1.giocatore import Giocatore
from parte1.squadra import Squadra
from functions import *
import json
import subprocess
import os

datiSocieta = "./datiSocieta.json"

try:
    with open(datiSocieta, "r", encoding="utf-8") as file:
        dataBase = json.load(file)
        listAllenatori = list()
        listGiocatori = list()
        listSquadre = list()
        listAllenatoriJSON = dataBase["allenatori"]
        listGiocatoriJSON = dataBase["giocatori"]
        listSquadreJSON = dataBase["squadre"]

        for allenatore in listAllenatoriJSON:
            allenatore = Allenatore(allenatore["cF"], allenatore["nome"], allenatore["cognome"], allenatore["anni"], allenatore["categoria"])
            listAllenatori.append(allenatore)
        
        for giocatore in listGiocatoriJSON:
            giocatore = Giocatore(giocatore["cF"], giocatore["nome"], giocatore["cognome"], giocatore["anni"], giocatore["ruolo"])
            listGiocatori.append(giocatore)
        
        for squadra in listSquadreJSON:
            squadra = Squadra(squadra["nome"], squadra["codiceFiscaleAllenatore"], squadra["codiciFiscaliGiocatori"], squadra["vinte"], squadra["perse"], squadra["pareggiate"])
            squadra.assegnaCategoria(listAllenatori)
            listSquadre.append(squadra)

except FileNotFoundError:
    
    print("Non esistono dati nel database!")

    listAllenatori = list()
    listGiocatori = list()
    listSquadre = list()

    #CREA ALLENATORI

    while True:
    
        userNumAllenatori = int(input("Quanti allenatori vuoi aggiungere? "))
        if type(userNumAllenatori) == int and userNumAllenatori >= 1:
            break
        else:
            print("Inserisci un numero valido!")

    for _ in range(userNumAllenatori):
    
        userAllenatoreNome = str(input("Inserisci il nome dell'allenatore: "))
        userAllenatoreCognome = str(input("Inserisci il cognome dell'allenatore: "))
        while True:

            userAllenatoreCF = input("Inserisci il codice fiscale dell'allenatore: ")
            isUnique = True

            for allenatore in listAllenatori:
                if userAllenatoreCF == allenatore.cF:
                    isUnique = False
                    break

            if isUnique:
                break
            else:
                print("Codice fiscale già presente, inseriscine un altro.")
        
        while True:

            userAllenatoreEta = int(input("Inserisci l'età dell'allenatore: "))
            if 24 < userAllenatoreEta < 68 and type(userAllenatoreEta) == int:
                break
            else:
                print("Inserisci un'età valida!")
        
        print("\nCategorie disponibili:")
        
        for categoria in allenatore.categoriaList:
            print(f"\n -{categoria}", end="\n")
        
        while True:

            userAllenatoreCategoria = str(input("\nInserisci la categoria dell'allenatore: "))
            if userAllenatoreCategoria in allenatore.categoriaList:
                break

        
        allenatore = Allenatore(userAllenatoreCF, userAllenatoreNome, userAllenatoreCognome, userAllenatoreEta , userAllenatoreCategoria)
        listAllenatori.append(allenatore)
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
    for allenatore in listAllenatori:
        print(allenatore)
    
    #CREA GIOCATORI

    while True:
        userNumGiocatori = int(input("Quanti giocatori vuoi aggiungere? "))
        if type(userNumGiocatori) == int and userNumGiocatori >= 1:
            break
        else:
            print("Inserisci un numero valido!")

    for _ in range(userNumGiocatori):
    
        userGiocatoreNome = str(input("Inserisci il nome del giocatore: "))
        userGiocatoreCognome = str(input("Inserisci il cognome del giocatore: "))
        while True:

            userGiocatoreCF = input("Inserisci il codice fiscale del giocatore: ")
            isUnique = True

            for giocatore in listGiocatori:
                if userGiocatoreCF == giocatore.cF:
                    isUnique = False
                    break

            if isUnique:
                break
            else:
                print("Codice fiscale già presente, inseriscine un altro.")
        
        while True:

            userGiocatoreEta = int(input("Inserisci l'età del giocatore: "))
            if 5 <= userGiocatoreEta <= 19 and type(userGiocatoreEta) == int:
                break
            else:
                print("Inserisci un'eta valida!")

        print("\nLista ruoli:")

        for ruolo in Giocatore.ruoloList:
            print(f"\n -{ruolo}", end="\n")
        
        while True:

            userGiocatoreRuolo = str(input("Inserisci il ruolo del giocatore: "))
            if userGiocatoreRuolo in Giocatore.ruoloList:
                break
        
        giocatore = Giocatore(userGiocatoreCF, userGiocatoreNome, userGiocatoreCognome, userGiocatoreEta, userGiocatoreRuolo)
        listGiocatori.append(giocatore)
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
    for giocatore in listGiocatori:
        print(giocatore)
    
    #CREA SQUADRE

    while True:

        userNumSquadre = int(input("Inserisci il numero di squadre che vuoi creare: "))

        if type(userNumSquadre) == int and userNumSquadre >= 1:
            break
        else:
            print("Inserisci un numero valido!")
        
    for _ in range(userNumSquadre):

        userListGiocatoriSquadra = list()
    
        userSquadraNome = str(input("Inserisci il nome della squadra: "))

        for allenatore in listAllenatori:
            print(allenatore, end="\n")
        
        while True:

            userSquadraAllenatore = input(f"Inserisci il codice fiscale dell'allenatore della squadra {userSquadraNome}: ")
            found = False

            for allenatore in listAllenatori:
                if userSquadraAllenatore == allenatore.cF:
                    found = True
                    break

            if found:
                allenatoreCategoria = allenatore.categoriaAllenatore
                allenatoreToCheck = allenatore
                break
            else:
                print("Allenatore non presente, inseriscine un altro.")

        while True:

            userNumGiocatoriSquadra = int(input(f"Inserisci il numero di giocatori che vuoi aggiungere alla squadra {userSquadraNome}: "))

            if type(userNumGiocatoriSquadra) == int and userNumGiocatoriSquadra >= 5:
                break
            else:
                print("Inserisci un numero valido!")

        for _ in range(userNumGiocatoriSquadra):

            while True:

                for giocatore in listGiocatori:
                    if giocatore.cF not in userListGiocatoriSquadra and giocatore.categoria == allenatoreToCheck.categoriaAllenatore:
                        print(giocatore, end="\n")

                userChoice = input("Inserisci il codice fiscale del giocatore: ")
                found = False

                for giocatore in listGiocatori:
                    if userChoice == giocatore.cF:
                        found = True
                        
                        if giocatore.categoria == allenatoreToCheck.categoriaAllenatore:
                            if userChoice not in userListGiocatoriSquadra:
                                for squadra in listSquadre:
                                    if userChoice in squadra.listaGiocatori:
                                        squadra.listaGiocatori.remove(userChoice)
                                userListGiocatoriSquadra.append(userChoice)
                                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                                break
                            else:
                                print("Giocatore già presente nella squadra!")

                if found:
                    break
                else:
                    print("Inserisci un giocatore valido!")
        
        while True:
            userSquadraVittorie = int(input("Inserisci quante vittorie ha la squadra: "))
            if type(userSquadraVittorie) == int and userSquadraVittorie >= 0:
                break
            else:
                print("Inserisci un numero valido!")
        
        while True:
            userSquadraSconfitte = int(input("Inserisci quante sconfitte ha la squadra: "))
            if type(userSquadraSconfitte) == int and userSquadraSconfitte >= 0:
                break
            else:
                print("Inserisci un numero valido!")

        while True:
            userSquadraPareggi = int(input("Inserisci quanti pareggi ha la squadra: "))
            if type(userSquadraPareggi) == int and userSquadraPareggi >= 0:
                break
            else:
                print("Inserisci un numero valido!")

        
        squadra = Squadra(userSquadraNome, userSquadraAllenatore, userListGiocatoriSquadra, userSquadraVittorie, userSquadraSconfitte, userSquadraPareggi, listAllenatori)
        listSquadre.append(squadra)
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        for squadra in listSquadre:
            print(squadra, end="\n")

while True:
    listActions = [
        "\n 1: Aggiungere un nuovo giocatore\n"
        " 2: Aggiungere un nuovo allenatore\n",
        "3: Aggiungere una nuova squadra\n",
        "4: Modificare i dati di un giocatore\n",
        "5: Modificare i dati di un allenatore\n",
        "6: Modifica i dati di una squadra\n",
        "7: Stampare tutte le info dei giocatori\n",
        "8: Stampare tutte le info degli allenatori\n",
        "9: Stampare tutte le info delle squadre\n",
        "10: Calcolare le partite giocate e i punti per ogni squadra\n",
        "11: Salvare i dati aggiornati nel file datiSocieta.json\n",
        "12: Uscire dal programma\n"
    ]

    actions = " ".join(listActions)
    try:
        userAction = int(input(f"\nSelezionare la funzione da svolgere tra: {actions}"))
    
    except ValueError:
        print("Inserire un numero!")

    if userAction == 12:
        print("Programma terminato!")
        break
    
    match userAction:

        case 1:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            while True:
                userNumGiocatori = int(input("Quanti giocatori vuoi aggiungere? "))
                if type(userNumGiocatori) == int and userNumGiocatori >= 1:
                    break
                else:
                    print("Inserisci un numero valido!")

            for _ in range(userNumGiocatori):
            
                userGiocatoreNome = str(input("Inserisci il nome del giocatore: "))
                userGiocatoreCognome = str(input("Inserisci il cognome del giocatore: "))
                while True:

                    userGiocatoreCF = input("Inserisci il codice fiscale del giocatore: ")
                    isUnique = True

                    for giocatore in listGiocatori:
                        if userGiocatoreCF == giocatore.cF:
                            isUnique = False
                            break

                    if isUnique:
                        break
                    else:
                        print("Codice fiscale già presente, inseriscine un altro.")
                
                while True:

                    userGiocatoreEta = int(input("Inserisci l'età del giocatore: "))
                    if 5 <= userGiocatoreEta <= 19 and type(userGiocatoreEta) == int:
                        break
                    else:
                        print("Inserisci un'eta valida!")

                print("\nLista ruoli:")

                for ruolo in giocatore.ruoloList:
                    print(f"\n -{ruolo}", end="\n")
                
                while True:

                    userGiocatoreRuolo = str(input("Inserisci il ruolo del giocatore: "))
                    if userGiocatoreRuolo in giocatore.ruoloList:
                        break
                
                giocatore = Giocatore(userGiocatoreCF, userGiocatoreNome, userGiocatoreCognome, userGiocatoreEta, userGiocatoreRuolo)
                listGiocatori.append(giocatore)
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            
            for giocatore in listGiocatori:
                print(giocatore)
        
        case 2:

            while True:
    
                userNumAllenatori = int(input("Quanti allenatori vuoi aggiungere? "))
                if type(userNumAllenatori) == int and userNumAllenatori >= 1:
                    break
                else:
                    print("Inserisci un numero valido!")

            for _ in range(userNumAllenatori):
            
                userAllenatoreNome = str(input("Inserisci il nome dell'allenatore: "))
                userAllenatoreCognome = str(input("Inserisci il cognome dell'allenatore: "))
                while True:

                    userAllenatoreCF = input("Inserisci il codice fiscale dell'allenatore: ")
                    isUnique = True

                    for allenatore in listAllenatori:
                        if userAllenatoreCF == allenatore.cF:
                            isUnique = False
                            break

                    if isUnique:
                        break
                    else:
                        print("Codice fiscale già presente, inseriscine un altro.")
                
                while True:

                    userAllenatoreEta = int(input("Inserisci l'età dell'allenatore: "))
                    if 24 < userAllenatoreEta < 68 and type(userAllenatoreEta) == int:
                        break
                    else:
                        print("Inserisci un'età valida!")
                
                print("\nCategorie disponibili:")
                
                for categoria in allenatore.categoriaList:
                    print(f"\n -{categoria}", end="\n")
                
                while True:

                    userAllenatoreCategoria = str(input("\nInserisci la categoria dell'allenatore: "))
                    if userAllenatoreCategoria in allenatore.categoriaList:
                        break

                
                allenatore = Allenatore(userAllenatoreCF, userAllenatoreNome, userAllenatoreCognome, userAllenatoreEta , userAllenatoreCategoria)
                listAllenatori.append(allenatore)
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            
            for allenatore in listAllenatori:
                print(allenatore)

        case 3:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            while True:

                userNumSquadre = int(input("Inserisci il numero di squadre che vuoi creare: "))

                if type(userNumSquadre) == int and userNumSquadre >= 1:
                    break
                else:
                    print("Inserisci un numero valido!")
                
            for _ in range(userNumSquadre):

                userListGiocatoriSquadra = list()
            
                userSquadraNome = str(input("Inserisci il nome della squadra: "))

                for allenatore in listAllenatori:
                    print(allenatore, end="\n")
                
                while True:

                    userSquadraAllenatore = input(f"Inserisci il codice fiscale dell'allenatore della squadra {userSquadraNome}: ")
                    found = False

                    for allenatore in listAllenatori:
                        if userSquadraAllenatore == allenatore.cF:
                            found = True
                            break

                    if found:
                        allenatoreCategoria = allenatore.categoriaAllenatore
                        allenatoreToCheck = allenatore
                        break
                    else:
                        print("Allenatore non presente, inseriscine un altro.")

                while True:

                    userNumGiocatoriSquadra = int(input(f"Inserisci il numero di giocatori che vuoi aggiungere alla squadra {userSquadraNome}: "))

                    if type(userNumGiocatoriSquadra) == int and userNumGiocatoriSquadra >= 5:
                        break
                    else:
                        print("Inserisci un numero valido!")

                for _ in range(userNumGiocatoriSquadra):

                    while True:

                        for giocatore in listGiocatori:
                            if giocatore.cF not in userListGiocatoriSquadra and giocatore.categoria == allenatoreToCheck.categoriaAllenatore:
                                print(giocatore, end="\n")

                        userChoice = input("Inserisci il codice fiscale del giocatore: ")
                        found = False

                        for giocatore in listGiocatori:
                            if userChoice == giocatore.cF:
                                found = True
                                
                                if giocatore.categoria == allenatoreToCheck.categoriaAllenatore:
                                    if userChoice not in userListGiocatoriSquadra:
                                        for squadra in listSquadre:
                                            if userChoice in squadra.listaGiocatori:
                                                squadra.listaGiocatori.remove(userChoice)
                                        userListGiocatoriSquadra.append(userChoice)
                                        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                                        break
                                    else:
                                        print("Giocatore già presente nella squadra!")
                        if found:
                            break
                        else:
                            print("Inserisci un giocatore valido!")
                
                while True:
                    userSquadraVittorie = int(input("Inserisci quante vittorie ha la squadra: "))
                    if type(userSquadraVittorie) == int and userSquadraVittorie >= 0:
                        break
                    else:
                        print("Inserisci un numero valido!")
                
                while True:
                    userSquadraSconfitte = int(input("Inserisci quante sconfitte ha la squadra: "))
                    if type(userSquadraSconfitte) == int and userSquadraSconfitte >= 0:
                        break
                    else:
                        print("Inserisci un numero valido!")

                while True:
                    userSquadraPareggi = int(input("Inserisci quanti pareggi ha la squadra: "))
                    if type(userSquadraPareggi) == int and userSquadraPareggi >= 0:
                        break
                    else:
                        print("Inserisci un numero valido!")

                
                squadra = Squadra(userSquadraNome, userSquadraAllenatore, userListGiocatoriSquadra, userSquadraVittorie, userSquadraSconfitte, userSquadraPareggi)
                squadra.assegnaCategoria(listAllenatori)
                listSquadre.append(squadra)
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                for squadra in listSquadre:
                    print(squadra, end="\n")

        case 4:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            editAttr(listGiocatori, "giocatore")

        case 5:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            editAttr(listGiocatori, "allenatore")

        case 6:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            for squadra in listSquadre:
                print(squadra, end="\n")

            done = True

            while done:

                userChoice = str(input(f"Scegliere il nome della squadra tra quelli mostrati: "))

                found = False
                for squadra in listSquadre:
                    if squadra.nome == userChoice:
                        found = True
                        squadraToEdit = squadra
                        break

                if found == True:

                    print(squadra)
                    print(squadraToEdit.categoria)

                    listAttr = list()

                    for attributo in dir(squadra):

                        if not attributo.startswith("__") and not attributo.startswith("_"):
                            if attributo != "listaAllenatori" and attributo != "categoria" and attributo != "assegnaCategoria":
                                listAttr.append(attributo)
                    
                    while True:

                        found = False

                        userChoice = str(input(f"Cosa vuoi modificare della squadra {squadraToEdit.nome}?\n- {" \n- ".join(listAttr)}\n"))

                        if userChoice in listAttr:

                            if userChoice == "allenatoreCF":
                                
                                listAllenatoriValidi = list()
                                for allenatore in listAllenatori:
                                    if allenatore.categoriaAllenatore == squadraToEdit.categoria:
                                        listAllenatoriValidi.append(allenatore.cF)

                                if len(listAllenatoriValidi) == 0:
                                    print("Non ci sono allenatori per questa categoria!")
                                    break
                                else:
                                    found = True
                                    print("Lista dei codici fiscali degli allenatori: ")
                                    for item in listAllenatoriValidi:
                                        print(item, end="\n")
                                        
                                while True:
                                    updatedAttr = str(input(f"Modifica l'attributo {userChoice}: "))
                                    if updatedAttr in listAllenatoriValidi:
                                        break

                            elif userChoice == "listaGiocatori":

                                listGiocatoriSquadra = squadraToEdit.listaGiocatori

                                while True:

                                    userAction = str(input("Vuoi aggiungere o rimuovere giocatori? [aggiungere / rimuovere] "))

                                    if userAction == "aggiungere":
                                        giocatoriAmount = int(input(f"Quanti giocatori vuoi aggiungere alla squadra {squadraToEdit.nome}? "))
                                        for _ in range(giocatoriAmount):
                                            print("Lista giocatori disponibili:")
                                            for giocatore in listGiocatori:
                                                if giocatore.categoria == squadraToEdit.categoria and giocatore.cF not in listGiocatoriSquadra:
                                                    print(f" -{giocatore.cF}", end="\n")
                                            userGiocatoreCF = str(input("Aggiungi il giocatore: "))
                                            for squadra in listSquadre:
                                                if userGiocatoreCF in squadra.listaGiocatori and squadra != squadraToEdit:
                                                    squadra.listaGiocatori.remove(userGiocatoreCF)
                                            listGiocatoriSquadra.append(userGiocatoreCF)
                                        updatedAttr = listGiocatoriSquadra
                                        found = True
                                        break
                                    elif userAction == "rimuovere":
                                        for giocatore in listGiocatoriSquadra:
                                            print(giocatore, end="\n")
                                        while True:
                                            giocatoriAmount = int(input(f"Quanti giocatori vuoi rimuovere dal fornitore {object.nome}? "))
                                            for _ in range(giocatoriAmount):
                                                while True:
                                                    userGiocatoreCF = str(input("Rimuovi il Giocatore: "))
                                                    if userGiocatoreCF in listGiocatoriSquadra:
                                                        listGiocatoriSquadra.remove(userGiocatoreCF)
                                                        break
                                            updatedAttr = listGiocatoriSquadra
                                            break
                                        found = True
                                        break
                            else:
                                found = True
                                updatedAttr = input(f"Modifica l'attributo {userChoice}: ")
                                if userChoice == "nome":
                                    updatedAttr = str(updatedAttr)
                                else:
                                    updatedAttr = int(updatedAttr)
                        
                        if found:

                            setattr(squadraToEdit, userChoice, updatedAttr)
                            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                            print(squadraToEdit)
                            done = False
                            break
                            

        case 7:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("Lista giocatori:\n")
            for giocatore in listGiocatori:
                print(giocatore, end="\n", sep="\n")

        case 8:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("Lista allenatori:\n")
            for allenatore in listAllenatori:
                print(allenatore, end="\n", sep="\n")

        case 9:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            print("Lista squadre:\n")
            for squadra in listSquadre:
                print(squadra, end="\n", sep="\n")

        case 10:
            
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            stampaClassifica(listSquadre)

        case 11:
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            with open(datiSocieta, "w", encoding="utf-8") as file:

                listAllenatoriJSON = []
                listGiocatoriJSON = []
                listSquadreJSON = []

                for allenatore in listAllenatori:
                    cFAllenatore = allenatore.cF
                    nomeAllenatore = allenatore.nome
                    cognomeAllenatore = allenatore.cognome
                    etaAllenatore = allenatore.eta
                    categoriaAllenatore = allenatore.categoriaAllenatore

                    dataSheetAllenatori = {
                        "cF": cFAllenatore,
                        "nome": nomeAllenatore,
                        "cognome": cognomeAllenatore,
                        "anni": etaAllenatore,
                        "categoria": categoriaAllenatore
                    }
                    listAllenatoriJSON.append(dataSheetAllenatori)
                
                for giocatore in listGiocatori:
                    cFGiocatore = giocatore.cF
                    nomeGiocatore = giocatore.nome
                    cognomeGiocatore = giocatore.cognome
                    etaGiocatore = giocatore.eta
                    ruoloGiocatore = giocatore.ruolo
                    dataSheetGiocatori = {
                        "cF": cFGiocatore,
                        "nome": nomeGiocatore,
                        "cognome": cognomeGiocatore,
                        "anni": etaGiocatore,
                        "ruolo": ruoloGiocatore
                    }
                    listGiocatoriJSON.append(dataSheetGiocatori)

                for squadra in listSquadre:
                    nomeSquadra = squadra.nome
                    cFAllenatoreSquadra = squadra.allenatoreCF
                    listaGiocatoriSquadra = squadra.listaGiocatori
                    categoriaSquadra = squadra.categoria
                    vittorieSquadra = squadra.vittorie
                    pareggiSquadra = squadra.pareggi
                    sconfitteSquadra = squadra.sconfitte

                    dataSheetSquadra = {
                        "nome": nomeSquadra,
                        "codiceFiscaleAllenatore":cFAllenatoreSquadra,
                        "codiciFiscaliGiocatori": listaGiocatoriSquadra,
                        "categoria": categoriaSquadra,
                        "vinte": vittorieSquadra,
                        "pareggiate": pareggiSquadra,
                        "perse": sconfitteSquadra
                    }
                    listSquadreJSON.append(dataSheetSquadra)
                
                dataBase = {
                    "giocatori": listGiocatoriJSON,
                    "allenatori": listAllenatoriJSON,
                    "squadre": listSquadreJSON
                }
                
                json.dump(dataBase, file, indent=4)

                print("Salvataggio completato!")