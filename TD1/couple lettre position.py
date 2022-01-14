#INF2 - TD1- Exercice 7

noms = ["Bryan", "Boris", "Jean", "Brandon", "Louise", "Véronique"]

dico = {}

for nom in noms :
    for i in range(len(nom)):
        if (i, nom[i].lower()) in dico.keys():
            dico[(i, nom[i].lower())].append(nom)
        else:
            dico[(i, nom[i].lower())] = [nom]

position = int(input("Entrez la position : "))
lettre = input("Entrez la lettre : ").lower()

couple = (position, lettre)
print(f"Les noms comportant la lettre {lettre} en {position} ème position est : {dico[couple]}")