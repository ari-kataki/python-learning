import math

class Punto2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, nuovaX):
        self.__x = nuovaX

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, nuovaY):
        self.__y = nuovaY

    def distanzaDalCentro(self):
        distanzaDalCentro = math.sqrt(self.x**2 + self.y**2)
        return distanzaDalCentro

    def distanzaDalPunto(self, altroPunto2D):
        if isinstance(altroPunto2D, Punto2D):
            distanzaDalPunto = math.sqrt((self.x - altroPunto2D.x)**2 + (self.y - altroPunto2D.y)**2)
            return distanzaDalPunto
        else:
            raise Exception

    def __str__(self):
        stringa = "Oggetto Punto2D\n"
        stringa += f"Coordinata x->{self.x}\n"
        stringa += f"Coordinata y->{self.y}\n"
        stringa += f"Distanza dal centro->{self.distanzaDalCentro()}\n"
        return stringa
    
if __name__ == "__main__":
    coordinataX1 = int(input("Inserisci la coordinata x dell'oggetto Punto2D 1: "))
    coordinataY1 = int(input("Inserisci la coordinata y dell'oggetto Punto2D 1: "))
    coordinataX2 = int(input("Inserisci la coordinata x dell'oggetto Punto2D 2: "))
    coordinataY2 = int(input("Inserisci la coordinata y dell'oggetto Punto2D 2: "))

    punto1 = Punto2D(coordinataX1, coordinataY1)
    punto2 = Punto2D(coordinataX2, coordinataY2)

    print(punto1)
    print(punto2)

    print(f"La distanza tra il Punto2D 1 e il Punto2D 2 è: {punto1.distanzaDalPunto(punto2)}")