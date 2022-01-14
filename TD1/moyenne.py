#TD1 - Moyenne

N = int(input("Nombre de valeurs que vous voulez entrer : "))
somme = 0
tab = []
for i in range(N):
    val = int(input(f"Valeur {i} : "))
    tab.append(val)
    somme += val

moyenne_arithmetique = somme / N
print(f"La moyenne arithmétique est : {moyenne_arithmetique}")

moyenne_olympique = (somme - min(tab) - max(tab)) / (N-2)
print(f"La moyenne olympique est : {moyenne_olympique}")
