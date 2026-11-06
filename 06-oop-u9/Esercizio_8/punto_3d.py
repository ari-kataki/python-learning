from punto_2d import Punto2D

import math

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        return self.__z
    
    @z.setter
    def z(self, nuovaZ):
        self.__z = nuovaZ

    def distanzaDalCentro(self):
        distanzaDalCentro = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return distanzaDalCentro

    def distanzaDalPunto(self, altroPunto3D):
        if isinstance(altroPunto3D, Punto3D):
            distanzaDalPunto = math.sqrt((self.x - altroPunto3D.x)**2 + (self.y - altroPunto3D.y)**2 + (self.__z - altroPunto3D.z)**2)
            return distanzaDalPunto
        else:
            raise Exception
        
    def __str__(self):
        stringa = "Oggetto Punto£D\n"
        stringa += f"Coordinata x->{self.x}\n"
        stringa += f"Coordinata y->{self.y}\n"
        stringa += f"Coordinata y->{self.__z}\n"
        stringa += f"Distanza dal centro->{self.distanzaDalCentro()}\n"
        return stringa
    
if __name__ == "__main__":
    coordinataX1 = int(input("Inserisci la coordinata x dell'oggetto Punto3D 1: "))
    coordinataY1 = int(input("Inserisci la coordinata y dell'oggetto Punto3D 1: "))
    coordinataZ1 = int(input("Inserisci la coordinata z dell'oggetto Punto3D 1: "))
    coordinataX2 = int(input("Inserisci la coordinata x dell'oggetto Punto3D 2: "))
    coordinataY2 = int(input("Inserisci la coordinata y dell'oggetto Punto3D 2: "))
    coordinataZ2 = int(input("Inserisci la coordinata z dell'oggetto Punto3D 2: "))

    punto1 = Punto3D(coordinataX1, coordinataY1, coordinataZ1)
    punto2 = Punto3D(coordinataX2, coordinataY2, coordinataZ2)

    print(punto1)
    print(punto2)

    print(f"La distanza tra il Punto3D 1 e il Punto3D 2 è: {punto1.distanzaDalPunto(punto2)}")