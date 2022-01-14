#Programme principal de l'exerice 2

#Import du fichier contenant la classe Personne
from Exercice2_Personne import Personne

def main():
    #Affiche le rôle du programme
    print("Exercice 2 - Personnes")
    print("----------------------")
    #Demande des informations concernant la prmeière personne
    print("Personne 1 : ")
    nom = input("Nom de famille : ")
    prenom = input("Prénom : ")
    age = int(input("Age : "))
    sexe = input("Sexe (M/F) : ")
    personne1 = Personne(nom, prenom, age, sexe)
    #On affiche les caractéristiques de la 1ère personne
    print(personne1)
    print("----------------------")
    #Demande des informations concernant la deuxième personne
    print("Personne 2 : ")
    nom = input("Nom de famille : ")
    prenom = input("Prénom : ")
    age = int(input("Age : "))
    sexe = input("Sexe (M/F) : ")
    #On affiche les caractéristiques de la 2eme personne
    personne2 = Personne(nom, prenom, age, sexe)
    print(personne2)
    print("----------------------")
    #On génère John Doe 30 ans avec le constructeur par défaut
    print("Personne 3 : ")
    personne3 = Personne()
    print(personne3)
    print()
    #On utilise les méthodes créées
    #On compare les noms de famille des 3 personnes créées
    if personne1.sameLastName(personne2):
        print("Les deux personnes que vous avez saisies portent le même nom de famille.")
    else:
        print("Les deux personnes saisies ne portent pas le même nom de famille.")
    if personne1.sameLastName(personne3):
        print("La 1ère personne porte le même nom de famille que John Doe !")
    else:
        print("La 1ère personne ne porte pas le même nom de famille que John Doe.")
    if personne2.sameLastName(personne3):
        print("La 2ème personne porte le même nom de famille que John Doe !")
    else:
        print("La 2ème personne ne porte pas le même nom de famille que John Doe.")
    print()
    #On affiche la personne la plus âgée, en comparant d'abord les 2 premières personnes puis en comparant avec l'âge de John Doe
    print(f"La personne la plus âgée est : \n{personne1.oldest(personne2).oldest(personne3)}")


if __name__ == "__main__":
    main()



