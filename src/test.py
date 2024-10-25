from tkit import *
class graph:
    def __init__(self):
        self.g = ouvrirFenetre(400,400)


    def affichage(self):
        bouton(350,70,25,"×").affichage(self.g)
        bouton(350,140,25,"/").affichage(self.g)
        bouton(350, 210, 25,"-").affichage(self.g)
        bouton(350, 280, 25,"+").affichage(self.g)
        bouton(350, 350, 25,"=").affichage(self.g)
        rectangle(50,50,250,75).affichage(self.g)
        rectangle(50, 150, 250, 75).affichage(self.g)
        rectangle(50, 250, 250, 75).affichage(self.g)


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
        self.chif1 = int(input("premier chiffre"))
        self.chif2 = int(input("deuxieme chiffre"))



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