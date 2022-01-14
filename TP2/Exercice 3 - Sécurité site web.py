#Exercice 3 - Niveau de sécurité du mot de passe

def NBMin(password:str) -> int:
    "Renvoie le nombre de lettres minuscules du mot de passe"
    #Initialisation du compteur de lettres minuscules
    nb = 0
    #On parcourt la chaine de caractères et on incrémente le compteur à chaque minuscule rencontrée
    for caractere in password:
        if (caractere >= "a") and (caractere <= "z"):
            nb += 1
    #On retourne le nombre de lettres minuscules
    return nb


def NBMaj(password:str) -> int:
    "Renvoie le nombre de lettres majuscules du mot de passe"
    #Initialisation du compteur de lettres majuscules
    nb = 0
    #On parcourt la chaine de caractères et on incrémente le compteur à chaque majuscule rencontrée
    for caractere in password:
        if (caractere >= "A") and (caractere <= "Z"):
            nb += 1
    #On retourne le nombre de lettres majuscules
    return nb

def NBAlpha(password:str) -> int:
    "Renvoie le nombre de caractères non alphabétiques du mot de passe"
    #Initialisation du compteur de nombre de caractères non alphabétiques
    nb = 0
    #On parcourt la chaine de caractères et on incrémente le compteur à chaque caractère non alphabétique rencontrée
    for caractere in password:
        if (caractere < "A") or (caractere > "z"):
            nb += 1
    #On retourne le nombre de caractères non alphabétiques
    return nb

def LongMin(password:str) -> int:
    "Renvoie la longueur de la plus longue séquence de lettres minuscules du mot de passe"
    #Initialisation de la valeur de la plus longue séquence de lettres minuscules à 0
    plus_longue_seq = 0
    #Initialisation de la valeur courante de la longueur de la séquence de lettres minuscules
    nb = 0
    #Parcous de chacun des caractères du mot de passe
    for caractere in password:
        #si le caractère est une minuscule, on incrémente la longueur courante de 1
        if (caractere >= "a") and (caractere <= "z"):
            nb += 1
            #si la longueur courante est supérieure à celle maximale, elle remplace la valeur de la plus longue séquence
            if nb > plus_longue_seq:
                plus_longue_seq = nb
       #si un caractère n'est pas une minuscule, il coupe une séquence de minuscules : le compteur repart à 0
        else:
            nb = 0
    #On retourne la longueur de la plus longue séquence de minuscules
    return plus_longue_seq

def LongMaj(password:str) -> int:
    "Renvoie la longueur de la plus longue séquence de lettres majuscules du mot de passe"
    #Initialisation de la valeur de la plus longue séquence de lettres majuscules à 0
    plus_longue_seq = 0
    #Initialisation de la valeur courante de la longueur de la séquence de lettres majuscules
    nb = 0
    # Parcous de chacun des caractères du mot de passe
    for caractere in password:
        #si le caractère est une majuscule, on incrémente la longueur courante de 1
        if (caractere >= "A") and (caractere <= "Z"):
            nb += 1
            #si la longueur courante est supérieure à celle maximale, elle remplace la valeur de la plus longue séquence
            if nb > plus_longue_seq:
                plus_longue_seq = nb
        #si un caractère n'est pas une majuscule, il coupe une séquence de majuscules : le compteur repart à 0
        else:
            nb = 0
    #On retourne la longueur de la plus longue séquence de majuscules
    return plus_longue_seq

def Score(password:str):
    "Affiche la force du mot de passe"
    #Initialisation du score à 0
    score = 0

    #Calcul des différents bonus
    #Bonus 1 : Nombre de caractères * 4
    score += len(password) * 4
    #Bonus 2 : (Nombre total de caractères – nombre de lettres majuscules) * 2
    score += (len(password) - NBMaj(password)) * 2
    #Bonus 3 : (Nombre total de caractères – nombre de lettres minuscules) * 3
    score += (len(password) - NBMin(password)) * 3
    #Bonus 4 : Nombre de caractères non alphabétiques * 5
    score += NBAlpha(password) * 5

    #Calcul des différents malus
    #Malus 1 : longueur de la plus longue séquence de lettres minuscules * 2
    score -= LongMin(password) * 2
    #Malus 2 : Longueur de la plus longue séquence de lettres majuscules * 3
    score -= LongMaj(password) * 3

    print(score)
    #Si le score est inférieur à 20, la force du mot de passe est très faible
    if score < 20:
        print(f"La force du mot de passe {password} est TRES FAIBLE")
    #Sinon, si le score est inférieur à 40, la force du mot de passe est faible
    elif score < 40:
        print(f"La force du mot de passe {password} est FAIBLE")
    #sinon, si le score est inférieur à 80, la force du mot de passe est fort
    elif score < 80:
        print(f"La force du mot de passe {password} est FORT")
    #sinon, la force du mot de passe est très fort
    else:
        print(f"La force est du mot de passe {password} est TRES FORT")


def main():
    # Affiche le rôle du programme
    print("Exercice 3 - Force du mot de passe")

    # Initialisation de la variable continuer qui indique si l'utilisateur souhaite continuer ou non
    continuer = True
    while continuer:
        # Le programme demande un mot de passe à l'utilisateur
        password = (input("Entrez un mot de passe : "))
        Score(password)

        # On demande à l'utilisateur s'il souhaite tester d'autres mots de passe
        reponse = input("Voulez-vous continuer ? (O/N)").upper()
        # Tant qu'il répond autre chose que "O"(oui) ou "N"(non), on redemande
        while (reponse != "O") and (reponse != "N"):
            reponse = input("Voulez-vous continuer ? (O/N)").upper()
        # Actualisation de la variable réponse
        continuer = reponse == "O"


if __name__ == "__main__":
    main()




