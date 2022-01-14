#Exercice 1 - Sommet

class Sommet():
    __nbSommets = 0

    def __init__(self, nom):
        self.id = nom
        Sommet.__nbSommets += 1 #Toujours mettre le nom de la classe pour que l'interpréteur sache que c'est un attribut de classe

    def __str__(self):
        return f"Nom du sommet : {self.getID()}"

    def __del__(self): #del(mon_sommet) appelle A.__del__(mon_sommet)
        Sommet.__nbSommets -= 1

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nom):
        if nom.__hash__() != None:
            self.__id = nom
        else:
            raise TypeError("Le type de l'identificateur doit être hashable.")

    def getNbSommets(): #Pas de self car c'est une méthode de classe, pour l'appeller : Sommet.getNbSommets()
        return Sommet.__nbSommets


#script principal
def main():
    continuer = True
    while continuer:
        try:
            id = input("Entrez le nom de l'identificateur : ")
            sommet = Sommet(id)
            print("Sommet créé")
        except TypeError as error:
            print(error)
        finally:
            reponse = input("Voulez-vous continuer ? (O/N)").upper()
            continuer = reponse == 'O'

if __name__ == "__main__":
    main()




