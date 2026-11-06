import os
import json
from datetime import datetime   # per il log

from parte1.utente import Utente
from parte1.libro import Libro
from parte2.prestito import Prestito, valoriStatoPrestito

# VARIABILI DI MODULO
fileJSON = "datiBiblioteca.json"
fileLog = "log.txt"

# DATABASE - dizionario globale con liste di oggetti
dataBase = {
    "utenti": [],
    "libri": [],
    "prestiti": []
}

# FUNZIONI DI SUPPORTO (helper)

# cerca un oggetto nella lista per un attributo univoco
def trovaUtente(matricola):
    oggettoUtente = None
    for utente in dataBase["utenti"]:
        if utente.matricola == matricola:
            oggettoUtente = utente
    return oggettoUtente

def trovaLibro(codice):
    oggettoLibro = None
    for libro in dataBase["libri"]:
        if libro.codice == codice:
            oggettoLibro = libro
    return oggettoLibro

# FUNZIONE DI LOG
# scrive una riga nel file di log

def scriviLog(tipoOperazione, dati):
    try:
        with open(fileLog, "a") as file:
            ora = datetime.now()
            file.write(f"{ora} - {tipoOperazione} - {dati}\n")
    except:
        print("Attenzione: impossibile scrivere sul file di log.")

# FUNZIONI DEL MENU - AGGIUNTA OGGETTI
# aggiunge un nuovo utente al dataBase
def aggiungiUtente():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente: ")

    if trovaUtente(matricola) != None:
        print("Errore: esiste gia' un utente con questa matricola!")
    else:
        nome = input("Inserisci il NOME dell'utente: ")
        cognome = input("Inserisci il COGNOME dell'utente: ")
        utente = Utente(matricola, nome, cognome)
        dataBase["utenti"].append(utente)
        print("Utente aggiunto con successo!")
        scriviLog("AGGIUNTA UTENTE", f"Matricola: {matricola}, Nome: {nome} {cognome}")

    os.system("pause")
    os.system("cls")

# aggiunge un nuovo libro al dataBase

def aggiungiLibro():
    os.system("cls")
    codice = input("Inserisci il CODICE del libro: ")

    if trovaLibro(codice) != None:
        print("Errore: esiste gia' un libro con questo codice!")
    else:
        titolo = input("Inserisci il TITOLO del libro: ")
        autore = input("Inserisci l'AUTORE del libro: ")
        genere = input("Inserisci il GENERE del libro: ")
        annoPubblicazione = input("Inserisci l'ANNO DI PUBBLICAZIONE del libro: ")
        libro = Libro(codice, titolo, autore, genere, annoPubblicazione)
        dataBase["libri"].append(libro)
        print("Libro aggiunto con successo!")
        scriviLog("AGGIUNTA LIBRO", f"Codice: {codice}, Titolo: {titolo}, Autore: {autore}")

    os.system("pause")
    os.system("cls")

# FUNZIONI DEL MENU - LOGICA DI PRESTITO

# registra un nuovo prestito

# Ogni else stampa il messaggio di errore corrispondente.
def registraPrestito():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente: ")
    oggettoUtente = trovaUtente(matricola)

    if oggettoUtente != None:
        if oggettoUtente.numeroLibriInPrestito() < 3:
            codice = input("Inserisci il CODICE del libro da prendere in prestito: ")
            oggettoLibro = trovaLibro(codice)

            if oggettoLibro != None:
                if oggettoLibro.isDisponibile():
                    prestito = Prestito(oggettoUtente, oggettoLibro)
                    dataBase["prestiti"].append(prestito)
                    print("Prestito registrato con successo!")
                    scriviLog("REGISTRAZIONE PRESTITO", f"Matricola: {matricola}, Codice libro: {codice}")
                else:
                    print("Errore: il libro non e' disponibile!")
            else:
                print("Errore: libro non trovato!")
        else:
            print("Errore: l'utente ha gia' raggiunto il limite massimo di 3 libri in prestito!")
    else:
        print("Errore: utente non trovato!")

    os.system("pause")
    os.system("cls")

# restituisce un libro
def restituisciLibro():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente che restituisce il libro: ")
    oggettoUtente = trovaUtente(matricola)

    if oggettoUtente != None:
        codice = input("Inserisci il CODICE del libro da restituire: ")
        oggettoLibro = trovaLibro(codice)

        if oggettoLibro != None:
            # CERCA IL PRESTITO ATTIVO corrispondente
            oggettoPrestitoAttivo = None
            for prestito in dataBase["prestiti"]:
                if prestito.utente == oggettoUtente and prestito.libro == oggettoLibro and prestito.isAttivo():
                    oggettoPrestitoAttivo = prestito

            if oggettoPrestitoAttivo != None:
                oggettoPrestitoAttivo.restituisciLibro()
                print("Libro restituito con successo!")
                scriviLog("RESTITUZIONE LIBRO", f"Matricola: {matricola}, Codice libro: {codice}")
            else:
                print("Errore: nessun prestito attivo trovato per questo utente e questo libro!")
        else:
            print("Errore: libro non trovato!")
    else:
        print("Errore: utente non trovato!")

    os.system("pause")
    os.system("cls")

# FUNZIONI DEL MENU - MODIFICA
# modifica i dati di un utente
def modificaUtente():
    os.system("cls")
    matricola = input("Inserisci la MATRICOLA dell'utente da modificare: ")
    oggettoUtente = trovaUtente(matricola)

    if oggettoUtente != None:
        print("Utente trovato! Reinserisci i dati dell'utente:")
        oggettoUtente.nome = input("Inserisci il NOME dell'utente: ")
        oggettoUtente.cognome = input("Inserisci il COGNOME dell'utente: ")
        print("Dati utente aggiornati!")
    else:
        print("Errore: utente non trovato!")

    os.system("pause")
    os.system("cls")

# modifica i dati di un libro
def modificaLibro():
    os.system("cls")
    codice = input("Inserisci il CODICE del libro da modificare: ")
    oggettoLibro = trovaLibro(codice)

    if oggettoLibro != None:
        print("Libro trovato! Reinserisci i dati del libro:")
        oggettoLibro.titolo = input("Inserisci il TITOLO del libro: ")
        oggettoLibro.autore = input("Inserisci l'AUTORE del libro: ")
        oggettoLibro.genere = input("Inserisci il GENERE del libro: ")
        oggettoLibro.annoPubblicazione = input("Inserisci l'ANNO DI PUBBLICAZIONE del libro: ")
        print("Dati libro aggiornati!")
    else:
        print("Errore: libro non trovato!")

    os.system("pause")
    os.system("cls")

# FUNZIONI DEL MENU - STAMPA
# stampa tutti gli oggetti di una lista
def stampaUtenti():
    os.system("cls")
    for utente in dataBase["utenti"]:
        print(utente)
    os.system("pause")
    os.system("cls")

def stampaLibri():
    os.system("cls")
    for libro in dataBase["libri"]:
        print(libro)
    os.system("pause")
    os.system("cls")

# stampa solo gli oggetti con stato attivo
def stampaPrestitiAttivi():
    os.system("cls")
    listaPrestitiAttivi = list()

    for prestito in dataBase["prestiti"]:
        if prestito.isAttivo():
            listaPrestitiAttivi.append(prestito)

    if len(listaPrestitiAttivi) > 0:
        for prestito in listaPrestitiAttivi:
            print(prestito)
    else:
        print("Nessun prestito attivo.")

    os.system("pause")
    os.system("cls")

# FUNZIONI DEL MENU - RICERCA E FILTRAGGIO
# cerca oggetti per valore di un attributo
def cercaLibriPerGenere():
    os.system("cls")
    genere = input("Inserisci il GENERE da cercare: ")
    listaRisultati = list()

    for libro in dataBase["libri"]:
        if libro.genere == genere:
            listaRisultati.append(libro)

    if len(listaRisultati) > 0:
        for libro in listaRisultati:
            print(libro)
    else:
        print("Nessun libro trovato per il genere inserito.")

    os.system("pause")
    os.system("cls")

# mostra un conteggio per ogni oggetto della lista A
def mostraLibriPerUtente():
    os.system("cls")
    for utente in dataBase["utenti"]:
        print(f"Utente {utente.matricola} - {utente.nome} {utente.cognome}: {utente.numeroLibriInPrestito()} libro/i in prestito")
    os.system("pause")
    os.system("cls")

# mostra tutti gli oggetti con stato disponibile
def mostraLibriDisponibili():
    os.system("cls")
    listaDisponibili = list()

    for libro in dataBase["libri"]:
        if libro.isDisponibile():
            listaDisponibili.append(libro)

    if len(listaDisponibili) > 0:
        for libro in listaDisponibili:
            print(libro)
    else:
        print("Nessun libro disponibile al momento.")

    os.system("pause")
    os.system("cls")

# SALVATAGGIO E CARICAMENTO JSON
# salva il dataBase nel file JSON
def salvaDati():
    data = {
        "utenti": [],
        "libri": [],
        "prestiti": []
    }

    # Converti ogni oggetto Utente in un dizionario
    for utente in dataBase["utenti"]:
        data["utenti"].append({
            "matricola": utente.matricola,
            "nome": utente.nome,
            "cognome": utente.cognome
        })

    # Converti ogni oggetto Libro in un dizionario
    for libro in dataBase["libri"]:
        data["libri"].append({
            "codice": libro.codice,
            "titolo": libro.titolo,
            "autore": libro.autore,
            "genere": libro.genere,
            "annoPubblicazione": libro.annoPubblicazione,
            "stato": libro.stato
        })

    # Converti ogni oggetto Prestito in un dizionario
    # Salva solo gli attributi univoci degli oggetti collegati (matricola, codice)
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

# carica il dataBase dal file JSON
def caricaDati():
    try:
        with open(fileJSON, "r") as file:
            data = json.load(file)

        # Ricrea gli oggetti Utente
        dataBase["utenti"].clear()
        for u in data["utenti"]:
            oggettoUtente = Utente(u["matricola"], u["nome"], u["cognome"])
            dataBase["utenti"].append(oggettoUtente)

        # Ricrea gli oggetti Libro e ripristina lo stato se era in prestito
        dataBase["libri"].clear()
        for l in data["libri"]:
            oggettoLibro = Libro(l["codice"], l["titolo"], l["autore"], l["genere"], l["annoPubblicazione"])
            if l["stato"] == "in prestito":
                oggettoLibro.prendiInPrestito()     # ripristina lo stato del libro
            dataBase["libri"].append(oggettoLibro)

        # Ricrea gli oggetti Prestito usando statoIniziale per evitare logica doppia
        dataBase["prestiti"].clear()
        for p in data["prestiti"]:
            oggettoUtente = trovaUtente(p["matricola"])       # ritrova oggetto gia' caricato
            oggettoLibro = trovaLibro(p["codiceLibro"])       # ritrova oggetto gia' caricato

            if oggettoUtente != None and oggettoLibro != None:
                prestito = Prestito(oggettoUtente, oggettoLibro, p["stato"])  # modalita' caricamento
                if p["stato"] == valoriStatoPrestito[0]:
                    oggettoUtente.aggiungiLibro(oggettoLibro)  # ripristina lista utente
                dataBase["prestiti"].append(prestito)

        print("Dati caricati con successo!")
        os.system("pause")
        os.system("cls")
    except:
        print("Errore nel caricamento del file!")
        os.system("pause")
        os.system("cls")

# FUNZIONE MAIN - PUNTO DI INGRESSO
def main():
    # CONTROLLO FILE JSON ALL'AVVIO
    if not os.path.exists(fileJSON) or os.stat(fileJSON).st_size == 0:
        print(f"Il file {fileJSON} non esiste o e' vuoto.")
        scelta = input("Vuoi inserire i dati manualmente? (Si/No): ")

        if scelta == "Si":
            os.system("cls")
            # MINI-MENU DI INSERIMENTO INIZIALE
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
    # MENU PRINCIPALE INTERATTIVO
    # Ogni voce corrisponde a una funzione separata.
    # Il break avviene solo sull'opzione Esci.
    while True:
        print("Menu:")
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
        print("13. Salvare i dati aggiornati nel file")
        print("14. Uscire dal programma")

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
