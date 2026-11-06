from parte1.persona import Persona

class Allenatore(Persona):
    
    __categoriaList = ["pulcini", "esordienti", "allievi", "juniores"]
    
    def __init__(self, cF, nome, cognome, eta, categoriaAllenatore):
        super().__init__(cF, nome, cognome, eta)
        self.__categoriaAllenatore = categoriaAllenatore

    @property
    def categoriaList(self):
        return self.__categoriaList

    @property
    def categoriaAllenatore(self):
        return self.__categoriaAllenatore
    
    @categoriaAllenatore.setter
    def categoriaAllenatore(self, nuovaCategoriaAllenatore):
        self.__categoriaAllenatore = nuovaCategoriaAllenatore
    
    def __str__(self):
        return f"****************\n" + f"ALLENATORE:\n" + super().__str__() + f"Categoria: {self.__categoriaAllenatore}\n" + f"****************\n"