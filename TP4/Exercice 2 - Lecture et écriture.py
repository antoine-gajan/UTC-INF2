#Exercice 2 - Lecture et écriture dans un fichier

#Import des différents modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ecrire(fichier:str):
    "Stocke les résultats dans un fichier csv"
    #Initialisation d'un tableau avec les valeurs d'abscisse
    abscisse = [x for x in range(-5, 6)]
    print(f"x = {abscisse}")
    #Initialisation d'un tableau avec les valeurs de cosinus correspondantes
    ordonnee = [np.cos(x) for x in abscisse]
    print(f"cos(x) = {ordonnee}")
    #Création d'un dataframe avec les données
    donnees = pd.DataFrame({'x': abscisse, 'cosinus': ordonnee}, columns=['x', 'cosinus'])
    #Export des données dans le fichier csv codé en utf-8, avec un entête et comme séparateur le point-virgule
    donnees.to_csv(fichier, index=None, header=True, encoding='utf-8', sep=';')


def lire(fichier:str):
    "Lit les données d'un fichier csv"
    #Création d'un dataframe avec les données du fichier
    donnees = pd.read_csv(fichier, usecols=['x', 'cosinus'], sep=';')
    #On affiche les données dans la console
    print(donnees)
    #Extraction du fichier des valeurs de x
    abscisse = donnees.x
    #Extraction du fichier des valeurs de cosinus
    ordonnee = donnees.cosinus

    #Tracage de la courbe du cosinus
    #Définition des valeurs minimales et maximales des axes x et y
    plt.xticks(np.arange(-5, 6, 1))
    plt.yticks(np.arange(-1, 1.25, 0.25))

    #Création du titre
    plt.title("Exercice 2 - Courbe du cosinus", fontweight="bold", pad=15, color="b")

    #Etiquettes du grpahique
    plt.xlabel("x")
    plt.ylabel("cos(x)")

    #Ajout des points sur le graphique
    plt.plot(abscisse, ordonnee)

    #Affichage et fermeture du grpahique
    plt.show()
    plt.close()


def main():
    #Création d'un fichier math.csv contenant les valeurs de x et cos(x) pour x allant de -5 à 5
    ecrire('math.csv')
    #Lecture du fichier crée et affichage du graphique
    lire('math.csv')

if __name__ == "__main__":
    main()
