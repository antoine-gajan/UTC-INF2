#Question 4 - Programme qui indique si une année rentrée par l'utilisateur est bissextile

#Indique à l'utilisateur le rôle du programme
print("Question 4 - Programme qui informe si une année est bissextile ou non")

#Demande à l'utilisateur l'année
annee = int(input("Entrez une année : "))

#Vérification si l'année est bissextile ou non
#Une année est bissextile si elle est divisible par 4 mais pas par 100 ou si elle est divisible par 4 et par 400
if (annee % 4 == 0) and ((annee % 100 != 0) or (annee % 400 == 0)) :
    #Informe l'utilisateur que l'année est bissextile
    print(f"L'année {annee} est bissextile.")
else :
    #Informe l'utilisateur que l'année n'est pas bissextile
    print(f"L'année {annee} n'est pas bissextile.")
