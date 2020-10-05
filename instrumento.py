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

class Persona(object):

    def __init__(self,nombre):
        self.nombre = nombre

    def presentar(self):
        print("Hola mi nombre es ",self.nombre)


class Musico (Persona):

    def tocar(self, i = Instrumento ):
        i.afinar
        i.tocar
        i.tocar_nota

class Banda:

    def __init__(self):
        self.musicos = []

    def agregar_musico(self, nombre, m = Musico ):
        self.musicos.append(m.nombre)
        return print(self.musicos)

    def generar_instrumento(self):
        i = Instrumento
        opc = random.randrange(3)
        if(opc == 1):
            i = Guitarra
        if(opc == 2):
            i = Bajo
        if(opc == 3):
            i = Violin
    
    def presentar_banda(self):
        m = Musico
        musicos = []
        for m in musicos:
            m.presentar()
            m.tocar(generar_instrumento())

           
b = Banda
b.agregar_musico("","Pepito")
b.agregar_musico("","Juan")
b.agregar_musico("","Mariana")


"""
opc2 = random.randrange(7)


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
"""