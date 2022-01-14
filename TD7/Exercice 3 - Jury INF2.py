#Exercice 3 - Jury de INF2

import pandas as pd

def moyenne(nom_fichier:str):
    "Ajoute la colonne moyenne"
    data = pd.read_csv(nom_fichier, sep=";")
    data['moyenne'] = data['median'] * 0.3 + data['TP'] * 0.25 + data['final'] * 0.45
    #Ascending pour trier par ordre décroissant
    #Inplace pour modifier le dataframe lui-même au lieu d'en renvoyer un nouveau
    data.sort_values(by='moyenne', ascending=False, inplace=True)
    #Pour ne pas avoir les indices 0,1,2,... comme dans le dataFrame
    data.to_csv("Jury-INF2.csv", sep=";", index=False)

def resultat(ligne):
    "Fonction qui détermine le résultat à l'UV de l'élève"
    median = ligne['median']
    final = ligne['final']
    tp = ligne['TP']
    moyenne = ligne['moyenne']
    if ligne.isnull().values.any():
        return "_ABS"
    if float(final) < 6 or float(moyenne) < 10:
        return "F"
    if float(moyenne) >= 10 and float(moyenne) < 11:
        return "E"
    if float(moyenne) >= 11 and float(moyenne) < 13:
        return "D"
    if float(moyenne) >= 13 and float(moyenne) < 15:
        return "C"
    if float(moyenne) >= 15 and float(moyenne) < 17:
        return "B"
    else:
        return "A"

def jury_final():
    data = pd.read_csv("Jury-INF2.csv", sep=";")
    data['résultat'] = data.apply(resultat, axis=1)
    data.to_csv("Jury-INF2.csv", sep=';', index=False)


moyenne("notes.csv")
jury_final()