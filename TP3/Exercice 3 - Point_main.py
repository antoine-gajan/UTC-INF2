#Exercice 3 - Programme principal pour la 1ère partie de l'énoncé (Classe Point)

#Import de la classe Point issu de l'autre fichier
from Exercice3_Point import Point

def main():
    #Affiche le rôle du programme
    print("Exercice 3 - Point du plan")
    print("----------------------")
    #Demande des informations concernant le 1er point
    print("Point 1 : ")
    abs = float(input("Abscisse : "))
    ord = float(input("Ordonnée : "))
    point1 = Point(abs, ord)
    #On affiche les caractéristiques du 1er point
    print(point1)
    print("----------------------")
    #Demande des informations concernant le 2ème point
    print("Point 2 : ")
    abs = float(input("Abscisse : "))
    ord = float(input("Ordonnée : "))
    point2 = Point(abs, ord)
    #On affiche les caractéristiques du 2ème point
    print(point2, "\n")
    #On affiche la distance entre les 2 points
    print(f"La distance entre le point A = {point1} et le point B = {point2} est {point1.calculer_distance(point2)}")
    #On affiche le milieu entre les 2 points saisis par la personne
    print(f"Le milieu est : {point1.calculer_milieu(point2)}")

if __name__ == "__main__":
    main()
