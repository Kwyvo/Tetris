from module.fltk import *
from composant.boutons import boutons_para,bouton_plus,bouton_moins,bouton_save_para
from sauvegarde.sauvegarde import *
from time import *

#parametres de bases:
vitesse_save= charger_donnees("para.json")["vitesse"]

dimension= charger_donnees("para.json")["dimension_fen"]
hauteurFenetre = dimension[0]
largeurFenetre = dimension[1]


# Dimensions du plateau
plateau = [[0 for i in range(10)] for j in range(20)]
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



def menu_para(test):

    global vitesse_save,largeurFenetre,hauteurFenetre
    hauteur= hauteurFenetre
    largeur=largeurFenetre
    vitesse= vitesse_save


    dimension= charger_donnees("para.json")["dimension_fen"]
    hauteur,hauteurFenetre = dimension[0],dimension[0]
    largeur,largeurFenetre = dimension[1],dimension[1]
    taille_txt = int(10 * (hauteurFenetre*0.0025))


    while test:
        rectangle(largeurFenetre*0.287,hauteurFenetre*0.13,largeurFenetre*0.716,hauteurFenetre*0.86,remplissage="grey",tag="para")
        texte(largeurFenetre*0.50, hauteurFenetre*0.20, 'SETTINGS', ancrage='center', couleur='white',police = 'Fixedsys', taille = int(1.25* taille_txt),tag="titre")
        texte(largeurFenetre*0.30,hauteurFenetre*0.86,'Apply',police = 'Fixedsys',couleur='white', taille = int(1.25* taille_txt))

        #changer la vitesse --------------
        texte(largeurFenetre*0.40, hauteurFenetre*0.40, 'Vitesse', ancrage='center', couleur='white',police = 'Fixedsys', taille = int(1.25* taille_txt),tag="categorie")
        texte(largeurFenetre * 0.48, (hauteurFenetre * 0.42 + hauteurFenetre * 0.475)/2,f"{vitesse}",police = "Arial Black",taille = taille_txt,couleur = 'white',tag="valeur")
        texte(largeurFenetre*0.45,hauteurFenetre*0.455,'-',couleur="white",tag="change")
        texte(largeurFenetre*0.55,hauteurFenetre*0.46,'+',couleur="white",tag="change")

        if bouton_moins(largeurFenetre*0.45,hauteurFenetre*0.455,largeurFenetre*0.5,hauteurFenetre*0.51):
            if vitesse > 0.0:
                vitesse -= 0.1
                vitesse= round(vitesse,1)
            

        elif bouton_plus(largeurFenetre*0.55,hauteurFenetre*0.46,largeurFenetre*0.60,hauteurFenetre*0.51):
            vitesse += 0.1
            vitesse= round(vitesse,1)

        #--------------------------------

        #changer les dimensions de la fenetre
        texte(largeurFenetre*0.42, hauteurFenetre*0.60, 'Dimension', ancrage='center', couleur='white',police = 'Fixedsys', taille = int(1.25*taille_txt),tag="categorie")
        texte(largeurFenetre * 0.43, (hauteurFenetre * 0.83 + hauteurFenetre * 0.475)/2,f"{largeur}",police = "Arial Black",taille = taille_txt,couleur = 'white',tag="valeur")
        texte(largeurFenetre * 0.54, (hauteurFenetre * 0.83 + hauteurFenetre * 0.475)/2,f"{hauteur}",police = "Arial Black",taille = taille_txt,couleur = 'white',tag="valeur")
        texte(largeurFenetre*0.40,hauteurFenetre*0.655,'-',couleur="white",tag="change")
        texte(largeurFenetre*0.64,hauteurFenetre*0.66,'+',couleur="white",tag="change")

        if bouton_moins(largeurFenetre*0.39,hauteurFenetre*0.67,largeurFenetre*0.42,hauteurFenetre*0.7):
            if hauteur > 500 and largeur > 500:
                
                hauteur -=100
                largeur -=100
                

                mise_a_jour()
            

        elif bouton_plus(largeurFenetre*0.64,hauteurFenetre*0.67,largeurFenetre*0.68,hauteurFenetre*0.7):
            if hauteur < 1000 and largeur < 1000:
                hauteur +=100
                largeur +=100

        

        #--------------------------------
        mise_a_jour()
        efface_tout()
        
        if boutons_para(largeurFenetre, hauteurFenetre) or bouton_save_para(largeurFenetre, hauteurFenetre):
            vitesse_save= vitesse
            efface("para")
            efface("titre")
            efface("categorie")
            efface("valeur")
            efface("change")
            efface("apply")

            dico_para = recup_donnees_para(vitesse,hauteur,largeur)
            stocker_donnees(dico_para,"para.json")

            test= not(test)

            return vitesse,hauteur,largeur


    