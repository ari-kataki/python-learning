import subprocess
import os

def editAttr(inputList, choice):

    for object in inputList:
        print(object, end="\n")

    while True:

        userChoice = str(input(f"Scegliere il codice fiscale [{choice}] tra quelli mostrati: "))

        found = False
        for object in inputList:
            if object.cF == userChoice:
                found = True
                break

        if found == True:

            print(object)

            listAttr = list()

            for attributo in dir(object):

                if not attributo.startswith("__") and not attributo.startswith("_"):
                    if attributo != "cF" and attributo != "categoria" and attributo != "ruoloList" and attributo != "assegnaCategoria":
                        listAttr.append(attributo)

            userChoice = str(input(f"Cosa vuoi modificare di {object.nome} [{choice}]?\n- {" \n- ".join(listAttr)}\n"))

            if userChoice in listAttr:

                if userChoice == "ruolo":
                    for ruolo in object.ruoloList:
                        print(ruolo, end="\n")
                    
                    while True:
                        updatedAttr = str(input(f"Modifica l'attributo {userChoice}: "))
                        if updatedAttr in object.ruoloList:
                            break
                else:
                    updatedAttr = str(input(f"Modifica l'attributo {userChoice}: "))

                setattr(object, userChoice, updatedAttr)

                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

                print(object)
            break
        
    return object

def stampaClassifica(lista):
    squadreOrdinate = sorted(lista, key=lambda s: s.vittorie * 3 + s.pareggi, reverse=True)
    nPartiteOrdinate = sorted(lista, key=lambda s: s.vittorie + s.sconfitte + s.pareggi, reverse=True)
    print("Classifica:")
    for squadra in squadreOrdinate:
        punti = squadra.vittorie * 3 + squadra.pareggi
        print(f" - {squadra.nome} : {punti} punti")
    print("\nPartite Giocate: ")
    for squadra in nPartiteOrdinate:
        nPartite = squadra.vittorie + squadra.sconfitte + squadra.pareggi
        print(f" - {squadra.nome} : {nPartite} partite giocate")
    