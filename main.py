# -------Importation-------
from time import *
from module.fltk import *

from affichage.loading import loading_main
from affichage.menu import menu
from affichage.animation_play import animation_play
from affichage.mod_menu import modes_menu
from sauvegarde.sauvegarde import *
from jeu import jeu
import argparse
from jeu_ia import jeu_ia
from tetris_rota.jeu_rota import jeu_rota


# -------------------------
def main():

    # -----Création Fenêtre----
    dimension= charger_donnees("para.json")["dimension_fen"]
    hauteurFenetre = dimension[0]
    largeurFenetre = dimension[1]
    cree_fenetre(largeurFenetre, hauteurFenetre, color= "gray5", title='TETRIS', icon='image/Tetris_logo.png')
    # -------------------------

    lancer_jeu = None
    plateau= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 2, 2, 2], [2, 2, 2, 0, 0, 0, 0, 2, 2, 2], [2, 2, 2, 0, 0, 0, 0, 0, 2, 2]]

    
    #------------------------------------
    while True:
        
        dimension= charger_donnees("para.json")["dimension_fen"]
        hauteurFenetre = dimension[0]
        largeurFenetre = dimension[1]
       


        lancer_jeu = menu(hauteurFenetre, largeurFenetre, score=0, niveau=1, compteur_ligne=0)
        if lancer_jeu == "PLAY":
            modes_menu(720,1300) #On lance le menu des modes de jeu

            #Quand le jeu fini on remet les paramètres par default
            lancer_jeu = None
            redimensionne_fenetre(largeurFenetre, hauteurFenetre)
        else:
            ev = donne_ev()
            if type_ev(ev) == 'Quitte':
                ferme_fenetre()

        mise_a_jour()



if __name__ == '__main__':


    dimension = charger_donnees("para.json")["dimension_fen"]
    hauteurFenetre = dimension[0]
    largeurFenetre = dimension[1]


    parser = argparse.ArgumentParser(description="Modes pour le jeu.")
    parser.add_argument("--ia", action="store_true", help="Activer le mode IA")
    parser.add_argument("--rota", action="store_true", help="Activer le mode rota")
    args = parser.parse_args()


    if args.ia:
        cree_fenetre(largeurFenetre, hauteurFenetre, color="gray5", title='TETRIS', icon="")
        jeu_ia(hauteurFenetre, largeurFenetre)

    elif args.rota:
        cree_fenetre(largeurFenetre, hauteurFenetre, color="gray5", title='TETRIS', icon="")
        jeu_rota(hauteurFenetre, largeurFenetre)

    else:
        main()

     