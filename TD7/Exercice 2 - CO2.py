#Exercice 2 - Emission de C02
import csv
from affichage_graphique import *
import pandas as pd

def creation_liste_csv(nom_fichier:str):
    with open(nom_fichier, 'r') as nom_fichier:
        data = csv.reader(nom_fichier, delimiter=',')
        for ligne in data:
            print(ligne)

def extraire_listes_csv(nom_fichier:str):
    annees = []
    CO2 = []
    with open(nom_fichier, 'r') as nom_fichier:
        data = csv.reader(nom_fichier,  delimiter = ',')
        next(data, None)
        for ligne in data:
            annee = int(ligne[0].split('-')[0])
            annees.append(annee)
            CO2.append(float(ligne[1]))
    return annees, CO2

def affiche_csv(x_values, y_values):
    affiche_courbe(x_values, y_values, "Exercice 2", "Annees", "Moyenne")

def creation_liste_pd(nom_fichier:str):
    with open(nom_fichier, 'r') as nom_fichier:
        data = pd.read_csv(nom_fichier, sep = ",", usecols=["Year", "Mean"])
        print(data)

def extraire_listes_pd(nom_fichier:str):

    with open(nom_fichier, 'r') as nom_fichier:
        data = pd.read_csv(nom_fichier,  sep = ',')
        annees = [int(annee[0:4]) for annee in data['Year'].to_list()]
        CO2 = [float(mean) for mean in data['Mean'].to_list()]
    return annees, CO2

def affiche_pd(x_values, y_values):
    affiche_courbe(x_values, y_values, "Exercice 2", "Annees", "Moyenne")

def main():
    creation_liste_pd("co2-annmean-mlo.csv")
    x_values, y_values = extraire_listes_pd("co2-annmean-mlo.csv")
    affiche_pd(x_values, y_values)

if __name__ == "__main__":
    main()