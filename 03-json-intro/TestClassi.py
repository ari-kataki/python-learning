class Test:
    def __init__(self, a, b):
        print("ogetto eseguito!")
        self.primoAttributo = a
        self.secondoAttributo = b
        
    def __str__(self):
        string = "Metodo eseguito!"
        string += f"\nprimoAttributo ={self.primoAttributo}; secondoAttributo = {self.secondoAttributo}!"
        return string 
  
    def method(self):
        print(f"Metodo eseguito con l'oggetto {self}!")
        print(f"primoAttributo: {self.primoAttributo}; secondoAttributo: {self.secondoAttributo}!")

oggettoTest = Test(10, 20)
print(oggettoTest)
print(oggettoTest.method)
print(Test.method)
print(oggettoTest.primoAttributo)
print(oggettoTest.secondoAttributo)
oggettoTest.method()
Test.method(oggettoTest)

print()

oggettoTest = Test(10,20)
print(oggettoTest)
print(oggettoTest.method)
print(Test.method)
oggettoTest.method()
Test.method(oggettoTest)