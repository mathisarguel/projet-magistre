import tkinter as tk
widown = tk.Tk()
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

    def moins(self):
        self.cpt = self.chif1 - self.chif2

    def fois(self):
        self.cpt = self.chif1 * self.chif2

    def div(self):
        try:
            self.cpt = self.chif1/self.chif2
        except ZeroDivisionError:
            print("error")

