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
        return self.distanzaDalCentro

    def distanzaDalPunto(self, altroPunto2D):
        if isinstance(altroPunto2D, Punto2D):
            distanzaDalPunto = math.sqrt((self.x - altroPunto2D.x)**2 + (self.y - altroPunto2D.y)**2)
        else:
            raise Exception
    
    def __str__(self):
        stringa = "Oggetto Punto2D\n"
        stringa += f"coordinata x ->{self.x}"
        stringa += f"coordinata y ->{self.y}"
        stringa += f"coordinata x ->{self.distanzaDalCentro()}"
        return stringa
    
if __name__ == "__main__":
    coordinataX1 = int(input("insert the cord for x on punto2d 1: "))
    coordinataY1 = int(input("insert the cord for y on punto2d 2: "))
    coordinataX2 = int(input("insert the cord for x on punto2d 3: "))
    coordinataY2 = int(input("insert the cord for y on punto2d 4: "))

    punto1 = Punto2D(coordinataX1, coordinataY1)
    punto2 = Punto2D(coordinataX2, coordinataY2)

    print (punto1)
    print (punto2)

    print(f"la distanza tra il punto2d 1 e il punto2d 2 e: {punto1.distanzaDalPunto(punto2)}")
