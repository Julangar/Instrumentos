import random
import abc
from abc import ABC, abstractmethod
class Instrumento(ABC):

    @abstractmethod
    #afinar instrumento
    def afinar(self):
        pass

    @abstractmethod
    #tocar instrumento
    def  tocar(self):
        pass

    @abstractmethod
    #tocar nota
    def tocar_nota(self,nota):
        pass

class Guitarra(Instrumento):

    def __init__(self):
        pass

    def afinar(self):
        return print("Afinando guitarra")

    def tocar(self):
        return print("Tocando guitarra")

    def tocar_nota(self, nota):
        return print("Tocando guitarra en ",nota)

class Bajo(Instrumento):

    def __init__(self):
        pass

    def afinar(self):
        return print("Afinando bajo")

    def tocar(self):
        return print("Tocando bajo")

    def tocar_nota(self, nota):
        return print("Tocando bajo en ",nota)

i = Instrumento
opc = random.randrange(3)
if(opc == 1):
    i = Guitarra
elif(opc == 2):
    i = Bajo

i.afinar("")
i.tocar("")
i.tocar_nota("","Do")
