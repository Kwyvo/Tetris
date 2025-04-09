from module.fltk import *
from composant.boutons import *
import time


def animation_play(hauteurFenetre, largeurFenetre, score, niveau, compteur_ligne):

    """
    Affiche l'animation d'introduction du jeu Tetris avec un plateau, la zone de la prochaine pièce,
    le score, le niveau, et le nombre de lignes complétées.

    Elle dessine :
    - Le plateau de jeu avec une bordure.
    - Une zone pour afficher la prochaine pièce.
    - Des informations de jeu telles que le score, le niveau et le nombre de lignes complétées.
    - Les cases du plateau avec un léger délai pour créer un effet d'animation.

    :param hauteurFenetre: Hauteur de la fenêtre de jeu en pixels.
    :param largeurFenetre: Largeur de la fenêtre de jeu en pixels.
    :param score: Score actuel du joueur, un entier.
    :param niveau: Niveau actuel du jeu, un entier.
    :param compteur_ligne: Nombre de lignes complétées par le joueur, un entier.
    """

    efface_tout()
    plateau = [[0 for i in range(10)] for j in range(20)]

    #---------------------------------------------------PLATEAU-----------------------------------------------------
    # Dimensions du plateau
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    # Calculer la taille d'un carré
    hauteur_boite = (hauteurFenetre*0.97) - (hauteurFenetre * 0.03)
    largeur_boite = (largeurFenetre* 0.57) - (largeurFenetre * 0.03)
    taille_carre = min(hauteur_boite / nb_lignes, largeur_boite / nb_colonnes)

    # Calculer les dimensions du plateau
    rectangle_x = largeurFenetre * 0.03
    rectangle_y = hauteurFenetre * 0.03
    rectangle_largeur = taille_carre * nb_colonnes
    rectangle_hauteur = taille_carre * nb_lignes

    # Dessiner le rectangle du plateau
    rectangle(rectangle_x, rectangle_y, rectangle_x + rectangle_largeur, rectangle_y + rectangle_hauteur, remplissage = '#111111', epaisseur = 0)

    rectangle(rectangle_x - 10, rectangle_y-10, rectangle_x + rectangle_largeur+10, rectangle_y + rectangle_hauteur +10, couleur = '#FF00FF')

   
    #---------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------DESSIN PROCHAINE PIECE------------------------------------------
    # Zone pour afficher la prochaine pièce
    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.03, largeurFenetre * 0.97, hauteurFenetre * 0.37, remplissage = '#111111',couleur = '#FF00FF')
    #---------------------------------------------------------------------------------------------------------------

    #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
    debut_rectangle_hauteur = hauteurFenetre * 0.40
    for i in range(3):
        rectangle(largeurFenetre * 0.55,debut_rectangle_hauteur, largeurFenetre * 0.97, debut_rectangle_hauteur+hauteurFenetre*0.10, remplissage = '#111111', couleur = '#FF00FF')
        debut_rectangle_hauteur += hauteurFenetre*0.10

    taille_txt = int(10 * (hauteurFenetre*0.0025))
    texte(largeurFenetre * 0.57, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:{score}",police = "Press Start 2P",taille = taille_txt,couleur = 'white') #score

    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:{niveau}",police = "Press Start 2P", taille = taille_txt,couleur = 'white')

    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:{compteur_ligne}",police = "Press Start 2P", taille = taille_txt,couleur = 'white')

    #---------------------------------------------------------------------------------------------------------------

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            rectangle(
                (taille_carre * j) + rectangle_x, 
                (taille_carre * i) + rectangle_y, 
                (taille_carre * j) + taille_carre + rectangle_x, 
                (taille_carre * i) + taille_carre + rectangle_y,
                couleur = 'gray5'
            )
            time.sleep(0.01)
            mise_a_jour() #on met a jour le plateau