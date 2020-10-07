import random
import abc
from abc import ABC, abstractmethod

musicos = []
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

    def afinar(self):
        return print("Afinando guitarra")

    def tocar(self):
        return print("Tocando guitarra")

    def tocar_nota(self):

        opc2 = random.randrange(7)
        if(opc2 == 1):
            nota = "Do"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 2):
            nota = "Re"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 3):
            nota = "Mi"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 4):
            nota = "Fa"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 5):
            nota = "Sol"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 6):
            nota = "La"
            return print("Tocando guitarra en ",nota)
        elif(opc2 == 7):
            nota = "Si"
            return print("Tocando guitarra en ",nota)


class Violin(Instrumento):

    def afinar(self):
        return print("Afinando violin")

    def tocar(self):
        return print("Tocando violin")

    def tocar_nota(self):

        opc2 = random.randrange(7)
        if(opc2 == 1):
            nota = "Do"
            return print("Tocando violin en ",nota)
        elif(opc2 == 2):
            nota = "Re"
            return print("Tocando violin en ",nota)
        elif(opc2 == 3):
            nota = "Mi"
            return print("Tocando violin en ",nota)
        elif(opc2 == 4):
            nota = "Fa"
            return print("Tocando violin en ",nota)
        elif(opc2 == 5):
            nota = "Sol"
            return print("Tocando violin en ",nota)
        elif(opc2 == 6):
            nota = "La"
            return print("Tocando violin en ",nota)
        elif(opc2 == 7):
            nota = "Si"
            return print("Tocando violin en ",nota)


class Bajo(Instrumento):

    def afinar(self):
        return print("Afinando bajo")

    def tocar(self):
        return print("Tocando bajo")

    def tocar_nota(self):

        opc2 = random.randrange(7)
        if(opc2 == 1):
            nota = "Do"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 2):
            nota = "Re"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 3):
            nota = "Mi"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 4):
            nota = "Fa"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 5):
            nota = "Sol"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 6):
            nota = "La"
            return print("Tocando bajo en ",nota)
        elif(opc2 == 7):
            nota = "Si"
            return print("Tocando bajo en ",nota)

class Persona(object):

    def __init__(self,nombre):
        self.nombre = nombre

    def presentar(self, nombre):
        print("Hola mi nombre es ",musicos[nombre])


class Musico (Persona):

    def tocar(self, j):
        j.afinar()
        j.tocar()
        j.tocar_nota()

class Banda(object):

    def agregar_musico(self, nombre):
        musicos.append(nombre)
        return musicos

    def generar_instrumento(self):
        opc = random.randrange(3)
        if(opc == 1):
            l = Guitarra()
            return l
        elif(opc == 2):
            i = Bajo()
            return i
        elif(opc == 3):
            j = Violin()
            return j

    
    def presentar_banda(self):
        m = Musico
        tamaño_lista = len(musicos)
        for i in range(0, tamaño_lista):
            m.presentar("", i)
            m.tocar("",b.generar_instrumento(""))
     
b = Banda
b.agregar_musico("","Pepito")
b.agregar_musico("","Juan")
b.agregar_musico("","Mariana")
b.presentar_banda("")
