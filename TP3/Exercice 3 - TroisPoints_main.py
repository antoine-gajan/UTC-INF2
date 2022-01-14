#Exercice 3 - Programme principal pour la 2eme partie de l'énoncé (Classe TroisPoints et Point)

#Import de la classe Point issu de l'autre fichier
from Exercice3_Point import Point, TroisPoints

#Programme principal
def main():
    #Affiche le rôle du programme
    print("Exercice 3 - Trois points du plan")
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
    print(point2)
    print("----------------------")
    # Demande des informations concernant le 3ème point
    print("Point 3 : ")
    abs = float(input("Abscisse : "))
    ord = float(input("Ordonnée : "))
    point3 = Point(abs, ord)
    # On affiche les caractéristiques du 3ème point
    print(point3, "\n")
    #On crée l'objet de classe TroisPoints associé
    triangle = TroisPoints(point1, point2, point3)
    # On affiche si les trois points sont alignés
    if triangle.sont_alignes():
        print("Les trois points sont alignés.")
    #sinon, ils ne sont pas alignés
    else:
        print("Les trois points ne sont pas alignés.")
    #On affiche si le triangle formé par les 3 points est isocèle
    if triangle.est_isocele():
        print("Le triangle formé par les trois points est isocèle.")
    #sinon, le triangle n'est pas isocèle
    else:
        print("Le triangle formé par les trois points n'est pas isocèle.")


if __name__ == "__main__":
    main()



