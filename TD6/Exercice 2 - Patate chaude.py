#Exercice 2 - Jeu de la patate chaude
from collections import deque
import random


def elimination(joueurs:list):
    "Affiche les éliminations et le gagnant du jeu"
    #Création d'une pile contenant les joueurs
    joueurs = deque(joueurs)
    #Tant qu'il reste plusieurs joueurs, le jeu continue
    while len(joueurs) != 1:
        #Nombre de passes aléatoires
        passes = random.randint(1, 10)
        #Vision tournante du jeu
        joueurs.rotate(-passes)
        #Elimination du joueur ayant la balle
        print(f"{joueurs.popleft()} a été éliminé.")
    #La taille de la pile vaut 1, donc ce joueur est le gagnant
    print(f"Le gagnant est {joueurs.pop()}.")


elimination(["A", "B", "C", "D", "E", "F", "G"])