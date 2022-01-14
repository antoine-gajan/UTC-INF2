#TD 3 - Exercice 2

class Horaire():
    def __init__(self, h, m):
        self.heure, self.minute = h, m #Utilisation des properties
        """self.setHeure(h)
        self.setMin(m)""" #équivalent sans les properties

    def __str__(self):
        return f"{self.heure}h{self.minute}min"

    def getHeure(self):
        return self.__heure

    def getMin(self):
        return self.__min

    def setHeure(self, h):
        if not isinstance(h, int):
            raise TypeError("L'heure doit être de type entière")
        elif (h < 0) or (h > 23):
            raise ValueError("L'heure doit être comprise entre 0 et 23")
        else:
            self.__heure = h

    def setMin(self, m):
        if not isinstance(m, int):
            raise TypeError("Les minutes doivent être de type entières")
        elif (m < 0) or (m > 59):
            raise ValueError("Les minutes doivent être comprises entre 0 et 59")
        else:
            self.__min = m

    minute = property(getMin, setMin)
    heure = property(getHeure, setHeure)

    def __add__(self, duree):
        if self.heure + duree.heure >= 24:
            h = (self.minute + duree.minute) % 24
        if self.minute + duree.minute >= 60:
            min = (self.minute + duree.minute) % 60
            h += 1
        return Horaire(h, min)


class Duree():
    def __init__(self, h, m):
        self.heure, self.minute = h, m  # Utilisation des properties
        """self.setHeure(h)
        self.setMin(m)"""  # équivalent sans les properties

    def __str__(self):
        return f"{self.heure}h{self.minute}min"

    def getHeure(self):
        return self.__heure

    def getMin(self):
        return self.__min

    def setHeure(self, h):
        if not isinstance(h, int):
            raise TypeError("L'heure doit être de type entière")
        elif (h < 0) or (h > 23):
            raise ValueError("L'heure doit être comprise entre 0 et 23")
        else:
            self.__heure = h

    def setMin(self, m):
        if not isinstance(m, int):
            raise TypeError("Les minutes doivent être de type entières")
        elif (m < 0) or (m > 59):
            raise ValueError("Les minutes doivent être comprises entre 0 et 59")
        else:
            self.__min = m

    minute = property(getMin, setMin)
    heure = property(getHeure, setHeure)

class Vol():
    def __init__(self, nom, depart, duree):
        self.__nom = nom
        self.__depart = depart
        self.__duree = duree
        self.__arrivee = depart + duree

    def __str__(self):
        return f"Vol : {self.__nom} \n Départ : {self.__depart} \n Durée : {self.__duree} \n Arrivée : {self.__arrivee}"

