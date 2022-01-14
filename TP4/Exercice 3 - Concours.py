#Exercice 3 - Concours

#Import de la librairie matplotlib
import matplotlib.pyplot as plt

def saisir() -> None:
    "Remplit les données relatives aux candidats dans le fichier concours.txt"
    #Ouverture du fichier en mode "ajout" pour permettre d'ajouter des candidats en plusieurs appels de la fonction
    with open('concours.txt', 'a') as fichier:
        #Variable indiquant que l'utilisateur souhaite continuer d'inscrire des candidats
        continuer = True
        #Tant que l'utilisateur souhaite continuer
        while continuer:
            #Nouveau candidat
            print("Nouveau candidat : ")
            #Demande du NCIN du candidat
            ncin = input("NCIN : ")
            #Demande du nom
            nom = input("Nom : ")
            #Demande du prénom
            prenom = input("Prénom : ")
            #Demande de l'âge et test de sa validité
            age = int(input("Age : "))
            if age <= 0:
                raise ValueError("L'âge doit être un entier strictement positif.")
            #Demande de la décision et test de sa validité
            decision = input("Décision (admis/refusé/ajourné): ").lower()
            while decision not in ('admis', 'refusé', 'ajourné'):
                decision = input("Erreur. Veuillez entrer une décision valide. \n Décision (admis/refusé/ajourné): ").lower()
            #Ecriture du candidat dans le fichier
            fichier.write(f"{ncin};{nom};{prenom};{age};{decision}\n")
            #Demande à l'utilisateur s'il souhaite continuer
            reponse = input("Voulez-vous ajouter un nouveau candidat ? (O/N) ").upper()
            #Tant que la réponse n'est pas un 'O' ou un 'N', on redemande
            while reponse != 'O' and reponse != 'N':
                reponse = input("Erreur. Voulez-vous ajouter un nouveau candidat ? (O/N) ")
            #Mise à jour de la variable 'continuer'
            continuer = reponse == 'O'

def admis() -> None:
    "Stocke les données relatives aux candidats admis"
    #Ouverture du fichier concours.txt en mode "lecture"
    with open('concours.txt', 'r') as candidats:
        #Ouverture du fichier admis.txt en mode écriture
        with open('admis.txt', 'w') as admis:
            #Pour chaque candidat au concours
            for candidat in candidats:
                #Extraction des informations relatives au candidat
                donnees = candidat.strip('\n')
                donnees = donnees.split(';')
                #S'il est admis, on l'ajoute au fichier admis.txt
                if donnees[4] == 'admis':
                    admis.write(candidat)

def attente() -> None:
    "Stocke les candidats admis et âgés de plus de 30 ans"
    #Ouverture en lecture du fichier admis.txt
    with open('admis.txt', 'r') as admis:
        #Ouverture du fichier attente.txt en écriture
        with open('attente.txt', 'w') as attente:
            #Pour chaque candidat admis
            for candidat in admis:
                #Extraction des informations relatives au candidat
                donnees = candidat.strip('\n')
                donnees = donnees.split(';')
                #Si son âge est supérieur ou égal à 30, on le place sur liste d'attente
                if int(donnees[3]) >= 30:
                    attente.write(candidat)

def statistiques(dec:str) -> float:
    "Retourne le pourcentage de candidats pour la décision"
    #Test si la décision placée en paramètre existe
    if dec not in ('admis', 'refusé', 'ajourné'):
        raise ValueError("Décision invalide.")
    #Initialisation à 0 de la variable indiquant le nombre de candidats ayant la decision placée en paramètre
    nb_dec = 0
    #Initialisation à 0 de la variable indiquant le nombre total de candidats inscrits au concours
    nb_candidats = 0
    #Ouverture du fichier concours.txt en lecture
    with open('concours.txt', 'r') as candidats:
        #Boucle pour chaque candidat inscrit
        for candidat in candidats:
            #Incrémentation du compteur de candidats
            nb_candidats += 1
            #Extraction des données du candidat
            donnees = candidat.strip('\n')
            donnees = donnees.split(';')
            #Si la décision correspond à celle placée en paramètre
            if donnees[4] == dec:
                #On incrémente le nombre de 1
                nb_dec += 1
    #Calcul du pourcentage
    pourcentage = nb_dec / nb_candidats * 100
    #Retourne le pourcentage de candidats pour la décision
    return pourcentage

def trace_camembert() -> None:
    "Affichage du camembert correspondant aux résultats du concours"
    #Récupération des pourcentages pour créer le camembert
    pourcentage_admis = statistiques('admis')
    pourcentage_refuse = statistiques('refusé')
    pourcentage_ajourne = statistiques('ajourné')
    #Création d'un tableau contenant les valeurs du camembert
    donnees = [pourcentage_admis, pourcentage_refuse, pourcentage_ajourne]
    #Création d'un tableau avec les étiquettes à placer sur le camembert
    etiquettes = [f"Admis\n({pourcentage_admis:2.2f}%)", f"Refusé\n({pourcentage_refuse:2.2f}%)", f"Ajourné\n({pourcentage_ajourne:2.2f}%)"]
    #Création d'un tableau avec les couleurs
    couleurs = ['orange', 'purple', 'blue']
    #Création du camembert
    plt.pie(donnees, labels=etiquettes, colors=couleurs, labeldistance=1.15, normalize=True)
    #Ajout d'un titre
    plt.title("Exercice 3 - Résultat au concours", fontweight='bold', color='b', pad='15')
    #Mise en place de la légende
    plt.legend(['Admis', 'Refusé', 'Ajourné'])
    #Affichage du camembert
    plt.show()
    #Fermeture du graphique
    plt.close()

def supprimer() -> None:
    "Supprime du fichier admis.txt les candidats de plus de 30 ans"
    #Ouverture du fichier admis.txt en lecture
    with open('admis.txt', 'r') as admis:
        #Récupération de l'ensemble des candidats
        candidats = admis.readlines()
    #Ouverture du fichier admis.txt en écriture
    with open('admis.txt', 'w') as admis:
        #Pour chaque candidat admis
        for candidat in candidats:
            # Extraction des informations relatives au candidat
            donnees = candidat.strip('\n')
            donnees = donnees.split(';')
            #Si son âge est inférieur à 30, on le ré-ajoute au fichier des admis
            if int(donnees[3]) < 30:
                admis.write(candidat)

#Programme principal
def main():
    #Saisie des candidats
    saisir()
    #Création du fichier avec les admis
    admis()
    #Création du fichier avec les admis en attente
    attente()
    #Affichage du camembert
    trace_camembert()
    #Suppression des personnes âgées de plus de 30 ans au fichier des admis
    supprimer()

if __name__ == '__main__':
    main()