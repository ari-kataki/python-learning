if __name__ == "__main__":
    try:
        file = open("Esercizio_1/numeri.txt", "r", encoding="utf-8")
        accumulatore = 0
        for riga in file:
            accumulatore += int(riga)

        print(f"La somma tutti i numeri presenti all'interno di numeri.txt è {accumulatore}")
        file.close()
    except FileNotFoundError:
        print("Errore nell'apertura del file")
    except ValueError:
        print(f"Errore nella conversione della riga {riga}")