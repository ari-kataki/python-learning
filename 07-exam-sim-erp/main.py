import json
from parte1.persona import Persona
from parte1.fornitore import Fornitore
from parte1.cliente import Cliente
from parte2.fattura import Fattura
from parte2.bilancio import *
import os
import subprocess
from functions import *

datiERP = "./datiERP.json"

try:
    with open(datiERP, "r", encoding="utf8") as file:

        dataBase = json.load(file)
        listFornitoriJSON = dataBase["fornitori"]
        listClientiJSON = dataBase["clienti"]
        listFattureJSON = dataBase["fatture"]
        listClienti = list()
        listFornitori = list()
        listFatture = list()
        

        for cliente in listClientiJSON:
            cliente = Cliente(cliente["nome"], cliente["cognome"], cliente["cF"])
            listClienti.append(cliente)

        for fornitore in listFornitoriJSON:
            fornitore = Fornitore(fornitore["nome"], fornitore["cognome"], fornitore["cF"], fornitore["settori"])
            listFornitori.append(fornitore)
            
        for fattura in listFattureJSON:
            cFPersona = fattura["cFPersona"]
            for cliente in listClienti:
                if cliente.codiceFiscale == cFPersona:
                    persona = cliente

            for fornitore in listFornitori:
                if fornitore.codiceFiscale == cFPersona:
                    persona = fornitore
                    
            fattura = Fattura(fattura["numero"], fattura["data"], fattura["importo"], persona)
            listFatture.append(fattura)

except FileNotFoundError:

    print("Non esistono dati nel database!")

    listClienti = list()
    listFornitori = list()
    listFatture = list()
    
    userNumFornitori = int(input("Quanti fornitori vuoi aggiungere? "))

    listFornitori = list()

    for _ in range(userNumFornitori):
        userFornNome = str(input("Inserisci il nome del fornitore: "))
        userFornCognome = str(input("Inserisci il cognome del fornitore: "))
        while True:

            userFornCF = input("Inserisci il codice fiscale del fornitore: ")
            isUnique = True

            for fornitore in listFornitori:
                if userFornCF == fornitore.codiceFiscale:
                    isUnique = False
                    break

            if isUnique:
                break
            else:
                print("Codice fiscale già presente, inseriscine un altro.")

        settoriAmount = int(input(f"Quanti settori ha il fornitore {userFornNome}?"))
        listSettori = list()
        for _ in range(settoriAmount):
            userFornSettore = str(input("Inserisci il settore del fornitore: "))
            listSettori.append(userFornSettore)
        
        fornitore = Fornitore(userFornNome, userFornCognome, userFornCF, listSettori)
        listFornitori.append(fornitore)

    userNumClienti = int(input("Quanti clienti vuoi aggiungere? "))

    listClienti = list()

    for _ in range(userNumClienti):
        userCliNome = str(input("Inserisci il nome del cliente: "))
        userCliCognome = str(input("Inserisci il cognome del cliente: "))

        while True:
            
            userCliCF = input("Inserisci il codice fiscale del cliente: ")
            isUnique = True

            for cliente in listClienti:
                if userCliCF == cliente.codiceFiscale:
                    isUnique = False
                    break

            if isUnique:
                break
            else:
                print("Codice fiscale già presente, inseriscine un altro.")

        cliente = Cliente(userCliNome, userCliCognome, userCliCF)
        listClienti.append(cliente)

    userNumFatture = int(input("Quante fatture vuoi aggiungere? "))

    for _ in range(userNumFatture):

        while True:
            
            userFattNumero = input("Inserisci il numero della fattura: ")
            isUnique = True

            for fattura in listFatture:
                if userFattNumero == fattura.numero:
                    isUnique = False
                    break

            if isUnique:
                break
            else:
                print("Numero della fattura già presente, inseriscine un altro.")

        while True:

            tipoFattura = " / ".join(Fattura.tipoFattura)

            userFattTipo = str(input(f"Inserisci il tipo della fattura [{tipoFattura}]: "))

            if userFattTipo in Fattura.tipoFattura:
                break

        userFattData = str(input("Inserisci la data della fattura: "))

        userFattImporto = float(input("Inserisci l'importo della fattura: "))

        userFattPersona = Persona
       
        if userFattTipo == Fattura.tipoFattura[0]:
            for cliente in listClienti:
                print(cliente, end="\n")
            while True:
                userChoice = str(input(f"Scegliere il nome del cliente tra quelli mostrati: "))
                found = False
                for cliente in listClienti:
                    if cliente.nome == userChoice:
                        userFattPersona = cliente
                        found = True
                        break
                if found == True:
                    break
            
            
        elif userFattTipo == Fattura.tipoFattura[1]:
            for fornitore in listFornitori:
                print(fornitore, end="\n")
            while True:
                userChoice = str(input(f"Scegliere il nome del fornitore tra quelli mostrati: "))
                found = False
                for fornitore in listFornitori:
                    if fornitore.nome == userChoice:
                        userFattPersona = fornitore
                        found = True
                        break
                if found == True:
                    break

        fattura = Fattura(userFattNumero, userFattTipo, userFattData, userFattImporto, userFattPersona)

        listFatture.append(fattura)

    for fornitore in listFornitori:
        print(fornitore, end="\n")
    for cliente in listClienti:
        print(cliente, end="\n")
    for fattura in listFatture:
        print(fattura, end="\n")

while True:

    listActions = [
        "\n 1: Aggiungere un nuovo fornitore o cliente\n",
        "2: Aggiungere una nuova fattura\n",
        "3: Modificare i dati di un fornitore o cliente\n",
        "4: Modificare i dati di una fattura\n",
        "5: Calcolare il bilancio (entrate, uscite o saldo)\n",
        "6: Stampare tutte le informazioni dei fornitori o clienti\n",
        "7: Stampare tutte le informazioni delle fatture\n",
        "8: Salvare i dati aggiornati nel file datiERP.json\n",
        "9: Uscire dal programma\n"
    ]
    actions = " ".join(listActions)

    try:
        userAction = int(input(f"\nSelezionare la funzione da svolgere tra: {actions}"))
    
    except ValueError:
        print("Inserire un numero!")

    if userAction == 9:
        print("Programma terminato!")
        break
    
    match userAction:

        case 1:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            while True:

                userChoice = str(input("Vuoi aggiungere un cliente o un fornitore? "))

                if userChoice == "cliente" or userChoice == "fornitore":
                    break

            if userChoice == "cliente":

                userNumClienti = int(input("Quanti clienti vuoi aggiungere? "))

                for _ in range(userNumClienti):
                    userCliNome = str(input("Inserisci il nome del cliente: "))
                    userCliCognome = str(input("Inserisci il cognome del cliente: "))

                    while True:
            
                        userCliCF = input("Inserisci il codice fiscale del cliente: ")
                        isUnique = True

                        for cliente in listClienti:
                            if userCliCF == cliente.codiceFiscale:
                                isUnique = False
                                break

                        if isUnique:
                            break
                        else:
                            print("Codice fiscale già presente, inseriscine un altro.")

                    cliente = Cliente(userCliNome, userCliCognome, userCliCF)
                    print(f"Riepilogo:\n {cliente}")
                    listClienti.append(cliente)

            if userChoice == "fornitore":

                userNumFornitori = int(input("Quanti fornitori vuoi aggiungere? "))

                for _ in range(userNumFornitori):
                    userFornNome = str(input("Inserisci il nome del fornitore: "))
                    userFornCognome = str(input("Inserisci il cognome del fornitore: "))
                    while True:
            
                        userFornCF = input("Inserisci il codice fiscale del fornitore: ")
                        isUnique = True

                        for fornitore in listFornitori:
                            if userFornCF == fornitore.codiceFiscale:
                                isUnique = False
                                break

                        if isUnique:
                            break
                        else:
                            print("Codice fiscale già presente, inseriscine un altro.")

                    settoriAmount = int(input(f"Quanti settori ha il fornitore {userFornNome}?"))
                    listSettori = list()
                    for _ in range(settoriAmount):
                        listSettori.append(userFornSettore = str(input("Inserisci il settore del fornitore: ")))

                    fornitore = Fornitore(userFornNome, userFornCognome, userFornCF, listSettori)
                    print(f"Riepilogo: {fornitore}")
                    listFornitori.append(fornitore)

        case 2:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            userNumFatture = int(input("Quante fatture vuoi aggiungere? "))

            for _ in range(userNumFatture):

                while True:
            
                    userFattNumero = input("Inserisci il numero della fattura: ")
                    isUnique = True

                    for fattura in listFatture:
                        if userFattNumero == fattura.numero:
                            isUnique = False
                            break

                    if isUnique:
                        break
                    else:
                        print("Numero della fattura già presente, inseriscine un altro.")

                userFattData = str(input("Inserisci la data della fattura: "))

                userFattImporto = float(input("Inserisci l'importo della fattura: "))

                userFattPersona = Persona

                while True:

                    userChoice = str(input("La fattura è intestata ad un cliente o a un fornitore? [cliente / fornitore] "))
            
                    if userChoice == "cliente":
                        for cliente in listClienti:
                            print(f"CF Cliente {cliente.nome}: {cliente.codiceFiscale}", end="\n")
                        while True:
                            userChoice = str(input(f"Scegliere il codice fiscale del cliente tra quelli mostrati: "))
                            found = False
                            for cliente in listClienti:
                                if cliente.codiceFiscale == userChoice:
                                    userFattPersona = cliente
                                    found = True
                                    break
                            if found == True:
                                break
                        break
                        
                    elif userChoice == "fornitore":
                        for fornitore in listFornitori:
                            print(f"CF Fornitore {fornitore.nome}: {fornitore.codiceFiscale} ", end="\n")
                        while True:
                            userChoice = str(input(f"Scegliere il codice fiscale del fornitore tra quelli mostrati: "))
                            found = False
                            for fornitore in listFornitori:
                                if fornitore.codiceFiscale == userChoice:
                                    userFattPersona = fornitore
                                    found = True
                                    break
                            if found == True:
                                break
                        break

                fattura = Fattura(userFattNumero, userFattData, userFattImporto, userFattPersona)

                print(fattura)

                listFatture.append(fattura)

        case 3:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            while True:

                userChoice = str(input("Vuoi modificare un cliente o un fornitore? "))

                if userChoice == "cliente":
                    editAttr(listClienti, userChoice)
                    break

                elif userChoice == "fornitore":
                    editAttr(listFornitori, userChoice)
                    break

        case 4:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
             
            for fattura in listFatture:
                print(fattura, end="\n")

            while True:
                
                userChoice = str(input(f"Scegliere il numero della fattura tra quelli mostrati: "))

                found = False

                for fattura in listFatture:

                    if fattura.numero == userChoice:
                        found = True
                        break

                if found == True:

                    print(fattura)

                    listAttr = list()

                    for attributo in dir(fattura):

                        if not attributo.startswith("__") and not attributo.startswith("_"):
                            listAttr.append(attributo)

                    userChoice = str(input(f"Cosa vuoi modificare della {fattura.numero}?\n {" \n ".join(listAttr)}\n"))

                    if userChoice in dir(fattura):

                        updatedAttr = input(f"Modifica l'attributo {userChoice}: ")

                        if userChoice == "data":
                            while True:
                                if checkDate(updatedAttr):
                                    break
                                updatedAttr = input("Inserisci una data corretta: ")

                        setattr(fattura, userChoice, updatedAttr)

                        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

                        print(fattura)

                    break

        case 5:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            print(f"Bilancio:\n Entrate: {calcEntrate(listFatture)}\n Uscite: {calcUscite(listFatture)}\n Saldo: {calcSaldo(listFatture)}\n")

        case 6:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            
            while True:

                userChoice = str(input("Vuoi mostrare la lista dei clienti o la lista dei fornitori? [clienti / fornitori] "))

                if userChoice == "clienti":
                    for cliente in listClienti:
                        print(cliente)
                    break

                elif userChoice == "fornitori":
                    for fornitore in listFornitori:
                        print(fornitore)
                    break

        case 7:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            print("Lista fatture:\n")
            for fattura in listFatture:
                print(fattura, end="\n", sep="\n")

        case 8:

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            with open(datiERP, "w", encoding="utf-8") as file:

                listClientiJSON = []
                listFornitoriJSON = []
                listFattureJSON = []

                for cliente in listClienti:
                    cFCliente = cliente.codiceFiscale
                    nomeCliente = cliente.nome
                    cognomeCliente = cliente.cognome
                    fedelta = cliente.fedelta

                    dataSheetClienti = {
                        "cF": cFCliente,
                        "nome": nomeCliente,
                        "cognome": cognomeCliente,
                        "fedelta'": fedelta
                    }
                    listClientiJSON.append(dataSheetClienti)
                
                for fornitore in listFornitori:
                    cFFornitore = fornitore.codiceFiscale
                    nomeFornitore = fornitore.nome
                    cognomeFornitore = fornitore.cognome
                    settoriFornitore = fornitore.settori
                    dataSheetFornitori = {
                        "cF": cFFornitore,
                        "nome": nomeFornitore,
                        "cognome": cognomeFornitore,
                        "settori": settoriFornitore
                    }
                    listFornitoriJSON.append(dataSheetFornitori)

                for fattura in listFatture:
                    numeroFattura = fattura.numero
                    dataFattura = fattura.data
                    importoFattura = fattura.importo
                    cFFattura = fattura.persona
                    dataSheetFattura = {
                        "numero": numeroFattura,
                        "data": dataFattura,
                        "importo": importoFattura,
                        "cFPersona": cFFattura
                    }
                    listFattureJSON.append(dataSheetFattura)
                
                dataBase = {
                    "clienti": listClientiJSON,
                    "fornitori": listFornitoriJSON,
                    "fatture": listFattureJSON
                }
                
                json.dump(dataBase, file, indent=4)

                print("Salvataggio completato!")
