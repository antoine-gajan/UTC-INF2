#Exercice 1 - Lieux

#Import du module Google Maps
import googlemaps

#Ajout de la classe gmap contenant une fonction permettant de récupérer les coordonnées GPS d'un lieu
class gmap:
    def coordgps(adresse):
        gmaps = googlemaps.Client(key='AIzaSyBY7RDZYuBbD6I8uFPxFdkE55Xx90720b0')
        geocode_result = gmaps.geocode(adresse)
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        return lat,lng


#Création de la classe Lieu
class Lieu():
    #Création du constructeur
    def __init__(self, nom:str, adresse:str):
        "Instancie un objet de la classe Lieu, contenant son nom et son adresse"
        self.__nom = nom
        self.__adresse = adresse
        #Utilisation de la méthode coordgps pour récupérer la latitude et la longitude de l'adresse
        self.__latitude, self.__longitude = gmap.coordgps(self.__adresse)

    #Méthode qui affiche le résultat complet
    def detail(self):
        "Renvoie le résultat en détail des coordonnées du lieu"
        print(f"Nom du lieu : {self.__nom} \n Adresse : {self.__adresse} \n Coordonnées GPS : ({self.__latitude}, {self.__longitude})")

#Programme principal demandant plusieurs lieux à l'utilisateur
def main():
    #Affichage de l'intérêt du programme
    print("Exercice 1 - Lieu avec Google Maps")
    #Initialisation de la variable indiquant si l'utilisateur souhaite continuer de rentrer des lieux
    continuer = True
    #Tant qu'il souhaite continuer
    while continuer:
        #Demande du nom et de l'adresse du lieu
        nom = input("Nom du lieu : ")
        adresse = input("Adresse du lieu :")
        #Création de l'objet lieu associé
        lieu = Lieu(nom, adresse)
        #Affichage du résultat complet
        lieu.detail()
        #Demande à l'utilisateur s'il souhaite continuer et mise à jour de la variable continuer
        reponse = input("Voulez vous continuer ? (O/N) ").upper()
        while reponse != "O" and reponse != "N":
            reponse = input("Voulez vous continuer ? (O/N) ").upper()
        continuer = reponse == "O"

if __name__ == "__main__":
    main()


