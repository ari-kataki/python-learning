import os
import json
from datetime import datetime

from parte1.utente import Utente
from parte1.libro import Libro
from parte2.prestito import Prestito

fileJSON = "datiBiblioteca.json"
fileLog = "log.txt"

dataBase = {
    "utenti": [],
    "libri": [],
    "prestiti": []
}

# -------------------------
# FUNZIONI DI SUPPORTO
# -------------------------

def scriviLog(tipoOperazione, dati):
    try:
        with open(fileLog, "a") as file:
            ora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"[{ora}] {tipoOperazione} - {dati}\n")
    except:
        print("Attenzione: impossibile scrivere sul file di log.")

def trovaTrouvaUtente(matricola):
    for utente in dataBase["utenti"]:
        if utente.matricola == matricola:
            return utente
    return None

def trovaLibro(codice):
    for libro in dataBase["libri"]:
        if libro.codice == codice:
            return libro
    return None

def matricolaEsiste(matricola):
    return trovaTrouvaUtente(matricola) != None

def codiceLibroEsiste(codice):
    return trovaLibro(codice) != None

# -------------------------
# FUNZIONI DEL MENU
# -------------------------

def aggiungiUtente():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente: ")

    if matricolaEsiste(matricola):
        print("Errore: esiste gia' un utente con questa matricola!")
        os.system("pause")
        return

    nome = input("Inserisci il NOME dell'utente: ")
    cognome = input("Inserisci il COGNOME dell'utente: ")
    utente = Utente(matricola, nome, cognome)
    dataBase["utenti"].append(utente)
    print("Utente aggiunto con successo!")
    scriviLog("AGGIUNTA UTENTE", f"Matricola: {matricola}, Nome: {nome} {cognome}")
    os.system("pause")

def aggiungiLibro():
    os.system("cls")
    codice = input("Inserisci il CODICE del libro: ")

    if codiceLibroEsiste(codice):
        print("Errore: esiste gia' un libro con questo codice!")
        os.system("pause")
        return

    titolo = input("Inserisci il TITOLO del libro: ")
    autore = input("Inserisci l'AUTORE del libro: ")
    genere = input("Inserisci il GENERE del libro: ")
    annoPubblicazione = input("Inserisci l'ANNO DI PUBBLICAZIONE del libro: ")
    libro = Libro(codice, titolo, autore, genere, annoPubblicazione)
    dataBase["libri"].append(libro)
    print("Libro aggiunto con successo!")
    scriviLog("AGGIUNTA LIBRO", f"Codice: {codice}, Titolo: {titolo}, Autore: {autore}")
    os.system("pause")

def registraPrestito():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente: ")
    oggettoUtente = trovaTrouvaUtente(matricola)

    if oggettoUtente == None:
        print("Errore: utente non trovato!")
        os.system("pause")
        return

    if oggettoUtente.numeroLibriInPrestito() >= 3:
        print("Errore: l'utente ha gia' raggiunto il limite massimo di 3 libri in prestito!")
        os.system("pause")
        return

    codice = input("Inserisci il CODICE del libro da prendere in prestito: ")
    oggettoLibro = trovaLibro(codice)

    if oggettoLibro == None:
        print("Errore: libro non trovato!")
        os.system("pause")
        return

    try:
        prestito = Prestito(oggettoUtente, oggettoLibro)
        dataBase["prestiti"].append(prestito)
        print("Prestito registrato con successo!")
        scriviLog("REGISTRAZIONE PRESTITO", f"Matricola: {matricola}, Codice libro: {codice}, Titolo: {oggettoLibro.titolo}")
    except Exception as e:
        print(f"Errore: {e}")

    os.system("pause")

def restituisciLibro():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente che restituisce il libro: ")
    oggettoUtente = trovaTrouvaUtente(matricola)

    if oggettoUtente == None:
        print("Errore: utente non trovato!")
        os.system("pause")
        return

    codice = input("Inserisci il CODICE del libro da restituire: ")
    oggettoLibro = trovaLibro(codice)

    if oggettoLibro == None:
        print("Errore: libro non trovato!")
        os.system("pause")
        return

    oggettoPrestitoAttivo = None
    for prestito in dataBase["prestiti"]:
        if prestito.utente == oggettoUtente and prestito.libro == oggettoLibro and prestito.isAttivo():
            oggettoPrestitoAttivo = prestito
            break

    if oggettoPrestitoAttivo == None:
        print("Errore: non risulta alcun prestito attivo per questo utente e questo libro!")
        os.system("pause")
        return

    try:
        oggettoPrestitoAttivo.restituisciLibro()
        print("Libro restituito con successo!")
        scriviLog("RESTITUZIONE LIBRO", f"Matricola: {matricola}, Codice libro: {codice}, Titolo: {oggettoLibro.titolo}")
    except Exception as e:
        print(f"Errore: {e}")

    os.system("pause")

def modificaUtente():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente da modificare: ")
    oggettoUtente = trovaTrouvaUtente(matricola)

    if oggettoUtente == None:
        print("Errore: utente non trovato!")
        os.system("pause")
        return

    print("Utente trovato! Reinserisci i dati (lascia vuoto per non modificare):")
    nuovoNome = input(f"Inserisci il NOME [{oggettoUtente.nome}]: ")
    nuovoCognome = input(f"Inserisci il COGNOME [{oggettoUtente.cognome}]: ")

    if nuovoNome != "":
        oggettoUtente.nome = nuovoNome
    if nuovoCognome != "":
        oggettoUtente.cognome = nuovoCognome

    print("Dati utente aggiornati!")
    os.system("pause")

def modificaLibro():
    os.system("cls")
    codice = input("Inserisci il CODICE del libro da modificare: ")
    oggettoLibro = trovaLibro(codice)

    if oggettoLibro == None:
        print("Errore: libro non trovato!")
        os.system("pause")
        return

    print("Libro trovato! Reinserisci i dati (lascia vuoto per non modificare):")
    nuovoTitolo = input(f"Inserisci il TITOLO [{oggettoLibro.titolo}]: ")
    nuovoAutore = input(f"Inserisci l'AUTORE [{oggettoLibro.autore}]: ")
    nuovoGenere = input(f"Inserisci il GENERE [{oggettoLibro.genere}]: ")
    nuovoAnno = input(f"Inserisci l'ANNO DI PUBBLICAZIONE [{oggettoLibro.annoPubblicazione}]: ")

    if nuovoTitolo != "":
        oggettoLibro.titolo = nuovoTitolo
    if nuovoAutore != "":
        oggettoLibro.autore = nuovoAutore
    if nuovoGenere != "":
        oggettoLibro.genere = nuovoGenere
    if nuovoAnno != "":
        oggettoLibro.annoPubblicazione = nuovoAnno

    print("Dati libro aggiornati!")
    os.system("pause")

def stampaUtenti():
    os.system("cls")
    if len(dataBase["utenti"]) == 0:
        print("Nessun utente registrato.")
    else:
        for utente in dataBase["utenti"]:
            print(utente)
    os.system("pause")

def stampaLibri():
    os.system("cls")
    if len(dataBase["libri"]) == 0:
        print("Nessun libro registrato.")
    else:
        for libro in dataBase["libri"]:
            print(libro)
    os.system("pause")

def stampaPrestitiAttivi():
    os.system("cls")
    trovati = False
    for prestito in dataBase["prestiti"]:
        if prestito.isAttivo():
            print(prestito)
            trovati = True
    if not trovati:
        print("Nessun prestito attivo.")
    os.system("pause")

def cercaLibriPerGenere():
    os.system("cls")
    genere = input("Inserisci il GENERE da cercare: ")
    trovati = False
    for libro in dataBase["libri"]:
        if libro.genere.lower() == genere.lower():
            print(libro)
            trovati = True
    if not trovati:
        print(f"Nessun libro trovato per il genere '{genere}'.")
    os.system("pause")

def mostraLibriPerUtente():
    os.system("cls")
    if len(dataBase["utenti"]) == 0:
        print("Nessun utente registrato.")
    else:
        for utente in dataBase["utenti"]:
            print(f"Utente {utente.matricola} - {utente.nome} {utente.cognome}: {utente.numeroLibriInPrestito()} libro/i in prestito")
    os.system("pause")

def mostraLibriDisponibili():
    os.system("cls")
    trovati = False
    for libro in dataBase["libri"]:
        if libro.isDisponibile():
            print(libro)
            trovati = True
    if not trovati:
        print("Nessun libro disponibile al momento.")
    os.system("pause")

# -------------------------
# FUNZIONI JSON
# -------------------------

def salvaDati():
    data = {
        "utenti": [],
        "libri": [],
        "prestiti": []
    }

    for utente in dataBase["utenti"]:
        data["utenti"].append({
            "matricola": utente.matricola,
            "nome": utente.nome,
            "cognome": utente.cognome
        })

    for libro in dataBase["libri"]:
        data["libri"].append({
            "codice": libro.codice,
            "titolo": libro.titolo,
            "autore": libro.autore,
            "genere": libro.genere,
            "annoPubblicazione": libro.annoPubblicazione,
            "stato": libro.stato
        })

    for prestito in dataBase["prestiti"]:
        data["prestiti"].append({
            "matricola": prestito.utente.matricola,
            "codiceLibro": prestito.libro.codice,
            "stato": prestito.stato
        })

    try:
        with open(fileJSON, "w") as file:
            json.dump(data, file, indent=4)
        print("Dati salvati con successo!")
    except:
        print("Errore nel salvataggio del file!")

    os.system("pause")
    os.system("cls")

def caricaDati():
    try:
        with open(fileJSON, "r") as file:
            data = json.load(file)

        dataBase["utenti"].clear()
        for u in data["utenti"]:
            oggettoUtente = Utente(u["matricola"], u["nome"], u["cognome"])
            dataBase["utenti"].append(oggettoUtente)

        dataBase["libri"].clear()
        for l in data["libri"]:
            oggettoLibro = Libro(l["codice"], l["titolo"], l["autore"], l["genere"], l["annoPubblicazione"])
            if l["stato"] == "in prestito":
                oggettoLibro.prendiInPrestito()
            dataBase["libri"].append(oggettoLibro)

        dataBase["prestiti"].clear()
        for p in data["prestiti"]:
            oggettoUtente = trovaTrouvaUtente(p["matricola"])
            oggettoLibro = trovaLibro(p["codiceLibro"])
            if oggettoUtente != None and oggettoLibro != None:
                prestito = Prestito.__new__(Prestito)
                prestito._Prestito__utente = oggettoUtente
                prestito._Prestito__libro = oggettoLibro
                prestito._Prestito__stato = p["stato"]
                if p["stato"] == "attivo":
                    oggettoUtente.aggiungiLibro(oggettoLibro)
                dataBase["prestiti"].append(prestito)

        print("Dati caricati con successo!")
        os.system("pause")
        os.system("cls")
    except:
        print("Errore nel caricamento del file!")
        os.system("pause")
        os.system("cls")

# -------------------------
# PROGRAMMA PRINCIPALE
# -------------------------

def main():
    if not os.path.exists(fileJSON) or os.stat(fileJSON).st_size == 0:
        print(f"Il file {fileJSON} non esiste o e' vuoto.")
        scelta = input("Vuoi inserire i dati manualmente? (Si/No): ")

        if scelta == "Si":
            os.system("cls")
            while True:
                print("Cosa vuoi aggiungere? (U = Utente, L = Libro, E = Esci)")
                comando = input("Scelta: ")

                if comando == "U":
                    aggiungiUtente()
                elif comando == "L":
                    aggiungiLibro()
                elif comando == "E":
                    break
                else:
                    print("Comando non riconosciuto!")
                    os.system("pause")
                    os.system("cls")
    else:
        caricaDati()

    while True:
        print("========== MENU BIBLIOTECA ==========")
        print("1.  Aggiungere un nuovo utente")
        print("2.  Aggiungere un nuovo libro")
        print("3.  Registrare un nuovo prestito")
        print("4.  Restituire un libro")
        print("5.  Modificare i dati di un utente (FACOLTATIVO)")
        print("6.  Modificare i dati di un libro (FACOLTATIVO)")
        print("7.  Stampare tutti gli utenti (FACOLTATIVO)")
        print("8.  Stampare tutti i libri")
        print("9.  Stampare tutti i prestiti attivi")
        print("10. Cercare i libri per genere")
        print("11. Mostrare quanti libri ha in prestito ogni utente")
        print("12. Mostrare tutti i libri disponibili")
        print("13. Salvare i dati aggiornati")
        print("14. Uscire dal programma")
        print("=====================================")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            aggiungiUtente()
        elif scelta == "2":
            aggiungiLibro()
        elif scelta == "3":
            registraPrestito()
        elif scelta == "4":
            restituisciLibro()
        elif scelta == "5":
            modificaUtente()
        elif scelta == "6":
            modificaLibro()
        elif scelta == "7":
            stampaUtenti()
        elif scelta == "8":
            stampaLibri()
        elif scelta == "9":
            stampaPrestitiAttivi()
        elif scelta == "10":
            cercaLibriPerGenere()
        elif scelta == "11":
            mostraLibriPerUtente()
        elif scelta == "12":
            mostraLibriDisponibili()
        elif scelta == "13":
            salvaDati()
        elif scelta == "14":
            print("Programma terminato.")
            break
        else:
            print("Scelta non valida, riprova.")
            os.system("pause")
            os.system("cls")

if __name__ == "__main__":
    main()
