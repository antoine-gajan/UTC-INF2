#TP1 - Programme permettant de calculer la surface d'un cercle en fonction du rayon

#import de la librairie math et du nombre pi
from math import pi

#Indique le rôle du programme à l'utlisateur
print("Question 1 - Calcul de la surface en fonction du rayon")

#Demande du rayon à l'utilisateur
rayon = float(input("Entrez le rayon du cercle : "))

if rayon > 0 : #si le rayon est valide
    #Calcul de la surface en fonction du rayon (la formule est surface = pi * (rayon**2)
    surface = pi * rayon**2
    #Affichage du résultat de la surface
    print(f"La surface du cercle de rayon {rayon} est {surface}")
else : #si le rayon entré est négatif, la surface n'exsite pas : le programme s'arrête
    print(f"Le rayon entré est négatif. Impossible de calculer la surface.")




