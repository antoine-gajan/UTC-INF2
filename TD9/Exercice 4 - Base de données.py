#Exerice 4 - Base de données
import sqlite3

#Fonction pour effectuer une requête
def requete(req):
    bdd = sqlite3.connect("BDD-exo4.sqlite")
    #Obtenir un curseur (tampon)
    #Plutot que de modifier direct la BDD, on utilise un tampon (mémoire temporaire) pour faire des modifs et les appliquer uniquement si on est sûr de ce qu'on écrit
    curseur = bdd.cursor()
    try :
        #Executer la requete
        curseur.execute(req)
    except:
        print(f"Requête incorrecte !")
    else:
        #Affichage de résultat
        for enregistrement in curseur:
            print(enregistrement)
        #Appliquer toutes les modifs sur la BDD réelle
        bdd.commit()
        #Fermer la connexion
        bdd.close()

#Modification de la BDD avec les requêtes
requete("SELECT * FROM client")
print()
requete("SELECT numero FROM numero_telephone WHERE client_id = 1")
print()
requete("SELECT client.nom, prenom, ville.nom FROM client INNER JOIN ville ON client.ville_id = ville.ID")
print()
requete("SELECT client.nom, prenom FROM client INNER JOIN ville ON ville.ID = client.ville_id WHERE code_departement = 60")
print()
requete("""SELECT c.nom, c.prenom FROM client AS c INNER JOIN numero_telephone AS n ON 
n.client_id = c.ID WHERE c.ID not in (SELECT c.ID FROM client AS c
INNER JOIN numero_telephone AS n ON n.client_id = c.ID WHERE est_demarche = true)""")
print()
requete("""SELECT c.nom, c.prenom, n.numero FROM client AS c INNER JOIN numero_telephone 
AS n ON c.ID = n.client_ID INNER JOIN operateur AS o on o.ID = n.operateur_id WHERE o.nom = 'SuperTelecom'""")
print()
requete("""SELECT c.nom, c.prenom, o.nom, n.numero FROM client AS c INNER JOIN numero_telephone as n ON n.client_id = c.ID
LEFT JOIN operateur AS o ON n.operateur_id = o.ID""")
print()
requete("""INSERT INTO ville VALUES (NULL, 'Marquise', '62', '62250', '62560', '5200')""")
print()
requete("""DELETE FROM ville WHERE code_postal = '60521'""")
print()
requete("""UPDATE numero_telephone SET est_demarche = 1 WHERE numero = '0311223344'""")
print()
requete("""UPDATE numero_telephone SET operateur_id = 4 WHERE numero = '0311223344'""")
print()
requete("""UPDATE numero_telephone SET operateur_id = (SELECT ID FROM operateur WHERE nom = 'Supertelecom')""")
print()
requete("""DELETE FROM CLIENT WHERE id = '1'""")
