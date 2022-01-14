#TP1 - Programme qui demande 2 nombres à l'utilisateur et l'informe ensuite si leur produit est positif ou négatif

#Indique à l'utilisateur le rôle du programme
print("Question 2 - Indique si le produit de 2 nombres est positif ou négatif")

#Demande des 2 nombres à l'utilisateur
a = float(input("Entrez le 1er nombre : "))
b = float(input("Entrez le 2ème nombre : "))

#Informe l'utilisateur si le produit est positif, nul ou négatif
if (a*b) > 0 : #si c'est positif
    print(f"Le produit de {a} par {b} est positif.")
elif (a*b) == 0 : #on considère 0 comme une valeur particulière
    print(f"Le produit de {a} par {b} est nul.")
else : #sinon c'est négatif
    print(f"Le produit de {a} par {b} est négatif.")