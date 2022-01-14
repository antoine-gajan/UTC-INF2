#Exerice 3 - Catalogue des cours

#Structure choisie : un dictionnaire de tableaux (ex: {INF2:("description","effectif","responsable"), MT12:(...)})
class Catalogue():
    def __init__(self):
        self.__uvs = {}

    def ajouterCours(self, code, description, effectif, responsable):
        "Ajoute un cours au catalogue"
        if code in self.__uvs.keys():
            raise ValueError("Cette UV est déjà dans le catalogue des UVs.")
        elif len(code) >= 5 :
            raise ValueError("Le code du cours est trop long.")
        else:
            self.__uvs[code] = [description, effectif, responsable]

    def supprimerCours(self, code):
        "Supprime un cours du catalogue"
        if code not in self.__uvs.keys():
            raise ValueError("Cette UV n'existe pas.")
        else:
            self.__uvs.pop(code)

    def recupererCours(self, code):
        "Renvoie le détail du cours"
        if code not in self.__uvs:
            raise ValueError("Cette UV n'existe pas.")
        else:
            print(f"UV {code} :")
            print(f"Description : {self.__uvs[code](0)}")
            print(f"Effectif : {self.__uvs[code](1)}")
            print(f"Responsable : {self.__uvs[code](2)}")

    def modifierCours(self, code, **kwargs):
        "Modifie un cours"
        if code not in self.__uvs.keys():
            raise ValueError("Cette UV n'existe pas.")
        else:
            if kwargs.get("description"):
                self.__uvs[code][0] = kwargs.get("description")
            if kwargs.get("effectif"):
                self.__uvs[code][1] = kwargs.get("effectif")
            if kwargs.get("responsable"):
                self.__uvs[code][2] = kwargs.get("responsable")

    def modifierCodeCours(self, code, nouveau_code):
        "Modifie le code d'un cours"
        if code not in self.__uvs.keys():
            raise ValueError("Cette UV n'existe pas.")
        else:
            infos = self.__uvs[code]
            self.supprimerCours(code)
            self.ajouterCours(nouveau_code, infos[0], infos[1], infos[2])

    def listerCours(self):
        for cours in sorted(self.__uvs.keys()):
            self.recupererCours(cours)
            print("--------------")









