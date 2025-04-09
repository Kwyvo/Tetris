# -------Importation-------
from time import sleep, time
from module.fltk import *
from random import randint
from copy import deepcopy


from affichage.menu_pause import menu_pause
from affichage.affiche_plateau import affiche_plateau
from fonction_piece.placer_pièce import placer_piece
from fonction_evenement.collision import collision
from affichage.graphisme import graphisme,dessin_plateau
from fonction_piece.genere_piece import generer_piece
from fonction_evenement.deplacement import deplacement
from fonction_piece.positionne_piece_generer import positionne_piece_generer
from fonction_piece.piece_rotation import rotation
from fonction_evenement.verifie_lignes import verifie_lignes
from fonction_evenement.zone_de_spawn_libre import zone_de_spawn_libre
from simulation.simulation_position import simulation_position
# -------------------------

def display(hauteurFenetre, largeurFenetre, plateau):

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

    #zone de score niveau etc        
    debut_rectangle_hauteur = hauteurFenetre * 0.40
    for i in range(3):
        rectangle(largeurFenetre * 0.55,debut_rectangle_hauteur, largeurFenetre * 0.97, debut_rectangle_hauteur+hauteurFenetre*0.10, remplissage = '#111111', couleur = '#FF00FF')
        debut_rectangle_hauteur += hauteurFenetre*0.10

    #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
    taille_txt = int(10 * (hauteurFenetre*0.0025))
    texte(largeurFenetre * 0.57, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:0",police = "Arial Black",taille = taille_txt,couleur = 'white',tag = "score") #score
    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:1",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "niveau")
    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:0",police = "Arial Black", taille = taille_txt,couleur = 'white',tag = "ligne")
    #---------------------------------------------------------------------------------------------------------------

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

    

    # Zone pour afficher la prochaine pièce
    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.03, largeurFenetre * 0.97, hauteurFenetre * 0.37, remplissage = '#111111', couleur='#FF00FF')
    
    mise_a_jour()



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


def jeu_ia(hauteurFenetre,largeurFenetre,sauv_plateau = [],sauv_coord_pieces_placer = [],score= 0,compteur_ligne = 0,niveau = 1,mode_de_jeu = "casual" ):
    """
    Fonction principale qui exécute le jeu Tetris.
    La fonction s'arrête lorsque la pièce qui apparaît rentre directement en colision avec une autre deja présente sur le plateau
    La fonction regroupe et traite l'ensemble des mécaniques de jeu; à savoir:

        - La création et la gestion du plateau de jeu.
        - L'apparition aléatoire des pièces.
        - Le déplacement, la chute et la rotation des pièces.
        - La gravité pour faire tomber les pièces au bout de x secondes.
        - Les vérifications de collisions pour le mouvement et la chute.
        - Le suivi et l'affichage du score et du niveau.
        - La détection des lignes complètes et leur suppression.
        - L'augmentation de la vitesse au fur et à mesure que le niveau augmente.
    """

    # --------ON CRÉER LE PLATEAU DE 10X20-----------------
    if sauv_plateau == []:
        plateau = [[0 for i in range(10)] for j in range(20)]
        coord_pieces_placer = []
        display(hauteurFenetre,largeurFenetre,plateau)
    else:
        plateau = sauv_plateau[:]
        display(hauteurFenetre,largeurFenetre,plateau)
        coord_pieces_placer = sauv_coord_pieces_placer[:]
        graphisme(plateau, [], coord_pieces_placer,[], hauteurFenetre, largeurFenetre, [], score, niveau, compteur_ligne, False,1)
    
    # -----------------------------------------------------
    

    # [[[#coord premier cube] #coord tout les cubes de la piece]# coord toute les pieces]
    prochaine_piece = [generer_piece(), generer_piece()][:]
    lignes_suppr = 0
    gameOver = False
    cooldown_rota = 0
    pause=False
    cooldown=0
    piece = []
    
    while not gameOver:

        #-----------------------Vérifier si le jeu est terminé après l'apparition de la pièce-----------------------
        if piece != [] and not zone_de_spawn_libre(plateau, piece): #on verifie si un bloc est deja present sur la zone de spawn
            gameOver = True
            graphisme(plateau, coord_piece, coord_pieces_placer,ancien_coord_piece, hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,1)
            efface(prochaine_piece[0][3])
            return True
        #-----------------------------------------------------------------------------------------------------------

        piece = prochaine_piece.pop(0) #[piece, couleur, nom piece]
        plateau = positionne_piece_generer(plateau, piece[0])  # on positionne la pièce choisit aléatoirement au milieu du plateau


        #---------------------------------------------SIMULATION---------------------------------------------------

        plateau2 = deepcopy(plateau)
        piece2 = deepcopy(piece)

        coord_piece2 = []  # stockage des coordonnées des cube de la pièce [[i,j,couleur],[i,j,couleur],[i,j,couleur],[i,j,couleur]]
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau2[i][j] == 1:
                    coord_piece2.append([i, j, piece[1],piece[3]])
        
        meilleur_position,rot = simulation_position(plateau2,coord_pieces_placer,coord_piece2,piece2[0],piece2)
        

        for _ in range(rot+1): #on effectue la "rotation" pour trouver la difference
            plateau2[:], coord_piece2[:], taille_piece, piece2[0] = rotation(plateau2, coord_piece2, [], piece2, 0)

        
        afficher(plateau,meilleur_position)

        difference = meilleur_position[0][1] - coord_piece2[0][1] 

    
        liste_deplacement = []
        liste_deplacement += ["Up"] * rot
        if difference < 0:
            liste_deplacement += ["Left"]*abs(difference)
        else:
            liste_deplacement += ["Right"]*difference

        #-----------------------------------------------------------------------------------------------------------


        taille_piece = len(piece[0])
        i_debut = 0
        i_fin = len(plateau)  # hauteur du plateau

        #--------------------------------------------------GRAVITÉ--------------------------------------------------
        while i_debut <= i_fin - taille_piece: # hauteur du plateau moins l'espace de fin pour la pièce

            #------------------------ON RÉCUPÈRE LES COORDONNÉES DE LA PIÈCE DANS LE PLATEAU------------------------
            coord_piece = []  # stockage des coordonnées des cube de la pièce à chaque chute de la pièce [[i,j,couleur],[i,j,couleur],[i,j,couleur],[i,j,couleur]]
            for i in range(len(plateau)):
                for j in range(len(plateau[i])):
                    if plateau[i][j] == 1:
                        coord_piece.append([i, j, piece[1],piece[3]])
            #-------------------------------------------------------------------------------------------------------

            #---------------------ON DÉFINIT LA DURÉE LIMITE EN FONCTION DU NIVEAU (EN SECONDES)--------------------
            if lignes_suppr >= 10:
                niveau += 1
                lignes_suppr = lignes_suppr%10

            temps_base = 1.0  #temp de base 1 seconde
            # Augmentation de 25% de la vitesse de chute à chaque niveau
            temps_chute = temps_base * (0.75 ** (niveau))
            debut_temps = time()
            # ----------------------------------MOUVEMENT DROITE, GAUCHE, ROTATION, CHUTE---------------------------
            while time() - debut_temps < temps_chute: # tant que le temps moins debut_temps et inferieur a le temps_chute
                sleep(0.03)
                
                if touche_pressee('Escape') and time() >= cooldown:
                    efface(prochaine_piece[0][3])
                    pause= not(pause)
                    cooldown= time() + 2
                    quitte = menu_pause(pause,cooldown,plateau,coord_pieces_placer,score,niveau,compteur_ligne,mode_de_jeu)
                    if quitte :
                        return 

                
                #--------------------SI ON VA À DROITE OU À GAUCHE, ON VÉRIFIE LES COLLISIONS-----------------------
                for touche in liste_deplacement:
                    sleep(0.1)
                    if (touche == 'Right' or touche == 'Left') and not collision(plateau, coord_piece, touche):
                        plateau = deplacement(plateau, coord_piece, touche)

                    if touche == "Up" and time()>= cooldown_rota:
                        cooldown_rota = time()+0.2
                        sleep(0.2)
                        if piece[2] != 'carre':
                            plateau[:], coord_piece[:], taille_piece, piece[0] = rotation(plateau, coord_piece, coord_pieces_placer, piece, i_debut)   
                    
                    graphisme(plateau, coord_piece, coord_pieces_placer,[], hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,0) 
                liste_deplacement[:] = []

                if coord_piece[0][1] == meilleur_position[0][1]: #si la piece ce trouve sur la meme colonnes alors la piece descent
                    temps_chute = 0
                #---------------------------------------------------------------------------------------------------

                ev = donne_ev()
                if type_ev(ev) == 'Quitte':
                    ferme_fenetre()
                
                #on affiche l'aspect graphique du jeu
                graphisme(plateau, coord_piece, coord_pieces_placer,[], hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,0) 
                
            #-------------------------------------------------------------------------------------------------------

            #------------------------------------VERIFICATION COLLISION AVEC LE BAS---------------------------------
            if collision(plateau, coord_piece, "Bottom"):  # S'il y a une collision alors la piece se stoppe
                break
            #-------------------------------------------------------------------------------------------------------

            if not pause:
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
        recup_score ,recup_lignes_suppr ,plateau, coord_pieces_placer, ancien_coord_piece = verifie_lignes(plateau, coord_pieces_placer)
        lignes_suppr+=recup_lignes_suppr
        compteur_ligne += recup_lignes_suppr
        score += int(recup_score * (niveau)*1.25)
        if recup_score != 0:
            graphisme(plateau, coord_piece, coord_pieces_placer,ancien_coord_piece, hauteurFenetre, largeurFenetre, prochaine_piece[0], score, niveau, compteur_ligne, gameOver,1)
        #-----------------------------------------------------------------------------------------------------------