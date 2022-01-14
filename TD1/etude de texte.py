#TD1 - Etude de texte

texte = input("Entrez un texte : ")

def retourne2(couple):
    return couple(1)

#Initialisation des variables
nb_car = 0
nb_lettres = 0
nb_voyelles = 0
nb_chiffres = 0
dico_lettres = dict([(chr(x),0) for x in range(ord('a'), ord('z')+1)])
freq = []

#Calculs pour l'étude du texte
for car in texte.lower() :
    nb_car += 1
    if ("a" <= car) and (car <= "z") :
        nb_lettres += 1
        if car in ('a', 'e', 'i', 'o', 'u', 'y') :
            nb_voyelles += 1
        dico_lettres[car] += 1
    elif ("0"<=car) and (car<="9") :
        nb_chiffres += 1

#Calcul de la fréquence
freq = [(lettre, nb/nb_lettres*100) for lettre, nb in dico_lettres.keys()]
freq.sort(key=retourne2, reverse=True)

#Affichage des résultats
print(f"Nombre de caractères : {nb_car}")
print(f"Nombre de lettres : {nb_lettres}")
print(f"Nombre de voyelles : {nb_voyelles}")
print(f"Nombre de chiffres : {nb_chiffres}")
print("------------------------------")
for couple in freq :
    print(f"Fréquence de {couple(0)} = {couple(1)} % ")
print("------------------------------")

