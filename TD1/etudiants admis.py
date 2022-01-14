#TD1 - Exercice 6 - Etudiant

#Initialisation variables
etudiants = {"Boris" : 10, "Bryan" : 12, "Jean" : 5, "Louis" : 18, "Pierre" : 9, "Matthieu" : 7}
etudiantAdmis = {}
etudiantNonAdmis = {}
somme_admis = 0
somme_non_admis = 0

#Rangement et calcul
for etudiant in etudiants :
    if etudiants[etudiant] >= 10 :
        etudiantAdmis[etudiant] = etudiants[etudiant]
        somme_admis += etudiants[etudiant]
    else :
        etudiantNonAdmis[etudiant] = etudiants[etudiant]
        somme_non_admis += etudiants[etudiant]

moyenne_admis = somme_admis / len(etudiantAdmis)
moyenne_non_admis = somme_non_admis / len(etudiantNonAdmis)

print(f"Les etudiants admis sont : {etudiantAdmis} et leur moyenne est {moyenne_admis}")
print(f"Les etudiants non admis sont : {etudiantNonAdmis} et leur moyenne est {moyenne_non_admis}")

