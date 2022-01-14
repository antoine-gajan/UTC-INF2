#Exercice 1 - Matrince n*m aléatoire

import numpy as np

def matrice_aleatoire(n:int, m:int):
    mat = np.random.random((n, m))
    un = np.ones((n, 1))
    mat = np.hstack((mat, un))
    print(mat)


if __name__ == "__main__":
    matrice_aleatoire(2,2)
