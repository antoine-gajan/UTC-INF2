#Exercice 1 - MyNotes
import os.path, PIL

class Note():
    def __init__(self, titre:str):
        self.titre = titre

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre:str):
        if isinstance(titre, str):
            self.__titre = titre
        else:
            raise TypeError("Le titre doit être une chaîne de caractères.")

    def print(self):
        print(f"{self.titre}")

class Article(Note):
    def __init__(self, titre:str, texte:str):
        super().__init__(titre) #Représente la partie Note, équivalent à Note.__init__(self, titre)
        self.texte = texte

    @property
    def texte(self):
        return self.__texte

    @texte.setter
    def texte(self, texte:str):
        if isinstance(texte, str):
            self.__texte = texte
        else:
            raise TypeError("Le texte doit être une chaîne de caractères.")

    def print(self):
        super().print()
        print(f"{self.texte}")

class Image(Note):
    def __init__(self, titre:str, description:str, fichier:str):
        super().__init__(titre) #Note.__init__(self, titre)
        self.description = description
        self.fichier = fichier

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description:str):
        if isinstance(description, str):
            self.__description = description
        else:
            raise TypeError("La description doit être une chaîne de caractères.")

    @property
    def fichier(self):
        return self.__fichier

    @fichier.setter
    def fichier(self, fichier:str):
         if os.path.isfile(fichier):
             self.__fichier = fichier
         else:
             raise OSError("Le chemin du fichier doit être une chaîne de caractères.")

    def print(self):
        super().print()
        print(self.description)
        img = PIL.Image.open(self.fichier)
        img.show()

class Document(Note):
    def __init__(self, titre):
        super().__init__(titre)
        self.__grp_notes = []

    def ajouter_note(self, note:Note):
        if isinstance(note, Note):
            self.__grp_notes.append(note)
        else:
            raise TypeError("La note doit être de type Note.")

    def supprimer_note(self, note:Note):
        if isinstance(note, Note):
            if note in self.__grp_notes:
                self.__grp_notes.remove(note)
            else:
                raise ValueError("La note saisie n'est pas dans le document. Impossible de la supprimer.")
        else:
            raise TypeError("La note rentrée n'est pas de type Note.")

    def print(self):
        super().print()
        for note in self.__grp_notes:
            note.print()

    def __iter__(self):
        "Initialise la séquence d'itération et renvoie l'objet"
        self.__nb = 0 #Initialise le nombre d'itérations
        return self

    def __next__(self):
        "Avance dans la séquence d'itération et renvoie la note courante"
        if self.__nb < len(self.__grp_notes): #s'il reste des objets
            elt = self.__grp_notes[self.__nb]
            self.__nb += 1 #Incrémentation du conteur
            return elt #Renvoie l'objet courant
        else:
            raise StopIteration #s'il n'y a plus d'éléments, fin de la séquence

#Programme principal
def main():
    mon_document = Document("Titre du document")
    note1 = Article("Choses à faire", "- Aller à l'école \n - Faire les courses")
    note2 = Note("Note")
    mon_document.ajouter_note(note1)
    mon_document.ajouter_note(note2)
    mon_document.print_document()
    mon_document.supprimer_note(note2)
    mon_document.print_document()

if __name__ == "__main__":
    main()
