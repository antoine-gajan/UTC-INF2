#Exercice 2 - Cryptage d'un mot en décalant les lettres pour le rendre illisible

def crypter(ch:str) -> str:
    "Retourne une chaine cryptée"
    #Intialisation de la nouvelle chaine cryptée à vide
    crypte = ""
    #On parcourt chaque caractère de la chaine
    for caractere in ch:
        #on teste si le caractère est bien une lettre de l'alphabet
        if (caractere >= "A") and (caractere <= "z"):
            #cas particulier : si la lettre est Z, on la remplace par A (en conservant majuscule et minuscule)
            if caractere == "Z" or caractere == "z":
                crypte += chr(ord(caractere) + ord("A") - ord("Z"))
            #cas normal : on remplace par la lettre qui suit
            else:
                crypte += chr(ord(caractere) + 1)
        #si le caractère n'est pas une lettre, on le laisse tel quel
        else:
            crypte += caractere
    return crypte

def main():
    #Affiche le rôle du programme
    print("Exercice 2 - Cryptage d'une chaine de caractères")

    # Initialisation de la variable continuer qui indique si l'utilisateur souhaite continuer ou non
    continuer = True
    while continuer:
        # Le programme demande un mot à l'utilisateur
        chaine = (input("Entrez une chaine de caractères : "))
        print(f"La chaine cryptée est {crypter(chaine)}")

        # On demande à l'utilisateur s'il souhaite continuer de rentrer des chaines de caractères
        reponse = input("Voulez-vous continuer ? (O/N)").upper()
        # Tant qu'il répond autre chose que "O"(oui) ou "N"(non), on redemande
        while (reponse != "O") and (reponse != "N"):
            reponse = input("Voulez-vous continuer ? (O/N)").upper()
        # Actualisation de la variable réponse
        continuer = reponse == "O"

if __name__ == "__main__":
    main()