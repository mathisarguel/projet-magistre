from tkit import *
#petite modif pour gagner du temps apres

class graph:
    def __init__(self):
        self.g = ouvrirFenetre(400, 400)
        self.liste = [(350, 70, 25, "×", "fois"), (350, 140, 25, "/", "div"), (350, 210, 25, "+", "plus"),
                      (350, 280, 25, "-", "moins"), (350, 350, 25, "=", "egal"), (50, 50, 250, 75, "rectangle1"),
                      (50, 150, 250, 75, "rectangle2"), (50, 250, 250, 75, "rectangle3")]

    def affichage(self):
        for i in self.liste:
            if type(i[3]) == int:
                self.g.dessinerRectangle(i[0], i[1], i[2], i[3], "grey")
            else:
                self.g.dessinerDisque(i[0], i[1], i[2], "orange")
                self.g.afficherTexte(i[3], i[0], i[1], col="black", sizefont=25)

    def recup_clic(self):
        clic = self.g.attendreClic()
        print(clic)
        for i in self.liste:
            if type(i[3]) == int:
                if i[0] + i[2] >= clic.x >= i[0] and i[1] + i[3] >= clic.y >= i[1]:
                    return i[4]
            else:
                if (i[0] + i[2]) >= clic.x >= (i[0] - i[2]) and (i[1] + i[2]) >= clic.y >= (i[1] - i[2]):
                    return i[4]





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
print(a.recup_clic())
