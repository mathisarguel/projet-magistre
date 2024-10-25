import tkit.py
class graph:
    def __init__(self):
        self.g = ouvrirFenetre(600,800)
        self. g.attendreClick()


class bouton:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r


    def affichage(self):
        self.g.dessinercer


class calcul:
    def __init__(self,a,b):
        self.chif1 = a
        self.chif2 = b
        cpt = 0

    def run(self):
        self.chif1 = int(input("premier chiffre"))
        self.chif2 = int(input("deuxieme chiffre"))
    def


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

a = graph
a.__init__()