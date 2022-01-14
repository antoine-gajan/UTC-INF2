#Exercice 1 - Programme qui vérifie si les parenthèses, accolades et crochets sont correctement fermés

from collections import deque

def verifier(texte:str):
    "Renvoie True si la syntaxe est correcte"
    #Création d'un dictionnaire avec les couples
    couples = {'{':'}', '[':']', '(':')'}
    #Création d'une pile qui va contenir l'ensemble des parenthèses, accolades et crochets ouvrants
    pile = deque()
    #Parcours du texte
    for car in texte:
        #si le caractère est "ouvrant", on l'ajoute à la pile
        if car in couples.keys():
            pile.append(car)
        #si le caractère est "fermant", on vérifie qu'il correspond à l'opposé du dernier empilé
        elif car in couples.values():
            #si le caractère est l'opposé du dernier élément de la pile, on continue
            ouvrant = pile.pop()
            if car != couples[ouvrant]:
                return False
    #si la taille de la pile vaut 0, la syntaxe est correcte
    if len(list(pile)) == 0:
        return True
    #sinon il reste des ouvrants sans correspondance, la syntaxe n'est pas correcte
    return False

