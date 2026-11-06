class Squadra:
    # def __init__(self, nome, allenatoreCF, listaGiocatori, vittorie, sconfitte, pareggi, listaAllenatori):
    #     self.__nome = nome
    #     self.__allenatoreCF = allenatoreCF
    #     self.__listaGiocatori = listaGiocatori
    #     self.__listaAllenatori = listaAllenatori
    #     self.__categoria = self.assegnaCategoria(self.__listaAllenatori)
    #     self.__vittorie = vittorie
    #     self.__sconfitte = sconfitte
    #     self.__pareggi = pareggi
    
    def __init__(self, nome, allenatoreCF, listaGiocatori, vittorie, sconfitte, pareggi):
        self.__nome = nome
        self.__allenatoreCF = allenatoreCF
        self.__listaGiocatori = listaGiocatori
        self.__vittorie = vittorie
        self.__sconfitte = sconfitte
        self.__pareggi = pareggi
        self.__categoria = ""
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nuovoNome):
        self.__nome = nuovoNome

    @property
    def allenatoreCF(self):
        return self.__allenatoreCF
    
    @allenatoreCF.setter
    def allenatoreCF(self, nuovoAllenatoreCF):
        self.__allenatoreCF = nuovoAllenatoreCF

    # @property
    # def listaAllenatori(self):
    #     return self.__listaAllenatori
    
    @property
    def listaGiocatori(self):
        return self.__listaGiocatori
    
    @listaGiocatori.setter
    def listaGiocatori(self, nuovaListaGiocatori):
        self.__listaGiocatori = nuovaListaGiocatori

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nuovaCategoria):
        self.__categoria = nuovaCategoria
    
    @property
    def vittorie(self):
        return self.__vittorie
    
    @vittorie.setter
    def vittorie(self, nuovoVittorie):
        self.__vittorie = nuovoVittorie
    
    @property
    def sconfitte(self):
        return self.__sconfitte
    
    @sconfitte.setter
    def sconfitte(self, nuovoSconfitte):
        self.__sconfitte = nuovoSconfitte
    
    @property
    def pareggi(self):
        return self.__pareggi
    
    @pareggi.setter
    def pareggi(self, nuovoPareggi):
        self.__pareggi = nuovoPareggi

    def __str__(self):
        return (f"****************\n"
                f"SQUADRA:\n"
                f" Nome: {self.__nome}\n"
                f" Allenatore: {self.__allenatoreCF}\n"
                f" Lista gioctori: {self.__listaGiocatori}\n"
                f" Vittorie: {self.__vittorie}\n"
                f" Sconfitte: {self.__sconfitte}\n"
                f" Pareggi: {self.__pareggi}\n"
                f" Categoria: {self.__categoria}\n"
                )
    
    def assegnaCategoria(self, allenatori):
        for allenatore in allenatori:
            if allenatore.cF == self.__allenatoreCF:
                self.__categoria = allenatore.categoriaAllenatore

    
