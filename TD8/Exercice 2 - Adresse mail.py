#Exercice 2 - Adresse mail

#Import du module Tkinter et PIL
from tkinter import *
from PIL import Image, ImageTk

class Fenetre(Tk):
    def __init__(self, largeur = 500, hauteur = 250):
        super().__init__()
        #Titre
        self.title("Formulaire mail")
        #Centrage de la fenêtre
        self.largeur_fenetre = largeur
        self.hauteur_fenetre = hauteur
        self.largeur_ecran = self.winfo_screenwidth()
        self.hauteur_ecran = self.winfo_screenheight()
        self.posx = self.largeur_ecran // 2 - self.largeur_fenetre // 2
        self.posy = self.hauteur_ecran // 2 - self.hauteur_fenetre //2
        self.geometry(f"{self.largeur_fenetre}x{self.hauteur_fenetre}+{self.posx}+{self.posy}")

        #Dictionnaire contenant les labels et les boutons
        self.labels = {}
        self.entrees = {}
        self.boutons = {}

        self.createLabel('nom', 'Nom : ', 1, 0)
        self.createLabel('prenom', 'Prénom : ', 2, 0)
        self.createLabel('domaine', 'Domaine : ', 3, 0)
        self.createLabel('valider', '', 4, 0, 3, sticky=W)

        self.createEntry('nom', 1, 1)
        self.createEntry('prenom', 2, 1)
        self.createEntry('domaine', 3, 1)

        self.createButton('valider', 'Valider', 5, 0, self.valider)
        self.createButton('reinitialiser', 'Réinitialiser', 5, 1, self.reinitialiser)
        self.createButton('quitter', 'Quitter', 5, 2, self.destroy)
        self.image()

    def createLabel(self, nom, texte, ligne, colonne, colonnespan = 1, sticky = E):
        self.labels[nom] = Label(self, text = texte, padx = 10, pady = 10)
        self.labels[nom].grid(row = ligne, column = colonne, columnspan = colonnespan, sticky = sticky)

    def createEntry(self, nom, ligne, colonne):
        self.entrees[nom] = Entry(self)
        self.entrees[nom].grid(row = ligne, column = colonne)

    def createButton(self, nom, texte, ligne, colonne, commande):
        self.boutons[nom] = Button(self, text = texte, command = commande)
        self.boutons[nom].grid(row = ligne, column = colonne)

    def valider(self):
        self.texte = f"{self.entrees['prenom'].get()}.{self.entrees['nom'].get()}@{self.entrees['domaine'].get()}"
        self.labels['valider'].config(text = self.texte)
        #ou self.labels['valider']['text'] = self.texte
        self.entrees['prenom'].delete(0, END)
        self.entrees['nom'].delete(0, END)
        self.entrees['domaine'].delete(0, END)

    def reinitialiser(self):
        self.entrees['prenom'].delete(0, END)
        self.entrees['nom'].delete(0, END)
        self.entrees['domaine'].delete(0, END)
        self.labels['valider'].config(text = '')
        #ou self.labels['valider']['text'] = ''

    def image(self):
        self.image = Image.open("drapeau.png")
        self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width = self.image.size[0], height = self.image.size[1])
        self.canvas.create_image(10, 0, anchor = NW, image = self.photo)
        self.canvas.grid(row = 1, column = 2, rowspan = 3)


fenetre = Fenetre()
fenetre.mainloop()