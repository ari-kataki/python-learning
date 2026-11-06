if __name__ == "__main__":
    while(True):
        numeroUtente = int(input("Inserisci un numero intero positivo: "))

        if numeroUtente > 0:
            break

    file = open("Esercizio_1/numeri.txt", "w")

    for contatore in range(numeroUtente + 1):
        file.write(f"{contatore}\n")

    file.close()