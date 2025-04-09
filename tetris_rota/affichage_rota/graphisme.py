from module.fltk import *
from fonction_piece.dessiner_prochaine_forme import forme
from affichage.game_over import game_over


def dessin_plateau(plateau_i,x,y,rectangle_largeur,rectangle_hauteur,largeurFenetre):
    if plateau_i == 1:
        rectangle(x, y, x + rectangle_largeur, y + rectangle_hauteur, remplissage = '#111111', epaisseur = 0)
        rectangle(x - 10, y-10, x + rectangle_largeur+10, y + rectangle_hauteur +10, couleur = '#FF00FF')

    else:
        rectangle(largeurFenetre*0.48+x, y, largeurFenetre*0.48+x + rectangle_largeur, y + rectangle_hauteur, remplissage = '#111111', epaisseur = 0)
        rectangle(largeurFenetre*0.48+x - 10,y-10, largeurFenetre*0.48+x + rectangle_largeur+10, y + rectangle_hauteur +10, couleur = '#FF00FF')

def recuperer_tag(c):
    l = []
    for i in range(len(c)):
        if c[i] != []:
            l.append(c[i][0][3])
    return l


def graphisme(plateau, coord_piece, coord_pieces_place,ancien_coord_piece, hauteurFenetre, largeurFenetre, prochaine_piece, score, niveau, compteur_ligne, gameOver,num):
    from math import sqrt
    """
    Affiche l'état graphique du jeu Tetris, incluant le plateau, la prochaine pièce, le score, le niveau, et le nombre de lignes.

    Cette fonction dessine plusieurs éléments sur l'écran, tels que :
    - Le plateau de jeu avec les cases remplies ou vides.
    - La prochaine pièce à jouer.
    - Les informations du jeu (score, niveau, lignes complétées).
    - Les pièces actuellement en jeu et les pièces déjà placées.
    - Si le jeu est terminé, affiche un écran "GAME OVER" grâce à la fonction game_over.

    :param plateau: Liste 2D représentant l'état du plateau de jeu, où chaque élément contient des informations sur les cases.
    :param coord_piece: Liste des coordonnées et couleurs des blocs de la pièce en cours.
    :param coord_pieces_place: Liste des coordonnées et couleurs des blocs des pièces déjà placées.
    :param hauteurFenetre: Hauteur de la fenêtre de jeu en pixels.
    :param largeurFenetre: Largeur de la fenêtre de jeu en pixels.
    :param prochaine_piece: Liste représentant la prochaine pièce à jouer, incluant sa forme et sa couleur.
    :param score: Score actuel du joueur, un entier.
    :param niveau: Niveau actuel du jeu, un entier.
    :param compteur_ligne: Nombre de lignes complétées par le joueur, un entier.
    :param gameOver: Booléen indiquant si le jeu est terminé. Si True, l'écran "GAME OVER" sera affiché.
    """

    # Dimensions du plateau
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    # Calculer la taille d'un carré
    hauteur_boite = (hauteurFenetre*0.97) - (hauteurFenetre * 0.03)
    largeur_boite = (largeurFenetre* 0.57) - (largeurFenetre * 0.03)
    taille_carre = min(hauteur_boite / nb_lignes, largeur_boite / nb_colonnes)

    rectangle_x = largeurFenetre * 0.02

    a,b = (rectangle_x,hauteurFenetre * 0.5), (hauteurFenetre*0.27,hauteurFenetre*0.25)
    calcule_longeur_coter = int(sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2)))
    taille_carre = calcule_longeur_coter / nb_colonnes
    moitier_diagonal_carre = (sqrt(2) * taille_carre)/2
    
    #-----------------------------------------------DESSIN PROCHAINE PIECE------------------------------------------
    if prochaine_piece != []:
        # Position de départ pour dessiner la prochaine pièce
        piece_x = largeurFenetre * 0.55 + (largeurFenetre * 0.95 - largeurFenetre * 0.55) / 2 - (len(prochaine_piece[0][0]) * taille_carre) / 2
        piece_y = hauteurFenetre * 0.10 + (hauteurFenetre * 0.25 - hauteurFenetre * 0.10) / 2 - (len(prochaine_piece[0]) * taille_carre) / 2


        
        # Dessiner la forme dans la zone dédiée
        forme(piece_x, piece_y, prochaine_piece[0], prochaine_piece[1], taille_carre*1.25,prochaine_piece[3])
    #---------------------------------------------------------------------------------------------------------------
    
    if coord_piece != []:
        efface(coord_piece[1][3])
    
    if num == 1:
        efface("score")
        efface("niveau")
        efface("ligne")

        #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
        taille_txt = int(10 * (hauteurFenetre*0.0025))
        texte(largeurFenetre * 0.57, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:{score}",police = "Arial Black",taille = taille_txt,couleur = 'white',tag = "score") #score
        texte(largeurFenetre * 0.57,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:{niveau}",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "niveau")
        texte(largeurFenetre * 0.57,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:{compteur_ligne}",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "ligne")
        #---------------------------------------------------------------------------------------------------------------
        
        if ancien_coord_piece != []:
            for tags in recuperer_tag(ancien_coord_piece):
                efface(tags)
        
        for i in range(len(coord_pieces_place)):
            for j in range(len(coord_pieces_place[i])):
                rectangle_x = largeurFenetre * 0.02
                rectangle_x += moitier_diagonal_carre * coord_pieces_place[i][j][1]
                rectangle_y = hauteurFenetre * 0.5
                rectangle_y += moitier_diagonal_carre * coord_pieces_place[i][j][0]
                
                polygone([(rectangle_x + (coord_pieces_place[i][j][0] * moitier_diagonal_carre),
                        rectangle_y - (coord_pieces_place[i][j][1] * moitier_diagonal_carre)),
                        
                        (moitier_diagonal_carre + rectangle_x + (coord_pieces_place[i][j][0] * moitier_diagonal_carre),
                        rectangle_y - (coord_pieces_place[i][j][1] * moitier_diagonal_carre) - moitier_diagonal_carre),
                        
                        (moitier_diagonal_carre * 2 + rectangle_x + (coord_pieces_place[i][j][0] * moitier_diagonal_carre),
                        rectangle_y - (coord_pieces_place[i][j][1] * moitier_diagonal_carre)),
                        
                        (moitier_diagonal_carre + rectangle_x + (coord_pieces_place[i][j][0] * moitier_diagonal_carre),
                        rectangle_y - (coord_pieces_place[i][j][1] * moitier_diagonal_carre) + moitier_diagonal_carre)], 
                        
                        remplissage=coord_pieces_place[i][j][2],
                        tag=coord_pieces_place[i][j][3])
    else:
        
        for i in range(len(coord_piece)):
            rectangle_x = largeurFenetre * 0.02
            rectangle_x += moitier_diagonal_carre * coord_piece[i][1]
            rectangle_y = (hauteurFenetre * 0.5)
            rectangle_y += moitier_diagonal_carre * coord_piece[i][0]
            polygone([(rectangle_x + (coord_piece[i][0] * moitier_diagonal_carre),
                    rectangle_y-((coord_piece[i][1] * moitier_diagonal_carre))),

                    (moitier_diagonal_carre+rectangle_x+ (coord_piece[i][0] * moitier_diagonal_carre),
                    rectangle_y-(coord_piece[i][1] * (moitier_diagonal_carre))-moitier_diagonal_carre),

                    (moitier_diagonal_carre*2+rectangle_x+ (coord_piece[i][0] * moitier_diagonal_carre),
                    rectangle_y-(coord_piece[i][1] * moitier_diagonal_carre)),

                    (moitier_diagonal_carre+rectangle_x+ (coord_piece[i][0] * moitier_diagonal_carre),
                    rectangle_y-(coord_piece[i][1] * moitier_diagonal_carre)+moitier_diagonal_carre)], 

                    remplissage=coord_piece[i][2],
                    tag = coord_piece[i][3])
    mise_a_jour() #on met a jour le plateau

    if gameOver:
        game_over(plateau, hauteurFenetre, largeurFenetre)


