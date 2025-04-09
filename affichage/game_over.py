from module.fltk import *
import time


def game_over(plateau, hauteurFenetre, largeurFenetre, taille_carre, rectangle_x, rectangle_y):
    """
    Affiche un écran de "GAME OVER" avec un effet visuel et attend un clic avant de revenir à l'état normal.

    :param plateau: Liste représentant l'état actuel du plateau de jeu, utilisé pour dessiner chaque case.
    :param hauteurFenetre: Hauteur de la fenêtre de jeu en pixels.
    :param largeurFenetre: Largeur de la fenêtre de jeu en pixels.
    :param taille_carre: Taille des cases du plateau de jeu, utilisée pour dessiner les rectangles.
    :param rectangle_x: Position X du coin supérieur gauche du plateau sur l'écran.
    :param rectangle_y: Position Y du coin supérieur gauche du plateau sur l'écran.
    """


    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            rectangle(
                (taille_carre * j) + rectangle_x, 
                (taille_carre * i) + rectangle_y, 
                (taille_carre * j) + taille_carre + rectangle_x, 
                (taille_carre * i) + taille_carre + rectangle_y,
                remplissage = '#111111',
                couleur = '#FF00FF'
            )
            time.sleep(0.01)
            mise_a_jour() #on met a jour le plateau

    texte(
            largeurFenetre // 2,
            hauteurFenetre // 2,
            "GAME OVER",
            ancrage="center",
            couleur="white",
            police = "Fixedsys",
            taille = 40,
            tag = 'game_over'
        )
    
    attend_clic_gauche()
    efface('game_over')
    efface('fond')
    
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            rectangle(
                (taille_carre * j) + rectangle_x, 
                (taille_carre * i) + rectangle_y, 
                (taille_carre * j) + taille_carre + rectangle_x, 
                (taille_carre * i) + taille_carre + rectangle_y,
                remplissage = '#111111',
                couleur = '#111111'
            )
            time.sleep(0.01)
            mise_a_jour() #on met a jour le plateau
