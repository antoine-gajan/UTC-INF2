#Exercice 1 - Création de fenêtre

#Import du module Tkinter
from tkinter import *

class Fenetre(Tk):
    def __init__(self, titre, largeur = 100, hauteur = 100):
        super().__init__()
        #Titre et fond d'écran
        self.title(titre)
        self.config(bg='yellow')
        #Centrage de la fenêtre
        self.largeur_fenetre = largeur
        self.hauteur_fenetre = hauteur
        self.largeur_ecran = self.winfo_screenwidth()
        self.hauteur_ecran = self.winfo_screenheight()
        self.posx = self.largeur_ecran // 2 - self.largeur_fenetre // 2
        self.posy = self.hauteur_ecran // 2 - self.hauteur_fenetre //2
        #Pour positionner sur la fenêtre
        self.geometry(f"{self.largeur_fenetre}x{self.hauteur_fenetre}+{self.posx}+{self.posy}")
        #Création des labels et bouton quitter
        self.labels = {}

    def createLabel(self, nom, texte):
        self.labels[nom] = Label(self, text = texte)
        self.labels[nom].pack()

    def boutonQuitter(self):
        self.boutonQuitter = Button(self, text='Quitter', command = self.destroy)
        self.boutonQuitter.pack()

#Programme principal
def main():
    """largeur = int(input('Largeur : '))
    hauteur = int(input('Hauteur : '))"""
    fenetre = Fenetre(largeur, hauteur)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
