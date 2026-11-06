try:
    file = open("Esercizio_3/elenco.txt", "r", encoding="utf-8")

    listaNomi = list()
    for riga in file:
        listaNomi.append(riga.upper())
    file.close()

    listaNomi.sort()

    file = open("Esercizio_3/elenco.txt", "w", encoding="utf-8")

    for nome in listaNomi:
        file.write(f"{nome}")

    file.close
except:
    print("Errore nell'apertura del file!")