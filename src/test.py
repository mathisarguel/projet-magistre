from tkit import *
#petite modif pour gagner du temps apres

class graph:
    def __init__(self):
        self.g = ouvrirFenetre(400, 400)
        self.liste = [(350, 50, 25, "×", "fois"), (350, 110, 25, "/", "div"), (350, 170, 25, "+", "plus"),
                      (350, 230, 25, "-", "moins"), (350, 350, 25, "AC", "AC"),
                      (50, 50, 250, 75, "rectangle1"),
                      (50, 150, 250, 75, "rectangle2"), (50, 250, 250, 75, "rectangle3")]
        self.dico = {}

    def affichage(self):
        for i in self.liste:
            if type(i[3]) == int:
                self.g.dessinerRectangle(i[0], i[1], i[2], i[3], "grey")
                self.dico[i[4]] = self.g.afficherTexte("", i[0] + (i[2] // 2), i[1] + (i[3] // 2), col = "white", sizefont=25)

            else:
                self.g.dessinerDisque(i[0], i[1], i[2], "orange")
                self.g.afficherTexte(i[3], i[0], i[1], col="black", sizefont=25)

    def recup_clic(self):
        clic = self.g.attendreClic()
        for i in self.liste:
            if type(i[3]) == int:
                if i[0] + i[2] >= clic.x >= i[0] and i[1] + i[3] >= clic.y >= i[1]:
                    return i[4]
            else:
                if (i[0] + i[2]) >= clic.x >= (i[0] - i[2]) and (i[1] + i[2]) >= clic.y >= (i[1] - i[2]):
                    return i[4]

    def recp_valeur(self, rectangle):
        liste = []
        touche = self.g.attendreTouche()
        while touche != "Return":
            if touche.isdigit():
                liste.append(touche)
                nbr = "".join(liste)
                self.g.changerTexte(self.dico[rectangle],nbr)
            touche = self.g.attendreTouche()
        nbr = "".join(liste)
        return nbr


    def modif_texte(self, obj, texte):
        self.g.changerTexte(self.dico[obj], texte)
        self.g.actualiser()


class calculatrice:
    def __init__(self,graph, a = 0, b = 0, signe = ""):
        self.a = a
        self.b = b
        self.signe = signe
        self.graph = graph


    def mode(self):
        clic = self.graph.recup_clic()
        if clic == "rectangle1" :
            self.a = int(self.graph.recp_valeur("rectangle1"))
        elif clic == "rectangle2" :
            self.b = int(self.graph.recp_valeur("rectangle2"))
        elif clic == "AC":
            self.graph.modif_texte("rectangle2","")
            self.graph.modif_texte("rectangle1","")
            self.a, self.b = 0, 0
            self.graph.modif_texte("rectangle3", "")
        elif clic != "rectangle3":
            self.signe = clic
        if clic != "AC" and self.a != 0 and self.b != 0:
            self.graph.modif_texte("rectangle3", self.dico(self.signe))
        self.mode()




    def lancement(self):
        self.graph.affichage()
        self.mode()


    def dico(self, a):
        if a == "plus":
            return self.plus()
        elif a == "moins":
            return self.moins()
        elif a == "fois":
            return self.fois()
        elif a == "div":
            return self.div()
        elif a =="AC":
            return self.Ac()

    def plus(self):
        return self.a + self.b

    def moins(self):

        return self.a - self.b

    def fois(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("error")
            print("test")

    def Ac(self):
        self.graph.modif_texte("rectangle1", "")
        self.graph.modif_texte("rectangle2", "")
        self.a = 0
        self.b = 0


a = graph()
c = calculatrice(graph=a)
c.lancement()
