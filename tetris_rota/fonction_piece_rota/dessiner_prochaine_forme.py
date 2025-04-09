from module.fltk import *


def forme(x_start, y_start, piece,couleur_piece, taille_carre,tag_1):

    """
    Dessine la pièce dans la case prochaine_piece à partir de ses coordonnées de départ, de la forme de la pièce,
    de sa couleur et de la taille d'un carrés.

    La fonction parcourt la matrice représentant la pièce et dessine un carré pour chaque cellule occupée par la pièce. 

    :param x_start: La position en x (coordonnée horizontale) où la pièce commence à être dessinée.
    :param y_start: La position en y (coordonnée verticale) où la pièce commence à être dessinée.
    :param piece: Une matrice représentant la forme de la pièce.
    :param couleur_piece: La couleur de la pièce qui sera utilisée pour remplir les cases dessinées.
    :param taille_carre: La taille du carré qui représente chaque partie de la pièce sur le plateau.
    """
    efface(tag_1)
    for i in range(len(piece)):
        x_a = x_start
        y_a = y_start + i * taille_carre
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                x_b = x_a + taille_carre
                y_b = y_a + taille_carre
                rectangle(x_a, y_a, x_b, y_b, remplissage=couleur_piece,tag = tag_1)
            x_a += taille_carre