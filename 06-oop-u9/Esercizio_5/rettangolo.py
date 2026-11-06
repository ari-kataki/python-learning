class Rettangolo:
    def __init__(self, base, altezza):
        self.__base = abs(base)
        self.__altezza = abs(altezza)

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, nuovaBase):
        self.__base = abs(nuovaBase)
    
    @property
    def altezza(self):
        return self.__altezza
    
    @altezza.setter
    def altezza(self, nuovaAltezza):
        self.__altezza = abs(nuovaAltezza)

    @property
    def perimetro(self):
        return (self.__base + self.__altezza)*2
    
    @property
    def area(self):
        return self.__base * self.__altezza

    def __str__(self):
        stringa = "Oggetto Rettangolo\n"
        stringa += f"Base->{self.__base}\n"
        stringa += f"Altezza->{self.__altezza}\n"
        stringa += f"Perimetro->{self.perimetro}\n"
        stringa += f"Area->{self.area}\n"
        return stringa

if __name__ == "__main__":
    base = 5
    altezza = 6
    rettangolo = Rettangolo(base, altezza)
    print(rettangolo)