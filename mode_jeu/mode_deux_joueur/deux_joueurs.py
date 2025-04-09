# -------Importation-------
from time import time
from module.fltk import *
import asyncio


from affichage.menu_pause import menu_pause
from fonction_piece.placer_pièce import placer_piece
from fonction_evenement.collision import collision
from mode_jeu.mode_deux_joueur.graphisme_deux_joueurs import graphisme,graphisme2,dessin_plateau
from fonction_piece.genere_piece import generer_piece
from fonction_evenement.deplacement import deplacement
from fonction_piece.positionne_piece_generer import positionne_piece_generer
from fonction_piece.piece_rotation import rotation
from fonction_evenement.verifie_lignes import verifie_lignes
from fonction_evenement.zone_de_spawn_libre import zone_de_spawn_libre
# -------------------------

def display(hauteurFenetre, largeurFenetre, plateau,num):

    # Dimensions du plateau
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    # Calculer la taille d'un carré
    hauteur_boite = (hauteurFenetre*0.97) - (hauteurFenetre * 0.03)
    largeur_boite = (largeurFenetre* 0.57) - (largeurFenetre * 0.03)
    taille_carre = min(hauteur_boite / nb_lignes, largeur_boite / nb_colonnes)

    # Calculer les dimensions du plateau
    rectangle_x = largeurFenetre * 0.03
    rectangle_x_2 = largeurFenetre*0.48+rectangle_x
    rectangle_y = hauteurFenetre * 0.03
    rectangle_largeur = taille_carre * nb_colonnes
    rectangle_hauteur = taille_carre * nb_lignes

    if num == 1:
        # Dessiner le rectangle du plateau 1
        dessin_plateau(1,rectangle_x,rectangle_y,rectangle_largeur,rectangle_hauteur,largeurFenetre)
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                rectangle(
                    (taille_carre * j) + rectangle_x,
                    (taille_carre * i) + rectangle_y,
                    (taille_carre * j) + taille_carre + rectangle_x,
                    (taille_carre * i) + taille_carre + rectangle_y,
                    couleur = 'gray5'
                )

        #zone de score niveau etc        
        debut_rectangle_hauteur = hauteurFenetre * 0.40
        for i in range(3):
            rectangle(largeurFenetre * 0.31,debut_rectangle_hauteur, largeurFenetre * 0.49, debut_rectangle_hauteur+hauteurFenetre*0.10, remplissage = '#111111', couleur = '#FF00FF')
            debut_rectangle_hauteur += hauteurFenetre*0.10

        #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
        taille_txt = int(10 * (hauteurFenetre*0.0025))
        texte(largeurFenetre * 0.32, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:0",police = "Arial Black",taille = taille_txt,couleur = 'white',tag = "score1") #score
        texte(largeurFenetre * 0.32,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:1",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "niveau1")
        texte(largeurFenetre * 0.32,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:0",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "ligne1")
        #---------------------------------------------------------------------------------------------------------------

        # Zone pour afficher la prochaine pièce
        rectangle(largeurFenetre * 0.31, hauteurFenetre * 0.03, largeurFenetre * 0.49, hauteurFenetre * 0.37, remplissage = '#111111', couleur='#FF00FF')
    else:
        # Dessiner le rectangle du plateau
        dessin_plateau(2,rectangle_x,rectangle_y,rectangle_largeur,rectangle_hauteur,largeurFenetre)
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                rectangle(
                    (taille_carre * j) + rectangle_x_2,
                    (taille_carre * i) + rectangle_y,
                    (taille_carre * j) + taille_carre + rectangle_x_2,
                    (taille_carre * i) + taille_carre + rectangle_y,
                    couleur = 'gray5'
                )

        #zone de score niveau etc
        debut_rectangle_hauteur = hauteurFenetre * 0.40
        for i in range(3):
            rectangle(largeurFenetre * 0.80,debut_rectangle_hauteur, largeurFenetre * 0.98, debut_rectangle_hauteur+hauteurFenetre*0.10, remplissage = '#111111', couleur = '#FF00FF')
            debut_rectangle_hauteur += hauteurFenetre*0.10

        #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
    
        taille_txt = int(10 * (hauteurFenetre*0.0025))
        texte(largeurFenetre * 0.81, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:0",police = "Arial Black",taille = taille_txt,couleur = 'white',tag = "score2") #score
        texte(largeurFenetre * 0.81,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:1",police = "Arial Black", taille = taille_txt,couleur = 'white',tag ="niveau2" )
        texte(largeurFenetre * 0.81,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:0",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "ligne2")
        #---------------------------------------------------------------------------------------------------------------

        # Zone pour afficher la prochaine pièce
        rectangle(largeurFenetre * 0.80, hauteurFenetre * 0.03, largeurFenetre * 0.98, hauteurFenetre * 0.37, remplissage = '#111111', couleur='#FF00FF')
    mise_a_jour()


async def jeu_joueur(hauteurFenetre, largeurFenetre, plateau,num, graphisme_func, touches):

    display(hauteurFenetre, largeurFenetre, plateau, num) #fonction qui affiche les éléments qui ne changeant pas (ex = contour du plateau,zone de la prochaine piece)

    coord_pieces_placer = []
    prochaine_piece = [generer_piece(), generer_piece()]
    score, lignes_suppr, niveau, compteur_ligne = 0, 0, 1, 0
    gameOver = False
    cooldown_rota = 0
    piece = []

    while not gameOver:
        #-----------------------Vérifier si le jeu est terminé après l'apparition de la pièce-----------------------
        if piece != [] and not zone_de_spawn_libre(plateau, piece):
            gameOver = True
            graphisme_func(plateau, [], coord_pieces_placer,ancien_cood_piece_posee, hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,1)
            return
        #-----------------------------------------------------------------------------------------------------------
        
        piece = prochaine_piece.pop(0)#[piece, couleur, nom piece]
        plateau = positionne_piece_generer(plateau, piece[0]) # on positionne la pièce choisit aléatoirement au milieu du plateau
        taille_piece = len(piece[0])
        i_debut = 0
        i_fin = len(plateau) # hauteur du plateau

        #--------------------------------------------------GRAVITÉ--------------------------------------------------
        while i_debut <= i_fin - taille_piece:  # hauteur du plateau moins l'espace de fin pour la pièce

            #------------------------ON RÉCUPÈRE LES COORDONNÉES DE LA PIÈCE DANS LE PLATEAU------------------------
            # stockage des coordonnées des cube de la pièce à chaque chute de la pièce [[i,j,couleur],[i,j,couleur],[i,j,couleur],[i,j,couleur]]
            coord_piece = [[i, j, piece[1], piece[3]] for i in range(len(plateau)) for j in range(len(plateau[i])) if plateau[i][j] == 1]
            #-------------------------------------------------------------------------------------------------------
            
            #---------------------ON DÉFINIT LA DURÉE LIMITE EN FONCTION DU NIVEAU (EN SECONDES)--------------------
            if lignes_suppr >= 10:
                niveau += 1
                lignes_suppr = lignes_suppr%10

            temps_base = 1.0 #temp de base 1 seconde
            # Augmentation de 25% de la vitesse de chute à chaque niveau
            temps_chute = temps_base * (0.75 ** (niveau))
            debut_temps = time()

            # ----------------------------------MOUVEMENT DROITE, GAUCHE, ROTATION, CHUTE---------------------------
            while time() - debut_temps < temps_chute:  # tant que le temps moins debut_temps et inferieur a le temps_chute
                await asyncio.sleep(0.03)

                if touche_pressee('Escape') and time() >= cooldown:
                    efface(prochaine_piece[0][3])
                    pause= not(pause)
                    cooldown= time() + 2
                    quitte = menu_pause(pause,cooldown,plateau,coord_pieces_placer,score,niveau,compteur_ligne,"")
                    if quitte :
                        return 
                    
                #--------------------SI ON VA À DROITE OU À GAUCHE, ON VÉRIFIE LES COLLISIONS-----------------------
                touche = None
                # Déplacement à gauche ou à droite si pas de collision
                if touche_pressee(touches["gauche"]):
                    touche = 'Left'
                elif touche_pressee(touches["droite"]):
                    touche = 'Right'
                if (touche == 'Right' or touche == 'Left') and not collision(plateau, coord_piece, touche):
                    plateau = deplacement(plateau, coord_piece, touche)

                #---------------------------------------------------------------------------------------------------


                if touche_pressee(touches["rotation"])and time()>= cooldown_rota:
                    cooldown_rota = time()+0.2
                    await asyncio.sleep(0.2)
                    if piece[2] != 'carre':
                        plateau[:], coord_piece[:], taille_piece, piece[0] = rotation(plateau, coord_piece, coord_pieces_placer, piece, i_debut)
                    

                if touche_pressee(touches["descente"]): # si on veut aller plus vite
                    temps_chute = 0

                ev = donne_ev()
                if type_ev(ev) == 'Quitte':
                    ferme_fenetre()

                #on affiche l'aspect graphique du jeu
                graphisme_func(plateau, coord_piece, coord_pieces_placer,[], hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,0)

            #-------------------------------------------------------------------------------------------------------
            
            #------------------------------------VERIFICATION COLLISION AVEC LE BAS---------------------------------
            if collision(plateau, coord_piece, "Bottom"): # S'il y a une collision alors la piece se stoppe
                break
            #-------------------------------------------------------------------------------------------------------

            #------------------------------SUPRESSION ET DECALAGE DE LA PIÈCE---------------------------------------
            # On va supprimer l'ancienne pièce grâce aux coordonées
            for i in range(len(coord_piece)):
                plateau[coord_piece[i][0]][coord_piece[i][1]] = 0
            # Déplacement vers le bas de la pièce grâce aux coordonées
            for i in range(len(coord_piece)):
                plateau[coord_piece[i][0] + 1][coord_piece[i][1]] = 1
            #-------------------------------------------------------------------------------------------------------
            i_debut += 1

        #-------------------------------------PLACAGE DES PIECES APRES COLLISION------------------------------------

        coord_piece_placer = placer_piece(plateau, piece[1],piece[3])
        plateau = coord_piece_placer[1]
        coord_pieces_placer.append(coord_piece_placer[0])
        prochaine_piece.append(generer_piece())
        #-----------------------------------------------------------------------------------------------------------
        
        #------------------------------------VERIFIER LES LIGNES, COMPTAGE SCORE------------------------------------
        recup_score, recup_lignes_suppr, plateau, coord_pieces_placer, ancien_cood_piece_posee = verifie_lignes(plateau, coord_pieces_placer)
        lignes_suppr += recup_lignes_suppr
        compteur_ligne += recup_lignes_suppr
        score += int(recup_score * (niveau) * 1.25)
        if recup_lignes_suppr != 0:
            graphisme_func(plateau, coord_piece, coord_pieces_placer,ancien_cood_piece_posee, hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,1)
        
        #-----------------------------------------------------------------------------------------------------------

async def deux_joueurs(hauteurFenetre, largeurFenetre):
    # --------ON CRÉER LE PLATEAU DE 10X20-----------------
    plateau1 = [[0 for _ in range(10)] for _ in range(20)]
    plateau2 = [[0 for _ in range(10)] for _ in range(20)]
    # -----------------------------------------------------

    #On créer la tache joueur1 
    joueur1 = asyncio.create_task(jeu_joueur(
        hauteurFenetre, largeurFenetre, plateau1,1, graphisme, {
            "gauche": "q", "droite": "d", "rotation": "z", "descente": "s"
        }
    ))

    #On créer la tache joueur2
    joueur2 = asyncio.create_task(jeu_joueur(
        hauteurFenetre, largeurFenetre, plateau2,2, graphisme2, {
            "gauche": "Left", "droite": "Right", "rotation": "Up", "descente": "Down"
        }
    )) 
    await asyncio.gather(joueur1, joueur2) #On lance les deux tâches parallelements et on attend la fin des deux tache