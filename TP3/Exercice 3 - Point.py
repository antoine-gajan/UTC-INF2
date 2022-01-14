#Exercice 3 - Classes Point et TroisPoints

#import de la méthode sqrt de la librairie math
from math import sqrt

class Point():
    #On définit le constructeur de la classe Point
    def __init__(self, abs:float, ord:float):
        "Création d'un point du plan"
        self.abscisse = abs
        self.ordonnee = ord

    #Création des getter et setter pour récuper les valeurs des différents attributs et les modifier
    @property
    def abscisse(self):
        "Retourne l'abscisse du point courant"
        return self.__abs

    @abscisse.setter
    def abscisse(self, abs:float):
        "Modifie l'abscisse du point courant"
        #si l'utilisateur a saisi une abscisse de type float, alors l'abscisse est valide
        if isinstance(abs, float):
            self.__abs = abs
        #sinon, on génère une exception liée au type de la valeur
        else:
            raise TypeError("L'abscisse doit être un float.")

    @property
    def ordonnee(self):
        "Retourne l'ordonnée du point courant"
        return self.__ord

    @ordonnee.setter
    def ordonnee(self, ord:float):
        "Modifie l'ordonnée du point courant"
        #si l'utilisateur a saisi une ordonnée de type float, alors l'ordonnée est valide
        if isinstance(ord, float):
            self.__ord = ord
        #sinon, on génère une exception liée au type de la valeur
        else:
            raise TypeError("L'ordonnée doit être un float.")

    def calculer_distance(self, other):
        "Retourne la distance entre le point courant et le point entré en paramètre"
        #on vérifie que l'utilisateur ait rentré un objet de type Point en paramètre
        if isinstance(other, Point):
            #calcul de la distance entre les 2 points
            distance = sqrt((self.abscisse - other.abscisse)**2 + (self.ordonnee - other.ordonnee)**2)
            #On retourne la valeur de la distance entre les 2 points
            return distance
        #sinon, on génère une exception liée au type de la valeur placée en paramètre
        else:
            raise TypeError("Other doit être de type Point.")

    def calculer_milieu(self, other):
        "Retourne le milieu entre le point courant et le point entré en paramètre"
        #on vérifie que l'utilisateur ait rentré un objet de type Point en paramètre
        if isinstance(other, Point):
            #calcul des coordonnées du milieu entre le point courant et le point entré en paramètre
            milieu_abs = (self.abscisse + other.abscisse) / 2
            milieu_ord = (self.ordonnee + other.ordonnee) / 2
            #Création du milieu, un objet de type Point
            milieu = Point(milieu_abs, milieu_ord)
            #On retourne le point crée (le milieu)
            return milieu
        #sinon, on génère une exception liée au type de l'objet entré en paramètre
        else:
            raise TypeError("Other doit être de type Point.")

    def __str__(self):
        "Retourne les coordonnées du point courant"
        return f"({self.abscisse}, {self.ordonnee})"

#Classe TroisPoints
class TroisPoints():
    def __init__(self, premier, deuxieme, troisieme):
        self.premier = premier
        self.deuxieme = deuxieme
        self.troisieme = troisieme

    #Création des getter et setter pour récuper les valeurs des différents attributs et les modifier
    @property
    def premier(self):
        "Retourne le 1er point"
        return self.__premier

    @premier.setter
    def premier(self, point):
        "Modifie le 1er point"
        #on vérifie que l'utilisateur ait rentré un objet de type Point en paramètre
        if isinstance(point, Point):
            self.__premier = point
        #sinon, on génère une exception liée au type de la valeur placée en paramètre
        else:
            raise TypeError("Le point entré en paramètre doit être de type Point.")

    @property
    def deuxieme(self):
        "Retourne le 2ème point"
        return self.__deuxieme

    @deuxieme.setter
    def deuxieme(self, point):
        "Modifie le 2eme point"
        #on vérifie que l'utilisateur ait rentré un objet de type Point en paramètre
        if isinstance(point, Point):
            self.__deuxieme = point
        #sinon, on génère une exception liée au type de la valeur placée en paramètre
        else:
            raise TypeError("Le point entré en paramètre doit être de type Point.")

    @property
    def troisieme(self):
        "Retourne le 3ème point"
        return self.__troisieme

    @troisieme.setter
    def troisieme(self, point):
        "Modifie le 3eme point"
        #on vérifie que l'utilisateur ait rentré un objet de type Point en paramètre
        if isinstance(point, Point):
            self.__troisieme = point
        #sinon, on génère une exception liée au type de la valeur placée en paramètre
        else:
            raise TypeError("Le point entré en paramètre doit être de type Point.")

    def sont_alignes(self):
        "Retourne True si les 3 points sont alignés"
        #Calcul des distances entre les 3 points
        AB = self.premier.calculer_distance(self.deuxieme)
        AC = self.premier.calculer_distance(self.troisieme)
        BC = self.deuxieme.calculer_distance(self.troisieme)

        #On teste les conditions nécéssaires pour savoir s'ils sont alignés
        if (AB == AC + BC) or (AC == AB + BC) or (BC == AC + AB):
            return True
        #Sinon, ils ne sont pas alignés
        else:
            return False

    def est_isocele(self):
        "Retourne True si le triangle formé par les 3 points est isocèle"
        # Calcul des distances entre les 3 points
        AB = self.premier.calculer_distance(self.deuxieme)
        AC = self.premier.calculer_distance(self.troisieme)
        BC = self.deuxieme.calculer_distance(self.troisieme)

        # On teste les conditions nécéssaires pour savoir si le triangle est isocèle
        if (AB == AC) or (AC == BC) or (BC == AB):
            return True
        # Sinon, le triangle n'est pas isocèle
        else:
            return False









