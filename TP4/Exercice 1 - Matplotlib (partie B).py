#Exercice 1 - Matplotlib Partie B

#Import des librairies matplotlib et numpy
import matplotlib.pyplot as plt
import numpy as np

#Initialisation du graphe et de ses axes
figure, axes = plt.subplots()


#Définition des graduations des axes x et y
plt.xticks(np.arange(-10, 25, 5))
plt.yticks(np.arange(0, 20, 2.5))

#Les axes ont la même échelle en abscisse et en ordonnée, ce qui permet d'obtenir des cercles et non des ellipses
axes.set_aspect(1)

#Création d'un titre
plt.title("Exercice 1 - Triangle de cercles", fontweight="bold", pad=15, color="b")

#Fonction qui permet de créer un cercle
def cercle(x0:float, y0:float, r:float) -> None:
    "Création d'un cercle de centre (x0,y0) et de rayon r"
    #Création de valeurs comprises entre 0 et 2pi
    valeur = np.linspace(0, 2 * np.pi, 300)
    #On calcule les valeurs x et y à insérer dans le graphique
    x = x0 + r * np.cos(valeur)
    y = y0 + r * np.sin(valeur)
    #Ajout des points sur le graphique
    plt.plot(x, y)

#Programme principal
def main():
    #Boucle pour générer les 10 lignes de cercles de rayon 1
    for i in range(10):
        #Boucle pour créer les 10-i cercles de rayon 1 par ligne
        for j in range(10-i):
            #Chaque centre de cercle est espacé de 2 unités du précédent cercle selon l'axe des ordonnées
            #Chaque centre de cercle est espacé de 2 unités du précédent cercle selon l'axe des abscisses et on décale de 1 en abscisse par rapport à la précédente ligne
            cercle(i + 2 * j, 2 * i, 1)
    #Affichage du graphique
    plt.show()
    #Fermeture du graphique
    plt.close()

if __name__ == '__main__':
    main()