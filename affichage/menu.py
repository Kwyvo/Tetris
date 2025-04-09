from module.fltk import *
from composant.boutons import *
from sauvegarde.sauvegarde import charger_donnees
from jeu import jeu
from mode_jeu.polyominos.polyominos import polyominos
from mode_jeu.pourrissement import pourrissement_jeu
from affichage.param import menu_para




def menu(hauteurFenetre, largeurFenetre, score, niveau, compteur_ligne,vitesse= 1):
    

    """
    Affiche le menu principal du jeu Tetris, y compris le plateau, les informations du jeu, 
    et les boutons pour démarrer ou quitter le jeu.

    Cette fonction gère :
    - Le dessin du plateau de jeu avec une bordure.
    - La zone pour afficher la prochaine pièce à venir.
    - L'affichage du score, du niveau et du nombre de lignes.
    - L'interaction avec les boutons pour commencer une nouvelle partie ou quitter.

    :param hauteurFenetre: Hauteur de la fenêtre du jeu en pixels.
    :param largeurFenetre: Largeur de la fenêtre du jeu en pixels.
    :param score: Le score actuel du joueur, un entier.
    :param niveau: Le niveau actuel du jeu, un entier.
    :param compteur_ligne: Le nombre de lignes complétées par le joueur, un entier.

    Renvoie `True` si l'utilisateur clique sur le bouton "Play" pour commencer une nouvelle partie.
             Si l'utilisateur clique sur le bouton "Exit", la fenêtre se ferme.
    """

    plateau = [[0 for i in range(10)] for j in range(20)]
    test=False
    taille_txt = int(10 * (hauteurFenetre*0.0025))

   


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
    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.03, largeurFenetre * 0.97, hauteurFenetre * 0.37,couleur = '#FF00FF')

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.07, largeurFenetre * 0.76, hauteurFenetre * 0.17,couleur = '#FF00FF')#LOAD 1
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.10,"SLOT 1",couleur="White",police="Arial Black",taille = taille_txt)


    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.07, largeurFenetre * 0.97, hauteurFenetre * 0.17,couleur = '#FF00FF')#LOAD 2
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.10,"SLOT 2",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.17, largeurFenetre * 0.76, hauteurFenetre * 0.27,couleur = '#FF00FF')#LOAD 3
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.20,"SLOT 3",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.17, largeurFenetre * 0.97, hauteurFenetre * 0.27,couleur = '#FF00FF')#LOAD 4
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.20,"SLOT 4",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.27, largeurFenetre * 0.76, hauteurFenetre * 0.37,couleur = '#FF00FF')#LOAD 5
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.30,"SLOT 5",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.27, largeurFenetre * 0.97, hauteurFenetre * 0.37,couleur = '#FF00FF',)#LOAD 6
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.30,"SLOT 6",couleur="White",police="Arial Black",taille = taille_txt)

    texte(largeurFenetre * 0.67,hauteurFenetre * 0.03,"LOAD SAVE",couleur="White",police="Arial Black", taille = taille_txt)

    #---------------------------------------------------------------------------------------------------------------

    #--------------------------------------AFFICHAGE SCORE NIVEAU LIGNE---------------------------------------------
    debut_rectangle_hauteur = hauteurFenetre * 0.40
    for i in range(3):
        rectangle(largeurFenetre * 0.55,debut_rectangle_hauteur, largeurFenetre * 0.97, debut_rectangle_hauteur+hauteurFenetre*0.10, remplissage = '#111111', couleur = '#FF00FF')
        debut_rectangle_hauteur += hauteurFenetre*0.10

    taille_txt = int(10 * (hauteurFenetre*0.0025))
    texte(largeurFenetre * 0.57, (hauteurFenetre * 0.40 + hauteurFenetre * 0.475)/2,f"SCORE:{score}",police = "Arial Black",taille = taille_txt,couleur = 'white') #score

    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.50 + hauteurFenetre * 0.575)/2,f"LEVEL:{niveau}",police = "Arial Black", taille = taille_txt,couleur = 'white')

    texte(largeurFenetre * 0.57,(hauteurFenetre * 0.60 + hauteurFenetre * 0.675)/2,f"ROW:{compteur_ligne}",police = "Arial Black", taille = taille_txt,couleur = 'white')

    #---------------------------------------------------------------------------------------------------------------

    #--------------------------------------AFFICHAGE PARAMETRES-----------------------------------------------------

    #rectangle(largeurFenetre* 0.90, hauteurFenetre* 0.90, largeurFenetre-1, hauteurFenetre-1, couleur = "green")
    taille_img= int(40 * (hauteurFenetre*0.0025))
    image(largeurFenetre* 0.93, hauteurFenetre*0.93,"image/parametres.png",hauteur=taille_img,largeur=taille_img)

    #---------------------------------------------------------------------------------------------------------------




    if boutons_play(largeurFenetre, hauteurFenetre):
        return "PLAY"
    elif boutons_exit(largeurFenetre, hauteurFenetre):
        ferme_fenetre()

    


    
    #---------------------BOUTONS SLOTS ----------------------------------------------------------------------------------------

    if boutons_slot1(largeurFenetre, hauteurFenetre):
        dico = charger_donnees("save1.json")
        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    elif boutons_slot2(largeurFenetre, hauteurFenetre):
        dico= charger_donnees("save2.json")

        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    elif boutons_slot3(largeurFenetre, hauteurFenetre):
        dico= charger_donnees("save3.json")
        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    elif boutons_slot4(largeurFenetre, hauteurFenetre):
        dico= charger_donnees("save4.json")
        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    elif boutons_slot5(largeurFenetre, hauteurFenetre):
        dico= charger_donnees("save5.json")
        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    elif boutons_slot6(largeurFenetre, hauteurFenetre):
        dico= charger_donnees("save6.json")
        plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu =  dico["plateau"],dico["coord_p"],dico["score"],dico["lignes"],dico["lvl"],dico["gamemode"]

        if mode_de_jeu=="casual":
            return jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="pourri":
            return pourrissement_jeu(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)

        elif mode_de_jeu=="poly":
            return polyominos(hauteurFenetre, largeurFenetre,plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu)


    #---------------------BOUTONS PARAMETRES -----------------------------------------------------------------------
    elif boutons_para(largeurFenetre, hauteurFenetre):
        test= not(test)
        valeurs=menu_para(test)
        hauteurFenetre,largeurFenetre=valeurs[1],valeurs[2]
        redimensionne_fenetre(hauteurFenetre,largeurFenetre)
        mise_a_jour()

        
    #---------------------------------------------------------------------------------------------------------------

            
    elif boutons_exit(largeurFenetre, hauteurFenetre):
        ferme_fenetre()

    