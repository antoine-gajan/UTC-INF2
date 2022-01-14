#Question 3 - Programme qui calcule le factoriel d'un entier donné par l'utilisateur

#Indique à l'utilisateur le rôle du programme
print("Question 3 - Calcul du factoriel d'un entier")

#Demande à l'utilisateur le nombre dont il souhaite connaître le factoriel
n = int(input("Entrez un nombre entier positif : "))

if n < 0 : #si le nombre est strictement négatif, le programme s'arrête et indique à l'utilisateur pourquoi
    print(f"Vous avez rentré {n} qui est un entier négatif. Il est impossible de calculer son factoriel.")
else : #si le nombre est valide, calcul du factoriel
    #Initialisation de la variable factoriel à 1
    factoriel = 1

    #Boucle pour calculer le factoriel car factoriel(n) = 1 * 2 * 3 *...* n
    for i in range(1, n+1) :
        factoriel = factoriel * i

    #Affichage du résultat du factoriel
    print(f"Le factoriel de {n} est {factoriel}")