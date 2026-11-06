from parte1.persona import Persona

class Giocatore(Persona):

    __categoriaList = ["pulcini", "esordienti", "allievi", "juniores"]

    __ruoloList = ["portiere", "difensore", "centrocampista", "attaccante"]

    def __init__(self, cF, nome, cognome, eta, ruolo):
        super().__init__(cF, nome, cognome, eta)
        self.__ruolo = ruolo
        self.__categoria = self.assegnaCategoria(self.eta)

    @property
    def ruoloList(self):
        return self.__ruoloList
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def ruolo(self):
        return self.__ruolo

    @ruolo.setter
    def ruolo(self, nuovoRuolo):
        self.__ruolo = nuovoRuolo
    
    def __str__(self):
        return f"****************\n" + f"GIOCATORE:\n" + super().__str__() + f" Ruolo: {self.__ruolo}\n" + f" Categoria: {self.__categoria}\n" + f"****************\n"
    
    def assegnaCategoria(self, eta):

        if 5 <= eta <= 10:
            self.__categoria = self.__categoriaList[0]

        elif 11 <= eta <= 14:
            self.__categoria = self.__categoriaList[1]

        elif 15 <= eta <= 17:
            self.__categoria = self.__categoriaList[2]
            
        elif 18 <= eta <= 19:
            self.__categoria = self.__categoriaList[3]
        
        return self.__categoria

        