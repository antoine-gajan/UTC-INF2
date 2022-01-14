#TD 7 - Exercice 1 - Distance sinus
import numpy as np
import math
from affichage_graphique import *

def sinus(xmin:float, xmax:float, pas:float, nom_fichier:str):
    "Remploir nom_fichier avec les coules de valeurs (x, distance de sin(x) par rapport à l'origine avec x variant entre xmin et xmax avec un pas"
    with open(nom_fichier, 'w') as distance_sinus:
        x_values = np.arange(xmin, xmax, pas)
        y_values = [math.sqrt(x**2 + math.sin(x)**2) for x in x_values]
        for i in range(len(x_values)):
            distance_sinus.write(f"{x_values[i]},{y_values[i]}\n")

def lireEtAfficher(nom_fichier:str):
    "Lit et affiche la courbe assocée à nom_fichier"
    x_values = []
    y_values = []
    with open(nom_fichier, 'r') as distance_sinus:
        for ligne in distance_sinus:
            data = ligne.split(',')
            x_values.append(float(data[0]))
            y_values.append(float(data[1]))
        affiche_courbe(x_values,y_values,"Exercice 1 - Distance sinus", "x", "sqrt(x²+sin²(x)")


def main():
    xmin = float(input("xmin = "))
    xmax = float(input("xmax = "))
    pas = float(input("Pas = "))
    nom_fichier = input("Nom du fichier : ")
    sinus(xmin, xmax, pas, nom_fichier)
    lireEtAfficher(nom_fichier)

if __name__ == "__main__":
    main()
