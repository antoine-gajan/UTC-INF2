#Exerice 4 - Echiquier

from tkinter import *

class Echiquier(Tk):
    def __init__(self, largeur=400, hauteur=400):
        super().__init__()
        # Titre
        self.title("Echiquier")
        # Centrage de la fenêtre
        self.largeur_fenetre = largeur
        self.hauteur_fenetre = hauteur
        self.largeur_ecran = self.winfo_screenwidth()
        self.hauteur_ecran = self.winfo_screenheight()
        self.posx = self.largeur_ecran // 2 - self.largeur_fenetre // 2
        self.posy = self.hauteur_ecran // 2 - self.hauteur_fenetre // 2
        self.geometry(f"{self.largeur_fenetre}x{self.hauteur_fenetre}+{self.posx}+{self.posy}")

        #Création de l'échiquier
        for i in range(1,9):
            for j in range(1,9):
                if (i + j) % 2 == 0:
                    self.createCase('black', i, j)
                else:
                    self.createCase('white', i, j)


    def createCase(self, couleur, ligne, colonne):
        self.case = Canvas(self, width=50, height=50, bg=couleur, borderwidth = -2)
        self.case.grid(row = ligne, column = colonne)


echiquier = Echiquier()
echiquier.mainloop()