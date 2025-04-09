from module.fltk import *
from time import *

from composant.boutons import (boutons_save,
                               boutons_slot1,
                               boutons_slot2,
                               boutons_slot3,
                               boutons_slot4,
                               boutons_slot5,
                               boutons_slot6)

from composant.boutons import boutons_leave_game
"""from sauvegarde.sauvegarde import recup_donnees
from sauvegarde.sauvegarde import stocker_donnees"""

plateau = [[0 for i in range(10)] for j in range(20)]
hauteurFenetre = 700
largeurFenetre = 700

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
taille_txt = int(10 * (hauteurFenetre*0.0025))


def save_slot():

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.03, largeurFenetre * 0.97, hauteurFenetre * 0.37,couleur = '#FF00FF')

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.07, largeurFenetre * 0.76, hauteurFenetre * 0.17,couleur = '#FF00FF')#SLOT 1
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.10,"SLOT 1",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.07, largeurFenetre * 0.97, hauteurFenetre * 0.17,couleur = '#FF00FF')#SLOT 2
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.10,"SLOT 2",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.17, largeurFenetre * 0.76, hauteurFenetre * 0.27,couleur = '#FF00FF')#SLOT 3
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.20,"SLOT 3",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.17, largeurFenetre * 0.97, hauteurFenetre * 0.27,couleur = '#FF00FF')#SLOT 4
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.20,"SLOT 4",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.55, hauteurFenetre * 0.27, largeurFenetre * 0.76, hauteurFenetre * 0.37,couleur = '#FF00FF')#SLOT 5
    texte(largeurFenetre * 0.60, hauteurFenetre * 0.30,"SLOT 5",couleur="White",police="Arial Black",taille = taille_txt)

    rectangle(largeurFenetre * 0.76, hauteurFenetre * 0.27, largeurFenetre * 0.97, hauteurFenetre * 0.37,couleur = '#FF00FF',)#SLOT 6
    texte(largeurFenetre * 0.81, hauteurFenetre * 0.30,"SLOT 6",couleur="White",police="Arial Black",taille = taille_txt)

    texte(largeurFenetre * 0.63,hauteurFenetre * 0.02,"SAVE GAME",couleur="White",police="Arial Black",taille = taille_txt,tag="save")

def menu_pause(pause,cooldown,plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu):


    save= None

    quitte = False
    while pause: #tant qu'on ne reappuie pas sur esc

        rectangle(rectangle_x, rectangle_y, rectangle_x + rectangle_largeur, rectangle_y + rectangle_hauteur, remplissage = '#111111', epaisseur = 0,tag="rect")
        texte((largeurFenetre*0.525)/2, (hauteurFenetre*0.10 + hauteurFenetre*0.30)/2, 'PAUSED', ancrage='center', couleur='White',police = 'Arial Black', taille = int(taille_txt),tag="pause")

        if boutons_save(largeurFenetre, hauteurFenetre): # on genère les 6 boutons qui nous permettront de sauvegarder notre partie
            save= True
            save_slot()

        if save:
            
            
            # on regarde si un des 6 boutons a été pressé

            if boutons_slot1(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save1.json")
                print(f"sauvegardé dans save1.json")

            elif boutons_slot2(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save2.json")
                print(f"sauvegardé dans save2.json")

            elif boutons_slot3(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save3.json")
                print(f"sauvegardé dans save3.json")

            elif boutons_slot4(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save4.json")
                print(f"sauvegardé dans save4.json")
            
            elif boutons_slot5(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save5.json")
                print(f"sauvegardé dans save5.json")
            
            elif boutons_slot6(largeurFenetre,hauteurFenetre):    

                dico_save= recup_donnees(plateau,coord_pieces_placer,score, niveau, compteur_ligne,mode_de_jeu)
                stocker_donnees(dico_save,"save6.json")
                print(f"sauvegardé dans save6.json")

        
        if boutons_leave_game(largeurFenetre, hauteurFenetre):
            efface_tout()
            return True


        texte((largeurFenetre*0.55)/2, (hauteurFenetre*0.80 + hauteurFenetre*0.90)/2, 'press <esc> for resume', ancrage='center', couleur='White',police = 'Arial Black', taille = int(taille_txt)//2,tag="esc")
        
        mise_a_jour()

        if touche_pressee('Escape') and time() >= cooldown:
            pause= not(pause)

            #on supprime tout ce qu'on a tracé
            efface('rect')
            efface('pause')
            efface('esc')
            efface("save")
            efface("quit")
            efface("load")

            efface("bout")
        mise_a_jour()

    return quitte