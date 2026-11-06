import random
def ottieniVincitore(moneta, dado1, dado2):
    """Esercizio 4"""
    if moneta != "t" and moneta != "c":
        raise Exception
    elif not(1 <= dado1 <= 6) and not (1 <= dado2 <= 6):
        raise Exception
    else:
        if moneta == "t":
            if dado1 > dado2:
                print("Il vincitore e player 1")
            elif dado1 < dado2:
                print("Il vincitore e player 2")
            else:
                print("Draw")
        if moneta == "c":
            if dado1 < dado2:
                print("Winner is player 1")
                risultato = 1
            elif dado1 > dado2:
                print("Winner is player 2")
                risultato = 2
            else:
                print("Draw")  

        return risultato

if __name__ == "__name__":
    player1 = input("Enter player 1 name")
    player2 = input("Enter player 2 name")


    moneta = random.choice(["t","c"])

    dadoG1 = random.randint(1,6)
    dadoG2 = random.randint(1,6)

    print(f"The coin tossed is {moneta}")
    print(f"The dado tossed is {dadoG1}")
    print(f"The dado tossed is {dadoG2}")

    risultatoPartita = ottieniVincitore(moneta, dadoG1, dadoG2)

    if risultatoPartita == 1:
        print(f"Winner is {player1}")
        
    elif risultatoPartita == 2:
        print(f"Winner is {player2}")
    else:
        print("Draw")