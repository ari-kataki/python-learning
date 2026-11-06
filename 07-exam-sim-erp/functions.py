from datetime import datetime
import subprocess
import os

def checkDate(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def editAttr(inputList, choice):
    for object in inputList:
        print(object, end="\n")

    while True:

        initialUserChoice = str(input(f"Scegliere il codice fiscale del {choice} tra quelli mostrati: "))
        found = False
        for object in inputList:
            if object.codiceFiscale == initialUserChoice:
                found = True
                break

        if found == True:

            print(object)

            listAttr = list()

            for attributo in dir(object):

                if not attributo.startswith("__") and not attributo.startswith("_"):
                    if attributo != "codiceFiscale" and attributo != "livelloFedelta":
                        listAttr.append(attributo)

            userChoice = str(input(f"Cosa vuoi modificare del {choice} {object.nome}?\n- {" \n- ".join(listAttr)}\n"))

            if userChoice in dir(object):
                
                if userChoice == "settori":

                    listSettoriObj = object.settori
                    while True:

                        userAction = str(input("Vuoi aggiungere o rimuovere settori? [aggiungere / rimuovere] "))

                        if userAction == "aggiungere":
                            settoriAmount = int(input(f"Quanti settori vuoi aggiungere al fornitore {object.nome}? "))
                            for _ in range(settoriAmount):
                                userFornSettore = str(input("Aggiungi il settore: "))
                                listSettoriObj.append(userFornSettore)
                            updatedAttr = listSettoriObj
                            break
                        elif userAction == "rimuovere":
                            for settore in listSettoriObj:
                                print(settore, end="\n")
                            while True:
                                settoriAmount = int(input(f"Quanti settori vuoi rimuovere dal fornitore {object.nome}? "))
                                for _ in range(settoriAmount):
                                    while True:
                                        userFornSettore = str(input("Rimuovi il settore: "))
                                        if userFornSettore in listSettoriObj:
                                            listSettoriObj.remove(userFornSettore)
                                            break
                                updatedAttr = listSettoriObj
                                break
                            break
                else:
                    updatedAttr = str(input(f"Modifica l'attributo {userChoice}: "))

                    if userChoice == "data":
                        while True:
                            if checkDate(updatedAttr):
                                break
                            updatedAttr = input("Inserisci una data corretta: ")

                setattr(object, userChoice, updatedAttr)

                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

                print(object)
            break
        
    return object
    
if __name__ == "__main__":
    print(checkDate("20/10/2020"))