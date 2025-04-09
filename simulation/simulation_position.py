from time import sleep
from copy import deepcopy
from module.fltk import *

from fonction_evenement.collision import collision
from fonction_evenement.deplacement import deplacement
from fonction_piece.piece_rotation import rotation



def afficher(plateau,coord_piece): #sera a supp
    # Dimensions du plateau
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    # Calculer la taille d'un carré
    hauteur_boite = (700*0.97) - (700 * 0.03)
    largeur_boite = (700* 0.57) - (700 * 0.03)
    taille_carre = min(hauteur_boite / nb_lignes, largeur_boite / nb_colonnes)

    rectangle_x = 700 * 0.03
    rectangle_y = 700 * 0.03

    efface(coord_piece[0][3])
    for i in range(len(coord_piece)):
        rectangle(
            (taille_carre * coord_piece[i][1]) + rectangle_x,
            (taille_carre * coord_piece[i][0]) + rectangle_y,
            (taille_carre * coord_piece[i][1]) + taille_carre + rectangle_x,
            (taille_carre * coord_piece[i][0]) + taille_carre + rectangle_y,
            remplissage=coord_piece[i][2],
            tag=coord_piece[i][3]
        )
    mise_a_jour()

def affiche_p(plateau,coord_pieces_place): #sera a supp
    # Dimensions du plateau
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    # Calculer la taille d'un carré
    hauteur_boite = (700*0.97) - (700 * 0.03)
    largeur_boite = (700* 0.57) - (700 * 0.03)
    taille_carre = min(hauteur_boite / nb_lignes, largeur_boite / nb_colonnes)

    rectangle_x = 700 * 0.03
    rectangle_y = 700 * 0.03
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            rectangle(
                (taille_carre * j) + rectangle_x,
                (taille_carre * i) + rectangle_y,
                (taille_carre * j) + taille_carre + rectangle_x,
                (taille_carre * i) + taille_carre + rectangle_y,
                couleur = 'gray'
            )
    for i in range(len(coord_pieces_place)):
            for j in range(len(coord_pieces_place[i])):
                rectangle(
                    (taille_carre * coord_pieces_place[i][j][1]) + rectangle_x,
                    (taille_carre * coord_pieces_place[i][j][0]) + rectangle_y,
                    (taille_carre * coord_pieces_place[i][j][1]) + taille_carre + rectangle_x,
                    (taille_carre * coord_pieces_place[i][j][0]) + taille_carre + rectangle_y,
                    remplissage = coord_pieces_place[i][j][2],
                    tag = coord_pieces_place[i][j][3]
                )
    mise_a_jour()





def verifie_dans_p(plateau, i, j):
    # renvoie True si i et j sont dans les limites du plateau
    return 0 <= i < len(plateau) and 0 <= j < len(plateau[0])

def compter_trous(plateau):
    #on compte le nb de trous

    trous = 0
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if est_un_trou(plateau, i, j):
                trous += 1
    return trous
    
def est_un_trou(plateau, i, j):

    if not (0 <= i < len(plateau) and 0 <= j < len(plateau[0])):
        return False
    
    return (plateau[i][j] == 0 and
            (i == 0 or plateau[i-1][j] != 0) and
            (i == len(plateau)-1 or plateau[i+1][j] != 0) and
            (j == 0 or plateau[i][j-1] != 0) and
            (j == len(plateau[0])-1 or plateau[i][j+1] != 0))
            

def trous_generes(plateau):
    return compter_trous(plateau)


def compter_lignes_probable(plateau,coord_piece_suggerees):

    nb_lignes_creee= 0
    for coord in coord_piece_suggerees:
        p1= coord[0] 
        c=0
        for i in range(len(plateau)):
            if i == p1:
                for j in range(len(plateau[0])):
                    if plateau[i][j] in {1,2}:
                        c+=1
                if c == j+1:
                    nb_lignes_creee +=1
    return nb_lignes_creee


def compter_hauteur_jeu2(plateau):
    res = 0
    for i in range(len(plateau)-1,0,-1):
        c = 0
        for j in range(len(plateau[0])):
            if plateau[i][j] == 2 or plateau[i][j] == 1:
                c +=len(plateau)-i
        res += c
    return res

def test(plateau, coord_piece, meilleur_position, score_meilleur_position, nb_trou_position, nb_ligne_supp, hauteur, rotation_meilleur_position, rota):
    
    nb_trou_position_temp = trous_generes(plateau)
    nb_ligne_supp_temp = compter_lignes_probable(plateau,coord_piece)
    hauteur_temp = compter_hauteur_jeu2(plateau)
    score_temp = 0



    if nb_trou_position_temp <= nb_trou_position :
        score_temp+=1

    if nb_ligne_supp_temp >= nb_ligne_supp:
        score_temp+=4

    if hauteur_temp < hauteur:
        score_temp += 3


    if score_temp >= score_meilleur_position:
        meilleur_position = deepcopy(coord_piece)
        nb_trou_position = nb_trou_position_temp
        nb_ligne_supp = nb_ligne_supp_temp
        rotation_meilleur_position = rota
        hauteur = hauteur_temp
        score_meilleur_position = score_temp

    return meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position


def simulation_position(plateau_og, coord_pieces_placer, coord_piece_og, piece_og, piece):
    
    #affiche_p(plateau,coord_pieces_placer) #sera a supp

    plateau = deepcopy(plateau_og)

    for k in range(len(plateau)):
        for l in range(len(plateau[0])):
            if plateau[k][l] == 1:
                plateau[k][l] = 0
              

    # ----------------------------------ON PLACE LA PIECE TOUT A GAUCHE---------------------------
    coord_piece2 = []
    val_j = []
    for bloc in coord_piece_og: #on place la piece tout a gauche
        val_j.append(bloc[1])
    val = min(val_j)
    for bloc in coord_piece_og:
        coord_piece2.append([bloc[0],bloc[1]-val,bloc[2],bloc[3]])
    # --------------------------------------------------------------------------------------------


    if piece[2] in {"t_piece","l_piece","j_piece"}: #on choisi le nombre de rotation a faire pour les tests
        iterable = 4
    elif piece[2] != "carre":
        iterable = 2
    else:
        iterable = 1

    liste_position = []
    meilleur_position = []

    
    nb_trou_position = 10000
    nb_ligne_supp = -1
    hauteur = 10000
    score_meilleur_position = 0
    rotation_meilleur_position = 0

    for i in range(iterable): #on regarde pour chaque rotation de la piece ses positions possible

        coord_piece3 = deepcopy(coord_piece2)
        taille_piece = len(piece_og) #taille de la piece en hauteur

        # ----------------------------------ROTATION DE LA PIECE---------------------------
        if i != 0:
            coord_piece3 = deepcopy(coord_piece2)
            plateau, coord_piece3, taille_piece, piece[0] = rotation(plateau, coord_piece3, coord_pieces_placer, piece, 0)
            for bloc in coord_piece3:
                if bloc[1] < 0:
                    coord_piece3 = [[bloc[0],bloc[1]+1,bloc[2],bloc[3]] for bloc in coord_piece3]
        #----------------------------------------------------------------------------------
        
        j_index = 0

        # ----------------------------------ON PARCOURS TOUTES LES COLONNES---------------------------
        while j_index <= len(plateau[0])-len(piece[0][0]):

            for elt in coord_piece3: #on place la piece dans le plateau
                plateau[elt[0]][elt[1]] = 1
            
            i_debut = 0

            # ----------------------------------ON DESCENT LA coord_piece LE PLUS BAS POSSIBLE---------------------------
            while i_debut <= len(plateau)-taille_piece:  

                coord_piece = [] 
                for k in range(len(plateau)):
                    for j in range(len(plateau[i])):
                        if plateau[k][j] == 1:
                            coord_piece.append([k, j, "gray",piece[3]])

                if collision(plateau,coord_piece,"Bottom"):
                    
                    liste_position.append(coord_piece) #on ajoute la position possible dans la liste des positions

                    meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position = test(plateau,coord_piece,meilleur_position,score_meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,rotation_meilleur_position,i)


                    if not collision(plateau,coord_piece,"Right"): #si la piece peut aller a droite

                        coord_piece4 = deepcopy(coord_piece)
                        plateau2 = deepcopy(plateau)
                        plateau2 = deplacement(plateau2,coord_piece4,"Right")

                        if coord_piece4 not in liste_position:
                            liste_position.append(coord_piece4)

                        meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position = test(plateau,coord_piece,meilleur_position,score_meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,rotation_meilleur_position,i) #on compare si la nouvelle piece est meilleur que lancienne

                        while not collision(plateau2,coord_piece4,"Right"): #tant qu'il n'y a pas de collision a droite on va a droite

                            plateau2 = deplacement(plateau2,coord_piece4,"Right")
                            
                            meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position = test(plateau,coord_piece,meilleur_position,score_meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,rotation_meilleur_position,i)

                            if coord_piece4 in liste_position: #si la coordonner est deja dans la liste des positions on arrete
                                break
                            
                            """for elt in coord_piece4:
                                elt[2] = "red"
                            afficher(plateau2,coord_piece4) 
                            sleep(0.5)"""
                            
                    
                    if not collision(plateau,coord_piece,"Left"): # si la piece peut aller a gauche

                        coord_piece4 = deepcopy(coord_piece)
                        plateau2 = deepcopy(plateau)
                        plateau2 = deplacement(plateau2,coord_piece4,"Left")

                        if coord_piece4 not in liste_position:
                            liste_position.append(coord_piece4)

                        meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position = test(plateau,coord_piece,meilleur_position,score_meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,rotation_meilleur_position,i) #on compare si la nouvelle piece est meilleur que lancienne
    
                        while not collision(plateau2,coord_piece4,"Left"): #tant qu'il n'y a pas de collision a gauche on va a gauche

                            plateau2 = deplacement(plateau2,coord_piece4,"Left")

                            meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,score_meilleur_position,rotation_meilleur_position = test(plateau,coord_piece,meilleur_position,score_meilleur_position,nb_trou_position,nb_ligne_supp,hauteur,rotation_meilleur_position,i)

                            if coord_piece4 in liste_position: #si la coordonner est deja dans la liste des positions on arrete
                                break

                            """for elt in coord_piece4:
                                elt[2] = "blue"
                            afficher(plateau2,coord_piece4)
                            sleep(0.5)"""

                    break #on arrete de descendre

                for l in range(len(coord_piece)):
                    plateau[coord_piece[l][0]][coord_piece[l][1]] = 0 
                for l in range(len(coord_piece)):
                    plateau[coord_piece[l][0] + 1][coord_piece[l][1]] = 1
                i_debut += 1
            #-----------------------------------------------------------------------------------------------------------
            #afficher(plateau,coord_piece) #ON AFFICHE LES REPRESENTATIONS DE LA coord_piece QUI BOUGE

            for elt in coord_piece: #on supprime la piece du plateau
                plateau[elt[0]][elt[1]] = 0

            #sleep(0.2)

            for bloc2 in coord_piece3: #ON DECALE LA coord_piece VERS LA DROITE
                bloc2[1] +=1
            
            j_index+=1
        # ------------------------------------------------------------------------------------------
    
    """afficher(plateau,coord_piece) #ON AFFICHE LES REPRESENTATIONS DE LA coord_piece QUI BOUGE (POUR LES TEST)
    attend_clic_gauche()
    ferme_fenetre()"""
    return meilleur_position ,rotation_meilleur_position
