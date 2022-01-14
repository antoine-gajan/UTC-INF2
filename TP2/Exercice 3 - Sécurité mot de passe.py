#---------------------------------------------
#Exercice 3 - Tester la force d'un mot de passe
#----------------------------------------------


#Regarde le nombre de caractères en minuscule dans le mdp
def NBMin(password:str) -> int:
    #ajoute 1 à chaque lettre en minuscule du mdp
    return sum(map(str.islower, password))

#Regarde le nombre de caractères en majuscule dans le mdp
def NBMaj(password:str) -> int:
    #ajoute 1 à chaque lettre en majuscule du mdp
    return sum(map(str.isupper, password))

#Regarde le nombre de caractères non alphanumérique dans le mdp
def NBAlpha(password:str) -> int:
    #Comme la fonction isNotAlpha n'existe pas, on prend le nombre de caractères du mdp et on enlève le nombre de caractères alphabétiques
    return len(password) - sum(map(str.isalpha, password))

#Regarde la séquence de la plus longue séquence de lettres minuscules
def LongMin(password:str) -> int:

    #On initialise la plus longue séquence max à 0
    maxNumber = 0
    # On initialise la séquence de traitement à 0
    currentNumber = 0


    #On étudie chaque caractère du mdp
    for char in password:
        if char.islower():
            # Si le caractère est en miniscule on ajoute 1 la la séquence en cours
            currentNumber = currentNumber+1
        else:
            # Si le caractère n'est pas en miniscule (nombre, caractère spécial ou maj) la séquence est finie

            if currentNumber > maxNumber:
                # Si la séquence actuelle est plus longue que la séquence maximale on change la longueur de la séquence la plus longue
                maxNumber = currentNumber
            #On remet à 0 la séquence en cours de traitement
            currentNumber = 0

    # À la fin de l'execution, on force la fin de la dernière séquence, et on retraite comme ci-dessus
    if currentNumber > maxNumber:
        maxNumber = currentNumber

    return maxNumber

#Regarde la séquence de la plus longue séquence de lettres majuscules
def LongMaj(password:str) -> int:

    # On initialise la plus longue séquence max à 0
    maxNumber = 0
    # On initialise la séquence de traitement à 0
    currentNumber = 0

    # On étudie chaque caractère du mdp
    for char in password:

        if char.isupper():
            # Si le caractère est en majuscule on ajoute 1 la la séquence en cours
            currentNumber = currentNumber+1
        else:

            # Si le caractère n'est pas en majuscule (nombre, caractère spécial ou min) la séquence est finie
            if currentNumber > maxNumber:
                # Si la séquence est plus longue que la séquence maximale on change la longueur de la séquence la plus
                maxNumber = currentNumber
            # On remet à 0 la séquence en cours de traitement
            currentNumber = 0

    # À la fin de l'execution, on force la fin de la dernière séquence, et on retraite comme ci-dessus
    if currentNumber > maxNumber:
        maxNumber = currentNumber

    return maxNumber

#Calcul le score final du mdp et le converti en force
def Score(password:str):
    #On récupère la longueur du mdp
    passLength = len(password)

    # On calcul des bonus basés sur l'énoncé
    scoreLength = passLength*4
    scoreUpper = (passLength - NBMaj(password)) * 2
    scoreLower = (passLength - NBMin(password)) * 3
    scoreNonAlpha = NBAlpha(password) * 5

    # On calcul des malus basés sur l'énoncé
    malusLongLower = LongMin(password) * 2
    malusLongUpper = LongMaj(password) * 3

    # On additionne les bonus et soustrait les malus pour avoir le score final
    finalScore = (scoreLength+scoreLower+scoreUpper+scoreNonAlpha)-(malusLongLower+malusLongUpper)
    print(finalScore)
    #Comme indiqué sur l'énoncé, on traite le score final pour donner un résultat compréhensif à l'utilisateur
    if finalScore < 20:
        print("La force de votre mot de passe est TRÈS FAIBLE")
    elif finalScore < 40:
        print("La force de votre mot de passe est FAIBLE")
    elif finalScore < 80:
        print("La force de votre mot de passe est FORT")
    else:
        print("La force de votre mot de passe est TRÈS FORT")

#Programme principal
def main():
    #Affiche le rôle du programme
    print(f"Exercice 3 - Force du mot de passe")
    #On demande à l'utilisateur de rentrer un mot de passe
    inputPassword = str(input("Mot de passe à tester : "))

    #On vérifie que le mot de passe est valide (qu'il n'est pas vide et qu'il n'a pas d'espace)
    if len(inputPassword) <= 0 or " " in inputPassword:
        print("Le mot de passe entré n'est pas valide")
    else:
        #On appelle la fonction de test des mots de passe
        Score(inputPassword)

if __name__ == "__main__":
    main()