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

class Violin (Instrumento):

    def __init__(self):
        pass

    def afinar(self):
        return print("Afinando violin...")

    def tocar(self):
        return print("Tocando violin...")

    def tocar_nota(self,nota):
        return print("Tocando violin en ",nota,"...")

class Persona():

    Name = ""
    Apellido = ""
    def Nombre(self,Name,Apellido):
        pass

class Musico (Persona):

    def _init_(self, Name, Apellido):
        self._nombre_ = Name
        self._apellido_ = Apellido
 
    def get_nombre(self):
        return self._nombre_

    def get_apellido(self):
        return self._apellido_

i = Instrumento
opc = random.randrange(3)
opc2 = random.randrange(7)
if(opc == 1):
    i = Guitarra
if(opc == 2):
    i = Bajo
if(opc == 3):
    i = Violin

i.afinar("")
i.tocar("")
if(opc2 == 1):
    i.tocar_nota("","Do")
if(opc2 == 2):
    i.tocar_nota("","Re")
if(opc2 == 3):
    i.tocar_nota("","Mi")
if(opc2 == 4):
    i.tocar_nota("","Fa")
if(opc2 == 5):
    i.tocar_nota("","Sol")
if(opc2 == 6):
    i.tocar_nota("","La")
if(opc2 == 7):
    i.tocar_nota("","Si")
