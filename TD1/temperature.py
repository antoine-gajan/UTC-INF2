#TD 1 - Exercice 3 - Température

#Initialisation de la température
temp = int(input("Entrez la température 1 : "))
min = temp
max = temp
proche0 = temp

#Boucle
for i in range(2, 13):
    temp = int(input(f"Entrez la valeur {i} : "))
    if temp < min :
        min = temp
    elif temp > max :
        max = temp
    elif abs(temp) < abs(proche0) :
        proche0 = temp
    elif abs(temp) == abs(proche0):
        proche0 = min(proche0, temp)

#Affichage des résultats
print(f"La température minimale est : {min}")
print(f"La température maximale est : {max}")
print(f"La température la plus proche de 0 est : {proche0}")
