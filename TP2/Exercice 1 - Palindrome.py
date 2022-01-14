#Exercice 1 - Fonction récursive permettant de vérifier si un mot est un palindrome

#Création de la fonction récursive
def palindrome(mot:str) -> bool:
    "Indique si un mot est un palindrome"
    #si le mot est vide, il se lit pareil de gauche à droite ou de droite à gauche
    if len(mot) == 0:
        return True
    #si la première et la dernière lettre sont identiques, on regarde si le mot extrait sans la première et la dernière lettre est un palindrome
    elif mot[0] == mot[-1]:
        return palindrome(mot[1:-1])
    #si la première et la dernière lettre du mot sont différentes, le mot ne peut pas être un palindrome
    else:
        return False


#Programme principal utilisant cette fonction
def main():
    # Affiche le rôle du programme
    print("Exercice 1 - Ce programme vous permet de savoir si un mot est un palindrome.")

    #Initialisation de la variable continuer qui indique si l'utilisateur souhaite continuer ou non
    continuer = True
    while continuer:
        #Le programme demande un mot à l'utilisateur
        mot = input("Entrez un mot : ")
        #si le mot est un palindrome, on l'indique à l'utilisateur
        if palindrome(mot):
            print(f"Le mot {mot} est un palindrome.")
        #sinon on lui indique que le mot saisi n'est pas un palindrome
        else:
            print(f"Le mot {mot} n'est pas un palindrome.")

        #On demande à l'utilisateur s'il souhaite continuer de rentrer des mots
        reponse = input("Voulez-vous continuer ? (O/N)").upper()
        #Tant qu'il répond autre chose que "O"(oui) ou "N"(non), on redemande
        while (reponse != "O") and (reponse != "N"):
            reponse = input("Voulez-vous continuer ? (O/N)").upper()
        #Actualisation de la variable réponse
        continuer = reponse == "O"


#Execution du programme
if __name__ == "__main__":
    main()

