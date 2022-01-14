#Exercice 2 - Personne

#Création de la classe Personne
class Personne():
    #Création du constructeur qui prend comme paramètre le nom, le prénom, l'âge et le sexe de la personne (par défaut, on crée John Doe, qui a 30 ans)
    def __init__(self, nom = "John", prenom = "Doe", age = 30, sexe = "M"):
        "Construit un objet de type Personne, contenant son nom, son prénom, son âge et son sexe"
        #si la personne a saisi pour nom une chaine de caractères non vide, alors le nom est valide
        if isinstance(nom, str) and nom != "":
            self.__nom = nom
        #sinon on génère une exception liée à la valeur
        else:
            raise ValueError("Le nom doit être une chaine de caractères non vide.")
        #si la personne a saisi pour prénom une chaine de caractères non vide, alors le prénom est valide
        if isinstance(prenom, str) and prenom != "":
            self.__prenom = prenom
        # sinon on génère une exception liée à la valeur
        else:
            raise ValueError("Le prénom doit être une chaine de caractères non vide.")
        #si la personne a saisi pour l'âge un entier supérieur à 0, alors l'âge est valide
        if isinstance(age, int) and age > 0 :
            self.__age = age
        #sinon on génère uen exception liée à la valeur
        else:
            raise ValueError("L'âge doit être un entier strictement positif.")
        #si la personne a saisi pour le sexe masculin ou féminin, alors le sexe est valide
        if (sexe.upper() == "M") or (sexe.upper() == "F"):
            self.__sexe = sexe.upper()
        #sinon on génère une exception liée à la valeur
        else:
            raise ValueError("Le sexe doit être soit masculin, soit féminin.")

    #Création des getters qui permettent de récupérer les valeurs des différents attributs de la personne
    def getLastName(self):
        "Retourne le nom de famille de la personne"
        return self.__nom

    def getName(self):
        "Retourne le prénom de famille de la personne"
        return self.__prenom

    def getAge(self):
        "Retourne l'âge de la personne"
        return self.__age

    def getSexe(self):
        "Retourne le sexe de la personne"
        return self.__sexe

    #Création d'une méthode qui permet de savoir si 2 personnes ont le même nom de famille
    def sameLastName(self, other):
        "Retourne True si self et other ont le même nom de famille"
        #On regarde si l'utilisateur a bien saisi une autre personne valide
        if isinstance(other, Personne):
            #si leur nom de famille est identique, alors on retourne True
            if self.getLastName() == other.getLastName():
                return True
            #sinon, on retourne False
            else:
                return False
        #sinon, on génère une exception concernant le type de other
        else:
            raise TypeError("Other doit être une personne.")

    def oldest(self, other):
        "Compare l'âge de self et other et retourne la personne qui est la plus âgée"
        #On regarde si l'utilisateur a bien saisi une autre personne valide
        if isinstance(other, Personne):
            #Si la personne appelante est plus âgée, alors on retourne self
            if self.getAge() > other.getAge():
                return self
            #sinon, on retourne other
            else:
                return other
        #Sinon, on génère une exception concernant le type de other
        else:
            raise TypeError("Other doit être une personne.")

    #Méthode qui affiche les caractéristiques de la personne
    def __str__(self):
        "Affiche les caractéristiques de la personne"
        return f"Nom de famille : {self.getLastName()} \nPrénom : {self.getName()} \nAge : {self.getAge()} ans\nSexe : {self.getSexe()}"
