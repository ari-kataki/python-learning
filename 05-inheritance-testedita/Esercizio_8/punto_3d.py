from punto_2D import Punto2D

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
        return self.distanzaDalCentro

    def distanzaDalPunto(self, altroPunto3D):
        if isinstance(altroPunto3D, Punto3D):
            distanzaDalPunto = math.sqrt((self.x - altroPunto3D.x)**2 + (self.y - altroPunto3D.y)**2 + (self.z - altroPunto3D.z)**2)
            return distanzaDalPunto
        else:
            raise Exception
        
    def __str__(self):
        stringa = "Oggetto Punto3D\n"
        stringa += f"coordinata x ->{self.x}\n"
        stringa += f"coordinata y ->{self.y}\n"
        stringa += f"coordinata z ->{self.z}\n"
        stringa += f"distanza dal centro ->{self.distanzaDalCentro()}\n"
        return stringa

if __name__ == "__main__":
    coordinataX1 = int(input("insert the cord for x on punto3d 1: "))
    coordinataY1 = int(input("insert the cord for y on punto3d 2: "))
    coordinataZ1 = int(input("insert the cord for z on punto3d 3: "))
    coordinataX2 = int(input("insert the cord for x on punto3d 4: "))
    coordinataY2 = int(input("insert the cord for y on punto3d 5: "))
    coordinataZ2 = int(input("insert the cord for z on punto3d 6: "))

    punto1 = Punto3D(coordinataX1, coordinataY1, coordinataZ1)
    punto2 = Punto3D(coordinataX2, coordinataY2, coordinataZ2)

    print (punto1)
    print (punto2)

    print(f"la distanza tra il punto3d 1 e il punto3d 2 e: {punto1.distanzaDalPunto(punto2)}")