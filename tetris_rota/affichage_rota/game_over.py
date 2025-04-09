from module.fltk import *
import time
from math import sqrt


def game_over(plateau, hauteurFenetre, largeurFenetre):
    """
    Affiche un écran de "GAME OVER" avec un effet visuel et attend un clic avant de revenir à l'état normal.

    :param plateau: Liste représentant l'état actuel du plateau de jeu, utilisé pour dessiner chaque case.
    :param hauteurFenetre: Hauteur de la fenêtre de jeu en pixels.
    :param largeurFenetre: Largeur de la fenêtre de jeu en pixels.
    :param taille_carre: Taille des cases du plateau de jeu, utilisée pour dessiner les rectangles.
    :param rectangle_x: Position X du coin supérieur gauche du plateau sur l'écran.
    :param rectangle_y: Position Y du coin supérieur gauche du plateau sur l'écran.
    """

    rectangle_x = largeurFenetre * 0.02
    a,b = (rectangle_x,hauteurFenetre * 0.5), (hauteurFenetre*0.27,hauteurFenetre*0.25)
    calcule_longeur_coter = int(sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2)))
    taille_carre = calcule_longeur_coter / (len(plateau[0]))
    moitier_diagonal_carre = (sqrt(2) * taille_carre)/2

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):

            rectangle_x = largeurFenetre * 0.02
            rectangle_x += moitier_diagonal_carre * j
            rectangle_y = hauteurFenetre * 0.5
            rectangle_y += moitier_diagonal_carre * i
            
            polygone([(rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre)),
                    
                    (moitier_diagonal_carre + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre) - moitier_diagonal_carre),
                    
                    (moitier_diagonal_carre * 2 + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre)),
                    
                    (moitier_diagonal_carre + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre) + moitier_diagonal_carre)], 
                    
                    remplissage='#111111',
                    couleur = '#FF00FF')

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

            rectangle_x = largeurFenetre * 0.02
            rectangle_x += moitier_diagonal_carre * j
            rectangle_y = hauteurFenetre * 0.5
            rectangle_y += moitier_diagonal_carre * i
            
            polygone([(rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre)),
                    
                    (moitier_diagonal_carre + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre) - moitier_diagonal_carre),
                    
                    (moitier_diagonal_carre * 2 + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre)),
                    
                    (moitier_diagonal_carre + rectangle_x + (i * moitier_diagonal_carre),
                    rectangle_y - (j * moitier_diagonal_carre) + moitier_diagonal_carre)], 
                    
                    remplissage='#111111',
                    couleur = '#111111')
            
            time.sleep(0.01)
            mise_a_jour() #on met a jour le plateau
