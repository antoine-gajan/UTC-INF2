#TD 3 - Exercice 1 : Objets (date)

class Date():
    def __init__(self, jour, mois, annee):
        self.setMois(mois)
        self.setJour(jour)
        self.setAnnee(annee)

    def __str__(self):
        return f"{self.__jour:02}/{self.__mois:02}/{self.__annee}"

    def getJour(self):
        return self.__jour

    def getMois(self):
        return self.__mois

    def getAnnee(self):
        return self.__annee

    def setJour(self, jour):
        if (jour >= 1) and (jour <= 31) and self.__mois in (1, 3, 5, 7, 8, 10, 12):
            self.__jour = jour
        elif (jour >= 1) and (jour <= 30) and self.__mois in (4, 6, 9, 11):
            self.__jour = jour
        elif (jour >= 1) and (jour <= 28) and self.__mois == 2:
            self.__jour = jour
        else:
            raise ValueError(f"La date {jour}/{self.__mois}/{self.__annee} n'existe pas")

    def setMois(self, mois):
        if (mois >= 1) and (mois <= 12):
            self.__mois = mois
        else:
            raise ValueError("Le mois doit être compris entre 1 et 12")

    def setAnnee(self, annee):
        self.__annee = annee

    def jour_du_lendemain(self):
        #Gestion des cas particuliers
        if self.__jour == 31 and self.__mois == 12 :
            return Date(1, 1, self.__annee + 1)
        elif self.__jour == 31 and self.__mois in (1, 3, 5, 7, 8, 10):
            return Date(1, self.__mois + 1, self.__annee)
        elif self.__jour == 30 and self.__mois in (4, 6, 9, 11):
            return Date(1, self.__mois + 1, self.__annee)
        elif self.__jour == 28 and self.__mois == 2:
            return Date(1, self.__mois + 1, self.__annee)
        #Cas normal
        else:
            return Date(self.__jour + 1, self.__mois, self.__annee)

#Programme principal pour calculer les dates de 2021
date = Date(1, 1, 2021)
mois = 1
while date.getAnnee() == 2021:
    print(date, end=" ")
    date = date.jour_du_lendemain()
    if date.getMois() != mois:
        print()
        mois = date.getMois()

