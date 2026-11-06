from parte2.fattura import Fattura

def calcEntrate(listFatture):
    ricavo = float()
    for fattura in listFatture:
        if fattura.tipo == "vendita":
            ricavo += fattura.importo
    return ricavo

def calcUscite(listaFatture):
    costi = float()
    for fattura in listaFatture:
        if fattura.tipo == "acquisto":
            costi += fattura.importo
    return costi

def calcSaldo(listaFatture):
    entrate = calcEntrate(listaFatture)
    uscite = calcUscite(listaFatture)
    saldo = entrate - uscite
    return saldo