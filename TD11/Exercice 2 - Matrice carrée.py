#Exercice 2 - Matrince carrée

import numpy as np

def matice_caree():
    #Matrice avec distribution centrée en 0
    R = np.random.normal(0, size=(2,2))
    print(f"R : {R}")
    print(f"Rt : {R.T}")
    #Calcul de M
    M = R.dot(R.T)
    print(f"M : {M}")
    #Calcul de l'inverse de M
    Minv = np.linalg.inv(M)
    print(f"Inverse de M : {Minv}")
    #Calcul du produit M par l'inverse de M
    result1 = M.dot(Minv)
    print(f"M.M-1 : {result1}")
    #Verification si le résultat correspond à celui attendu
    verif = np.allclose(result1, np.eye(2))
    print(verif)

def main():
    matice_caree()

if __name__ == '__main__':
    main()