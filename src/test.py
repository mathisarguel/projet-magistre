import tkinter as tk

class graph:
    def __init__():
        win = tk.Tk()
        win.title("Calculatrice")
        fct = tk.Canvas(win,width=500, height=500, bg="white")
        fct.pack()
        fct.create_rectangle(50, 50, 150, 150, outline="black", fill="lightblue", width=2)
        win.mainloop()



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
    def autrestest(self,"hdhd"):
        eprioekfjf

a = graph
a.__init__()