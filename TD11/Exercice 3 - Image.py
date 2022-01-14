#Exercice 3 - Image

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


#Image couleur
face_c = misc.face()
#Image sous forme de matrice
image = np.array(face_c)
#Récupérer dimension de l'image
dimension = face_c.shape
#Calcul pour le zoom
x0 = dimension[0]//4
x1 = 3*dimension[0]//4
y0 = dimension[1]//4
y1 = 3*dimension[1]//4
image_zoom = image[x0:x1, y0:y1]
plt.imshow(image_zoom)
plt.title('Image zoomée sans modification')
plt.show()
#Modification de la luminosité des pixels
image_zoom[image_zoom > 200] = 255
image_zoom[image_zoom < 50] = 0
#Affichage de l'image
plt.imshow(image_zoom)
plt.title('Image zoomée avec modification')
plt.show()


#Retour à l'image non zoomée
image_gris = np.array(misc.face(gray=True))
plt.imshow(image_gris, cmap=plt.cm.gray)
plt.title('Image normale en niveau de gris')
plt.show()


#Mise sous forme de tableau 1D
niveau_gris = np.ravel(image_zoom)
#Histogramme des niveaux de gris
plt.hist(niveau_gris, bins=256)
plt.title('Niveau de gris de l\'image non zoomée sans modification')
plt.show()


#Calcul et affichage de la nouvelle image
"""Val est tableau AD qui contient les différentes valeurs possibles de la matrice [0..255]
Nb est un tableaux des occurences de chaque valeur
=> Il y a nb[i] fois la valeur val[i] dans image_zoom

val = [0, 1, 2, 3, 4, ..., 255]
nb = [50, 02, 14, 20, ..., 1]
"""
val, nb = np.unique(image_zoom, return_counts=True)
cumul = np.cumsum(nb)
nb_pixels = sum(nb) #Renvoie la somme des nombres du tableau nb
taille_classe = nb_pixels //4
limite_classe1 = 0

while cumul[limite_classe1] <= taille_classe:
    limite_classe1 += 1

limite_classe2 = limite_classe1 + 1

while cumul[limite_classe2] <= 2*taille_classe:
    limite_classe2 += 1

limite_classe3 = limite_classe2 + 1
while cumul[limite_classe3] <= 3*taille_classe:
    limite_classe3 += 1

#Modification des pixels
for i in range(0, image_zoom.shape[0]):
    for j in range(0, image_zoom.shape[1]):
        pixel = image_zoom[i,j]
        if pixel <= limite_classe1:
            pixel = 0
        elif pixel <= limite_classe2:
            pixel = 84
        elif pixel <= limite_classe3:
            pixel = 168
        else:
            pixel = 255

plt.imshow(image_zoom)
plt.show()
plt.hist(image_zoom.ravel(), 256)








