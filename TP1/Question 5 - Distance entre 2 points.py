#Question 5  - Programme qui indique la distance entre 2 points du plan rentrés par l'utilisateur

#import du module permettant de calculer la racine carrée
from math import sqrt

#Indique à l'utilisateur le rôle du programme
print("Question 5 - Programme qui indique la distance entre 2 points de l'espace")

#Demande à l'utilisateur les coordonnées des 2 points A et B
#Pour le point x
print("Coordonnées du point A=(x1, y1) : ")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

#Saut d'une ligne pour un meilleur rendu
print()

#Pour le point y
print("Coordonnées du point B=(x2, y2) :")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

#Calcul de la distanc entre les points A et B
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Affichage du résultat
print(f"La distance entre les points ({x1},{y1}) et ({x2},{y2}) est {distance}")
