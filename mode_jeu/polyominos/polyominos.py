# -------Importation-------
from time import sleep, time
from module.fltk import *
from random import randint

from affichage.menu_pause import menu_pause
from sauvegarde.sauvegarde import recup_donnees
from fonction_piece.placer_pièce import placer_piece
from fonction_evenement.collision import collision
from affichage.graphisme import graphisme,dessin_plateau
from mode_jeu.polyominos.genere_piece_poly import generer_piece
from fonction_evenement.deplacement import deplacement
from fonction_piece.positionne_piece_generer import positionne_piece_generer
from fonction_piece.piece_rotation import rotation
from fonction_evenement.verifie_lignes import verifie_lignes
from fonction_evenement.zone_de_spawn_libre import zone_de_spawn_libre
from sauvegarde.sauvegarde import *
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
    texte(largeurFenetre * 0.57, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:0",police = "Fixedsys",taille = taille_txt,couleur = 'white',tag = "score") #score
    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:1",police = "Fixedsys", taille = taille_txt,couleur = 'white',tag = "niveau")
    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:0",police = "Fixedsys", taille = taille_txt,couleur = 'white',tag = "ligne")
    #---------------------------------------------------------------------------------------------------------------

    # Dessiner le rectangle du plateau 1
    dessin_plateau(1,rectangle_x,rectangle_y,rectangle_largeur,rectangle_hauteur,largeurFenetre)
    """for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            rectangle(
                (taille_carre * j) + rectangle_x,
                (taille_carre * i) + rectangle_y,
                (taille_carre * j) + taille_carre + rectangle_x,
                (taille_carre * i) + taille_carre + rectangle_y,
                couleur = 'gray5'
            )"""

    

    # Zone pour afficher la prochaine pièce
    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.03, largeurFenetre * 0.97, hauteurFenetre * 0.37, remplissage = '#111111', couleur='#FF00FF')
    
    mise_a_jour()

def polyominos(hauteurFenetre,largeurFenetre,sauv_plateau = [],sauv_coord_pieces_placer = [],score= 0,compteur_ligne = 0,niveau = 1,mode_de_jeu="poly"):
    """
    Fonction principale qui exécute le mode polyminos du jeu Tetris.
    La fonction s'arrête lorsque la pièce qui apparaît rentre directement en colision avec une autre deja présente sur le plateau
    La fonction regroupe et traite l'ensemble des mécaniques de jeu; à savoir:

        - La création et la gestion du plateau de jeu.
        - L'apparition aléatoire des pièces préalablement définis dans un fichier texte par des "+".
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
        coord_pieces_placer = sauv_coord_pieces_placer[:]
        display(hauteurFenetre,largeurFenetre,plateau)
        graphisme(plateau, [], coord_pieces_placer,[], hauteurFenetre, largeurFenetre, [], score, niveau, compteur_ligne, False,1)
    
    # -----------------------------------------------------

    # [[[#coord premier cube] #coord tout les cubes de la piece]# coord toute les pieces]

    prochaine_piece = [generer_piece(), generer_piece()][:]
    lignes_suppr = 0
    gameOver = False
    cooldown_rota = 0
    piece = []
    cooldown= 0
    pause= False
    
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

            temps_base = vitesse=charger_donnees("para.json")["vitesse"]
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
                touche = None
                # Déplacement à gauche ou à droite si pas de collision
                if touche_pressee('Left') : 
                    touche = 'Left'
                elif touche_pressee("Right"):
                    touche = 'Right'

                if (touche == 'Right' or touche == 'Left') and not collision(plateau, coord_piece, touche):
                    plateau = deplacement(plateau, coord_piece, touche)
                #---------------------------------------------------------------------------------------------------

                if touche_pressee("Up") and time()>= cooldown_rota:
                    cooldown_rota = time()+0.2
                    sleep(0.1)
                    if piece[2] != 'carre':
                        plateau[:], coord_piece[:], taille_piece, piece[0] = rotation(plateau, coord_piece, coord_pieces_placer, piece, i_debut)

                if touche_pressee("Down"): # si on veut aller plus vite
                    temps_chute = 0

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