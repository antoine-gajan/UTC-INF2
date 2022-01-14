#TD 2 - Carré magique

def somme_ligne(mat, i):
    somme = 0
    for nombre in mat[i]:
        somme += nombre
    return somme
    #2eme solution : return sum([mat[i][j] for j in range(len(mat))])
    #3eme solution : return sum(mat[i])

def somme_colonne(mat, i):
    somme = 0
    for j in range(len(mat)):
        somme += mat[j][i]
    return somme

def somme_diag1(mat):
    somme = 0
    for i in range(len(mat)):
        somme += mat[i][i]
    return somme

def somme_diag2(mat):
    somme = 0
    for i in range(len(mat)):
        somme += mat[i][len(mat)-1-i]
    return somme

def magique(mat_c):
    "Renvoie si une matrice carré est magique"
    #Initialisation de la valeur de référence
    ref = somme_ligne(mat_c, 0)
    #Test des lignes
    for i in range(len(mat_c)):
        if somme_ligne(mat_c, i) != ref :
            return False

   #Test colonne si test ligne est valide
    for i in range(len(mat_c)):
        if somme_colonne(mat_c, i) != ref :
            return False

    #Test diagonales si test lignes et colonnes valide
    if somme_diag1(mat_c) == somme_diag2(mat_c) == ref:
        return True
    return False


def carre_magique_normal(mat_c):
    i = 0
    l = [i for i in range(1, len(mat_c)**2 + 1)]
    normal = True
    while i < (len(mat_c)) and normal:
        j = 0
        while j < (len(mat_c)) and normal:
            if (mat_c[i][j] < 1) or (mat_c[i][j] > len(mat_c)**2):
                normal = False
            else:
                if mat_c[i][j] in l:
                    l.remove(mat_c[i][j])
                    j += 1
                else:
                    normal = False
        i += 1
    if len(l) == 0:
        return True
    return False


def affiche_test_cm(*args):
    for mat in args:
        if magique(mat):
            if carre_magique_normal(mat):
                print(f"{mat} est un carré magique normal")
            else :
                print(f"{mat} est un carré magique")
        else :
            print(f"{mat} n'est pas un carré magique")

C1= [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
C2 = [[21,7,17],[11,15,19],[13,23,9]]

affiche_test_cm(C1, C2)