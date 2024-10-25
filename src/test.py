from tkit import *
#petite modif pour gagner du temps apres

class graph:
    def __init__(self):
        self.g = ouvrirFenetre(400, 400)
        self.liste = [(350, 70, 25, "×", "fois"), (350, 140, 25, "/", "div"), (350, 210, 25, "+", "plus"),
                      (350, 280, 25, "-", "mois"), (350, 350, 25, "=", "egal"), (50, 50, 250, 75, "rectangle1"),
                      (50, 150, 250, 75, "rectangle2"), (50, 250, 250, 75, "rectangle3")]

    def affichage(self):
        for i in self.liste:
            if type(i[3])==int:
                rectangle(i[0], i[1], i[2], i[3]).affichage(self.g)
            else:
                bouton(i[0], i[1], i[2], i[3]).affichage(self.g)
        self.g.attendreClic()

class bouton:
    def __init__(self,x,y,r, signe):
        self.x = x
        self.y = y
        self.r = r
        self.signe = signe

    def affichage(self, graph):
        graph.dessinerDisque(self.x, self.y, self.r, "orange")
        graph.afficherTexte(self.signe,self.x,self.y, col="black", sizefont=25)

class rectangle:
    def __init__(self,x,y,longeur,largeur):
        self.x = x
        self.y = y
        self.longeur = longeur
        self.largeur = largeur

    def affichage(self, graph):
        graph.dessinerRectangle(self.x,self.y, self.longeur,self.largeur,"grey")

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



a = graph()

a.affichage()

