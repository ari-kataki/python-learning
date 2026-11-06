import math

class TriangoloRettangolo:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        self.ipotenusa = self.calcolaIpotenusa()

    def calcolaIpotenusa(self):
        return math.sqrt((self.cateto1)**2 + (self.cateto2)**2)
    
    def calcolaPerimetro(self):
        return self.cateto1 + self.cateto2 + self.ipotenusa
    
    def calcolaArea(self):
        return (self.cateto1 * self.cateto2) / 2
    
    def __str__(self):
        stringa = "Oggetto Triangolo Rettangolo\n"
        stringa += f"Cateto1->{self.cateto1}\n"
        stringa += f"Cateto2->{self.cateto2}\n"
        stringa += f"Ipotenusa->{self.ipotenusa}\n"
        stringa += f"Perimetro->{self.calcolaPerimetro()}\n"
        stringa += f"Area->{self.calcolaArea()}\n"
        return stringa
    
if __name__ == "__main__":
    triangolo = TriangoloRettangolo(4, 3)
    print(triangolo)
