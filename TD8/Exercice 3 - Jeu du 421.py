#Exerice 3 - Jeu du 421
import tkinter.messagebox
from tkinter import *
from random import randint
from Fenetre import *

class Jeu(Tk):
    def __init__(self, largeur=200, hauteur=300):
        super().__init__()
        # Titre
        self.title("Jeu du 421")
        # Centrage de la fenêtre
        self.largeur_fenetre = largeur
        self.hauteur_fenetre = hauteur
        self.largeur_ecran = self.winfo_screenwidth()
        self.hauteur_ecran = self.winfo_screenheight()
        self.posx = self.largeur_ecran // 2 - self.largeur_fenetre // 2
        self.posy = self.hauteur_ecran // 2 - self.hauteur_fenetre // 2
        self.geometry(f"{self.largeur_fenetre}x{self.hauteur_fenetre}+{self.posx}+{self.posy}")

        #Variable avec le nombre de coups
        self.coups = 0

        #Création de dictionnaires pour les labels et les boutons et les valeurs des dés
        self.labels = {}
        self.boutons = {}
        self.values = {}

        #Ajout sur la fenêtre des différents éléments
        self.construire()


    def construire(self):
        self.createLabel('titre', 'Jeu du 421', 1, 2)
        #Boutons pour les lancers
        self.createButton('de1', 'lancer dé 1', 2, 1, commande=lambda : self.lancer('de1'))
        self.createButton('de2', 'lancer dé 2', 3, 1, commande=lambda : self.lancer('de2'))
        self.createButton('de3', 'lancer dé 3', 4, 1, commande=lambda : self.lancer('de3'))
        #Labels pour afficher la valeur des dés
        self.createLabel('de1', '->  ', 2, 2, 'white', 'red')
        self.createLabel('de2', '->  ', 3, 2, 'white', 'red')
        self.createLabel('de3', '->  ', 4, 2, 'white', 'red')
        #Affichage du nombre de coups
        self.createLabel('resultat', f'Nb coups : {self.coups}', 5, 1, 'white', 'blue')

        #Bouton quitter
        self.BoutonQuitter(5, 2)

        #Ou :
        """for i in range ('1', '2', '3'):
            self.boutons[i] = Button(self, text = f'lancé dé {i}', command = lambda : self.lancerDe(i))
            self.boutons[i].grid(row = int(i), column = 0, pady = 10, padx = 10) 
        """

    def createLabel(self, nom, texte, ligne, colonne, bgcolor=None, fgcolor=None):
        self.labels[nom] = Label(self, text = texte, bg=bgcolor, fg=fgcolor)
        self.labels[nom].grid(row = ligne, column = colonne, padx = 5, pady = 10)

    def createButton(self, nom, texte, ligne, colonne, commande=NONE):
        self.boutons[nom] = Button(self, text=texte, borderwidth = 2, command = commande)
        #Ou pour la commande
        #Créer fonction lambda à la volée
        #def truc(x):
        #   print(x)
        #a = 4
        #f1 = lambda : truc(1)
        #f2 = lambda : truc(2)
        #f3 = lambda : truc(3)
        self.boutons[nom].grid(row = ligne, column = colonne, padx = 5, pady = 10)

    def BoutonQuitter(self, ligne, colonne):
        self.boutonQuitter = Button(self, text='Quitter', borderwidth = 2, command = self.destroy)
        self.boutonQuitter.grid(row = ligne, column = colonne, padx = 5, pady = 10)

    def lancer(self, nom):
        #Incrémentation du nombre de coups
        self.coups += 1
        self.labels['resultat']['text'] = f'Nb coups : {self.coups}'
        #Lancer du dé
        self.values[nom] = randint(1, 6)
        #Mise à jour de l'affichage
        self.labels[nom].config(text = f'-> {str(self.values[nom])}')
        #Regarde si le joueur a gagné
        self.gagner()

    def gagner(self):
        #Tri des valeurs des dés en ordre croissant
        self.tri = sorted([self.values.get('de1', 0), self.values.get('de2', 0), self.values.get('de3', 0)])
        #Si le joueur a gagné
        if  self.tri == [1, 2, 4]:
            #Affichage de la victoire
            self.victoire = tkinter.messagebox.showinfo('VICTOIRE', f'Félicitations ! Vous avez gagné en {self.coups} coups.')
            self.coups = 0

        #Ou :
        """
        des = set()
        for i in {'1', '2', '3'}:
            des.add(self.labels[i]['text'])
        if des == {'1', '2', '4'}:
            messagebox pour 421
        """



jeu = Jeu()
jeu.mainloop()