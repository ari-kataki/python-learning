def contaVocali(filename):
    """Esercizio 4"""
    try:
        contatoreVocali = 0
        with open(filename, "r", encoding="utf-8") as file:
            stringaFile = file.read().lower()

            contatoreVocali += stringaFile.count("a")
            contatoreVocali += stringaFile.count("e")
            contatoreVocali += stringaFile.count("i")
            contatoreVocali += stringaFile.count("o")
            contatoreVocali += stringaFile.count("u")
            contatoreVocali += stringaFile.count("y")

        return contatoreVocali
    except:
        print("Errore nella gestione del file")

print(f"Il numero di vocali all'interno del file è: {contaVocali("Esercizio_3/elenco.txt")}")