from module.fltk import *
from composant.boutons import *
from affichage.loading import loading_main
from mode_jeu.mode_deux_joueur.deux_joueurs import deux_joueurs
from mode_jeu.pourrissement import pourrissement_jeu
from mode_jeu.polyominos.polyominos import polyominos
from sauvegarde.sauvegarde import *
from jeu import jeu
import asyncio


def modes_menu(hauteurFenetre,largeurFenetre):
    
    efface_tout()
    redimensionne_fenetre(largeurFenetre, hauteurFenetre)


    dimension= charger_donnees("para.json")["dimension_fen"]
    hauteur = dimension[0]
    largeur = dimension[1]
    
    mod_jeu = ""
    

    while mod_jeu == "":
        image(largeurFenetre*0.5,hauteurFenetre*0.5,"image/mode_menu_fond.jpg",hauteur=720,largeur=1300)
        texte(largeurFenetre*0.02,hauteurFenetre*0.025,"GAME MODE",couleur="white",taille=50,police="Arial Black",style="italic")
        ligne(largeurFenetre*0.02,hauteurFenetre*0.15,largeurFenetre*0.98,hauteurFenetre*0.15,couleur="white")

        
        
        if bouton_Casual(largeurFenetre,hauteurFenetre):
            mod_jeu = "Casual"
        elif bouton_pourrissement(largeurFenetre,hauteurFenetre):
            mod_jeu = "pourrissement"
        elif bouton_2joueur(largeurFenetre,hauteurFenetre):
            mod_jeu = "2joueur"
        elif bouton_polyominos(largeurFenetre,hauteurFenetre):
            mod_jeu = "polyominos"

        if mod_jeu == "Casual":
            efface_tout()
            asyncio.run(loading_main(hauteurFenetre,largeurFenetre)) #On lance l'animation de chargement
            efface_tout()
            redimensionne_fenetre(hauteur, largeur)
            jeu(hauteur,largeur)
            
        elif mod_jeu == "2joueur":
            #animation_play(hauteurFenetre, largeurFenetre, 0,1,0)
            efface_tout()
            asyncio.run(loading_main(hauteurFenetre,largeurFenetre)) #On lance l'animation de chargement
            efface_tout()
            asyncio.run(deux_joueurs(hauteurFenetre, largeurFenetre)) #On lance le jeu 

        elif mod_jeu == "pourrissement":
            efface_tout()
            asyncio.run(loading_main(hauteurFenetre,largeurFenetre)) #On lance l'animation de chargement
            efface_tout()
            redimensionne_fenetre(hauteur, largeur)
            pourrissement_jeu(hauteur, largeur)
        elif mod_jeu == "polyominos":
            efface_tout()
            redimensionne_fenetre(hauteur, largeur)
            polyominos(hauteur, largeur)
        
        else:
            ev = donne_ev()
            if type_ev(ev) == 'Quitte':
                ferme_fenetre()

        
        mise_a_jour()
        efface_tout()



