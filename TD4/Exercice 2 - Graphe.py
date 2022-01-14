#Exercice 2 - Graphe

from Exercice 1 - Sommet import *
class Graphe():
    def __init__(self, nom):
        self.nom = nom
        self.__succ = {}

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        if isinstance(nom, str):
            self.__nom = nom
        else:
            raise TypeError("Le nom doit être de type str.")

    def getSommets(self):
        return len(self.__succ.keys())

    def getNbArcs(self):
        return sum([len(self.__succ[key]) for key in self.__succ.keys()])

    def __str__(self):
        lignes = []
        lignes.append(f"Nom : {self.nom}, Nombre de sommets : {self.getSommets()}, Nombre d'arcs : {self.getNbArcs()}")
        for key in self.__succ.keys():
            ligne = f"{key} + {','.join(self.__succ[key])}"
            lignes.append(ligne)
        return '\n'.join(lignes)

    def __iadd__(self, other):
        if isinstance(other, Sommet):
            if other not in self.__succ.keys():
                self.__succ[other] = {}

        elif isinstance(other, (Sommet, Sommet)):
            if other[0] not in self.__succ.keys() and other[1] not in self.__succ.keys():
                self.__succ[other[0]] = {other[1]}
                self.__succ[other[1]] = {}
            elif other[1] not in self.__succ.keys():
                self.__succ[other[0]].add(other[1])
                self.__succ[other[1]] = {}
            elif other[0] not in self.__succ.keys():
                self.__succ[other[0]] = {other[1]}
            else:
                self.__succ[other[0]].add(other[1])

        else:
            raise TypeError("Il faut que other soit un tuple de sommets ou un sommet.")
