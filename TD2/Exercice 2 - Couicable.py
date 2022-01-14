#TD 2 - Nombre couicable

def sommeChiffre(nb):
    "Retourne la somme des chiffres composant ce nombre"
    somme = 0
    for chiffre in str(nb):
        somme += int(chiffre)
    return somme

"""def sommeChiffre(nb):
    somme = 0
    while nb != 0 :
        somme += nb%10 #nb%10 est le dernier chiffre de nb
        nb = nb//10 #enlève le dernier chiffre de nb
    return somme """

def nombreChiffres(nb):
    "Retourne le nombre de chiffres composant un nombre"
    return len(str(nb))

def sommeChiffres(*args):
    "Retourne la somme d'une liste de nombres"
    somme = 0
    for nombre in args:
        somme += nombre
    return nombre

def test_nombre_chiffres_pair(fonction):
    def wrapper(nb):
        if nombreChiffres(nb) % 2 == 0 :
            return fonction(nb)
        else :
            return 0,0
    return wrapper


@test_nombre_chiffres_pair
def separeNombres(nb):
    "Sépare un nombre en 2 parties"
    taille = nombreChiffres(nb)
    if taille%2 != 0 :
        return 0,0
    else :
        position_milieu = taille//2
        partieGauche = int(str(nb)[:position_milieu])
        partieDroite = int(str(nb)[position_milieu:])
    return(partieGauche, partieDroite)

def sommeChiffres_recursif(nb):
    if nb == 0 :
        return 0 #si le nombre vaut 0, sa somme vaut 0
    else:
        return sommeChiffres_recursif(nb//10) + nb % 10 #sinon, on enleve le dernier chiffre et on somme les derniers nombres

def couicable(n):
    n = int(input("Entrez un nombre : "))
    partieGauche, partieDroite = separeNombres(nb)
    if ((nombreChiffres(n) % 2 == 0)) and (sommeChiffre(partieGauche) == sommeChiffre(partieDroite)):
        return True
    else:
        return False
