from tkit import *

class graph:
    def __init__(self):
        self.g = ouvrirFenetre(400,400)
        self.g.attendreClick()


class bouton:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r


class calcul:
    def __init__(self,a,b):
        self.chif1 = a
        self.chif2 = b
        cpt = 0

    def run(self):
        try:
            self.chif1 = int(input("premier chiffre"))
        except :
            while type(self.chif1) != int:
                self.chif1 = int(inpuut("Rentrer un chiffre"))
        try:
            self.chif2 = int(input("deuxieme chiffre"))
        except:
            while type(self.chif2) != int:
                self.chif2 = int(inpuut("Rentrer un chiffre"))


    def plus(self):
        self.cpt = self.chif1  + self.chif2
        print(self.cpt)

    def moins(self):
        self.cpt = self.chif1 - self.chif2

    def fois(self):
        self.cpt = self.chif1 * self.chif2

    def div(self):
        try:
            self.cpt = self.chif1/self.chif2
        except ZeroDivisionError:
            print("error")
            print("test")

