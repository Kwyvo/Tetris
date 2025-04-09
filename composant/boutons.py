from module.fltk import *

def click_gauche(x1,x2,y1,y2):
    """ Fonction qui detecte si un click gauche à été effectuée dans une zone donnée 
        Renvoie True si oui, sinon False

     x1 : Coordonnée x du coin supérieur gauche de la zone.
     x2 : Coordonnée x du coin inférieur droit de la zone.
     y1 : Coordonnée y du coin supérieur gauche de la zone.
     y2 : Coordonnée y du coin inférieur droit de la zone.

     """

    ev = donne_ev()  # On attend un evenement

    # Vérifier si l'événement est un clic gauche
    if type_ev(ev) == 'ClicGauche':
        x_souris = abscisse(ev)
        y_souris = ordonnee(ev)

        # Vérification si le clic est dans la zone du bouton PLAY
        if x1 <= x_souris <= x2 and y1 <= y_souris <= y2:
            return True
        return False


def souris_sur(x1, x2, y1, y2):
    """ Fonction qui detecte si un le curseur de la souris est présente dans une zone donnée 
        Renvoie True si oui, sinon False
        
     x1 : Coordonnée x du coin supérieur gauche de la zone.
     x2 : Coordonnée x du coin inférieur droit de la zone.
     y1 : Coordonnée y du coin supérieur gauche de la zone.
     y2 : Coordonnée y du coin inférieur droit de la zone.

     """

    x_souris = abscisse_souris()
    y_souris = ordonnee_souris()

    #rectangle(x1,y1,x2,y2,couleur="red") permet de faire des tests
    if x1 <= x_souris <= x2 and y1 <= y_souris <= y2:
        return True
    return False

def boutons_play(largeurFenetre, hauteurFenetre):
    """
    Fonction qui affiche et gère le bouton 'PLAY' dans l'interface de jeu.

    Dessine un bouton 'PLAY' et change la taille du texte lorsque la souris survole le bouton. 
    (Le dessin est automatique grâce aux dimensions de la fenêtre)

    Si un clic gauche est détecté dans la zone du bouton, la fonction renvoie `True`
    Son resultat est géré dans la fonction main.py .

    """

    taille_txt = int(15 * (hauteurFenetre*0.0025))
    if souris_sur(largeurFenetre*0.15, largeurFenetre*0.45,hauteurFenetre*0.20, hauteurFenetre*0.30) :
        texte((largeurFenetre*0.55)/2, (hauteurFenetre*0.20 + hauteurFenetre*0.30)/2, 'PLAY', ancrage='center', couleur='#FF00FF',police = 'Arial Black', taille = int(taille_txt+(4* (hauteurFenetre*0.0025))))
        if click_gauche(largeurFenetre*0.15, largeurFenetre*0.45,hauteurFenetre*0.20, hauteurFenetre*0.30):
            return True
    else:
        texte((largeurFenetre*0.55)/2, (hauteurFenetre*0.20 + hauteurFenetre*0.30)/2, 'PLAY', ancrage='center', couleur='#FF00FF',police = 'Arial Black',taille = int(taille_txt))
    
    
def boutons_exit(largeurFenetre, hauteurFenetre):
    """
    Fonction qui affiche et gère le bouton 'EXIT' dans l'interface de jeu.

    Dessine un bouton 'EXIT' et change la taille du texte lorsque la souris survole le bouton. 
    (Le dessin est automatique grâce aux dimensions de la fenêtre)

    Si un clic gauche est détecté dans la zone du bouton, la fonction renvoie `True` 
    Son resultat est géré dans la fonction main.py .
    
    """

    taille_txt = int(10 * (hauteurFenetre*0.0025))

    if souris_sur(largeurFenetre*0.17, largeurFenetre*0.37,hauteurFenetre*0.80, hauteurFenetre*0.90) :
        texte((largeurFenetre*0.55)/2, (hauteurFenetre*0.80 + hauteurFenetre*0.90)/2, 'EXIT', ancrage='center', couleur='#FF00FF',police = 'Arial Black', taille = int(taille_txt+(2* (hauteurFenetre*0.0025))))
        if click_gauche(largeurFenetre*0.17, largeurFenetre*0.37,hauteurFenetre*0.80, hauteurFenetre*0.90):
            return True
    else:
        texte((largeurFenetre*0.55)/2, (hauteurFenetre*0.80 + hauteurFenetre*0.90)/2, 'EXIT', ancrage='center', couleur='#FF00FF',police = 'Arial Black', taille = int(taille_txt))
    


couleur_bordure_bouton = "gray24"

def bouton_Casual(largeurFenetre,hauteurFenetre):
    taille_txt = 20

    if souris_sur(largeurFenetre*0.025, largeurFenetre*0.255,hauteurFenetre*0.30, hauteurFenetre*0.90) :

        image(largeurFenetre*0.14,hauteurFenetre*0.41,fichier="image/tetris_fond.png",hauteur=300,largeur=300)
        rectangle(largeurFenetre*0.023,hauteurFenetre*0.20,largeurFenetre*0.255,hauteurFenetre*0.90, couleur = 'white')
        
        rectangle(largeurFenetre*0.023,hauteurFenetre*0.60,largeurFenetre*0.255,hauteurFenetre*0.90, couleur = 'white',remplissage = "white")
        ligne(largeurFenetre*0.025,hauteurFenetre*0.92,largeurFenetre*0.255,hauteurFenetre*0.92, couleur = 'white')
        texte(largeurFenetre*0.14, hauteurFenetre*0.70, 'CASUAL', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = taille_txt + 2)
        if click_gauche(largeurFenetre*0.025, largeurFenetre*0.255,hauteurFenetre*0.20, hauteurFenetre*0.90):
            return True
    else:
        image(largeurFenetre*0.14,hauteurFenetre*0.51,"image/tetris_fond.png",hauteur=300,largeur=300)
        rectangle(largeurFenetre*0.023,hauteurFenetre*0.30,largeurFenetre*0.255,hauteurFenetre*0.90, couleur = couleur_bordure_bouton)
        
        rectangle(largeurFenetre*0.023,hauteurFenetre*0.60,largeurFenetre*0.255,hauteurFenetre*0.90, couleur = couleur_bordure_bouton, remplissage = couleur_bordure_bouton)
        texte(largeurFenetre*0.14, hauteurFenetre*0.70, 'CASUAL', ancrage='center', couleur='white',police = 'Arial Black', taille = taille_txt)


def bouton_pourrissement(largeurFenetre,hauteurFenetre):
    taille_txt = 20

    if souris_sur(largeurFenetre*0.265, largeurFenetre*0.495,hauteurFenetre*0.30, hauteurFenetre*0.90) :
        image(largeurFenetre*0.38,hauteurFenetre*0.41,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.38,hauteurFenetre*0.38,"image/chronometre-2.png",hauteur=180,largeur=180)
        rectangle(largeurFenetre*0.265,hauteurFenetre*0.20,largeurFenetre*0.495,hauteurFenetre*0.90, couleur = 'white')
        rectangle(largeurFenetre*0.265,hauteurFenetre*0.60,largeurFenetre*0.495,hauteurFenetre*0.90, couleur = 'white',remplissage = "white")
        ligne(largeurFenetre*0.265,hauteurFenetre*0.92,largeurFenetre*0.495,hauteurFenetre*0.92, couleur = 'white')
        texte(largeurFenetre*0.38, hauteurFenetre*0.70, 'POURRISSEMENT', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = taille_txt + 2)
        
        texte(largeurFenetre*0.38, hauteurFenetre*0.76, 'Un bloc aléatoiredisparaît  ', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.38, hauteurFenetre*0.80, ' périodiquement,de plus' , ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.38, hauteurFenetre*0.84, ' en plus vite à haut niveau.', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        if click_gauche(largeurFenetre*0.265, largeurFenetre*0.495,hauteurFenetre*0.30, hauteurFenetre*0.90):
            return True
    else:
        image(largeurFenetre*0.38,hauteurFenetre*0.51,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.38,hauteurFenetre*0.46,"image/chronometre-2.png",hauteur=180,largeur=180)
        rectangle(largeurFenetre*0.2635,hauteurFenetre*0.30,largeurFenetre*0.495,hauteurFenetre*0.90, couleur = couleur_bordure_bouton)
        rectangle(largeurFenetre*0.2635,hauteurFenetre*0.60,largeurFenetre*0.495,hauteurFenetre*0.90, couleur = couleur_bordure_bouton, remplissage = couleur_bordure_bouton)
        texte(largeurFenetre*0.38, hauteurFenetre*0.70, 'POURRISSEMENT', ancrage='center', couleur='white',police = 'Arial Black', taille = taille_txt)

 



def bouton_2joueur(largeurFenetre,hauteurFenetre):
    taille_txt = 20

    if souris_sur(largeurFenetre*0.505, largeurFenetre*0.735,hauteurFenetre*0.30, hauteurFenetre*0.90) :

        image(largeurFenetre*0.6215,hauteurFenetre*0.41,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.625,hauteurFenetre*0.41,"image/vs1.png",largeur = 300,hauteur=300)

        rectangle(largeurFenetre*0.505,hauteurFenetre*0.20,largeurFenetre*0.737,hauteurFenetre*0.90, couleur = 'white')
        rectangle(largeurFenetre*0.505,hauteurFenetre*0.60,largeurFenetre*0.737,hauteurFenetre*0.90, couleur = 'white',remplissage = "white")

        ligne(largeurFenetre*0.505,hauteurFenetre*0.92,largeurFenetre*0.737,hauteurFenetre*0.92, couleur = 'white')
        texte(largeurFenetre*0.625, hauteurFenetre*0.70, '2 PLAYERS', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = taille_txt + 2)

        texte(largeurFenetre*0.625, hauteurFenetre*0.76, 'Les lignes supprimées ajoutent', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.625, hauteurFenetre*0.80, 'des lignes trouées au ' , ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.625, hauteurFenetre*0.84, 'plateau de l’adversaire.' , ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)

        if click_gauche(largeurFenetre*0.505, largeurFenetre*0.735,hauteurFenetre*0.30, hauteurFenetre*0.90):
            return True
    else:
        image(largeurFenetre*0.6215,hauteurFenetre*0.51,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.625,hauteurFenetre*0.46,"image/vs1.png",largeur = 300,hauteur=300)

        rectangle(largeurFenetre*0.505,hauteurFenetre*0.30,largeurFenetre*0.737,hauteurFenetre*0.90, couleur = couleur_bordure_bouton)
        rectangle(largeurFenetre*0.505,hauteurFenetre*0.60,largeurFenetre*0.737,hauteurFenetre*0.90, couleur = couleur_bordure_bouton,remplissage = couleur_bordure_bouton)
        texte(largeurFenetre*0.625, hauteurFenetre*0.70, '2 PLAYERS', ancrage='center', couleur='white',police = 'Arial Black', taille = taille_txt)
        texte(largeurFenetre*0.625, hauteurFenetre*0.80, 'BETA TEST', ancrage='center', couleur='white',police = 'Arial Black', taille = taille_txt-5)




def bouton_polyominos(largeurFenetre,hauteurFenetre):
    taille_txt = 20

    if souris_sur(largeurFenetre*0.745, largeurFenetre*0.975,hauteurFenetre*0.30, hauteurFenetre*0.90) :
        image(largeurFenetre*0.8615,hauteurFenetre*0.41,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.8625,hauteurFenetre*0.41,"image/polyominos.png",hauteur=190,largeur=300)

        rectangle(largeurFenetre*0.745,hauteurFenetre*0.20,largeurFenetre*0.976,hauteurFenetre*0.90, couleur = 'white')
        rectangle(largeurFenetre*0.745,hauteurFenetre*0.60,largeurFenetre*0.976,hauteurFenetre*0.90, couleur = 'white',remplissage = "white")

        ligne(largeurFenetre*0.745,hauteurFenetre*0.92,largeurFenetre*0.975,hauteurFenetre*0.92,couleur = 'white')

        texte(largeurFenetre*0.865, hauteurFenetre*0.70, 'POLYOMINOS', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = taille_txt + 2)

        texte(largeurFenetre*0.865, hauteurFenetre*0.76, 'Les joueurs utilisent des formes', ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.865, hauteurFenetre*0.80, 'personnalisées définies dans' , ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        texte(largeurFenetre*0.865, hauteurFenetre*0.84, 'un fichier avec des blocs +' , ancrage='center', couleur=couleur_bordure_bouton,police = 'Arial Black', taille = 12)
        if click_gauche(largeurFenetre*0.745, largeurFenetre*0.975,hauteurFenetre*0.30, hauteurFenetre*0.90):
            return True
    else:
        image(largeurFenetre*0.8615,hauteurFenetre*0.51,"image/tetris_fond.png",hauteur=300,largeur=300)
        image(largeurFenetre*0.8625,hauteurFenetre*0.46,"image/polyominos.png",hauteur=190,largeur=300)
        rectangle(largeurFenetre*0.745,hauteurFenetre*0.30,largeurFenetre*0.976,hauteurFenetre*0.90, couleur = couleur_bordure_bouton)
        rectangle(largeurFenetre*0.745,hauteurFenetre*0.60,largeurFenetre*0.976,hauteurFenetre*0.90, couleur = couleur_bordure_bouton,remplissage=couleur_bordure_bouton)
        texte(largeurFenetre*0.865, hauteurFenetre*0.70, 'POLYOMINOS', ancrage='center', couleur='white',police = 'Arial Black', taille = taille_txt)


# BOUTONS PARAMETRE-------------------------------

def boutons_para(largeurFenetre, hauteurFenetre):

    if souris_sur(largeurFenetre* 0.90, largeurFenetre-1, hauteurFenetre* 0.90, hauteurFenetre-1):

        if click_gauche(largeurFenetre* 0.90, largeurFenetre-1, hauteurFenetre* 0.90, hauteurFenetre-1):
            return True
    
    



# BOUTONS SAVE------------------------------------

def boutons_save(largeurFenetre, hauteurFenetre):
    """
    Fonction qui affiche et gère le bouton 'SAVE' dans l'interface de jeu.

    Dessine un bouton 'SAVE' et change la couleur du texte lorsque la souris survole le bouton. 
    (Le dessin est automatique grâce aux dimensions de la fenêtre)

    Si un clic gauche est détecté dans la zone du bouton, la fonction renvoie `True` 
    Son resultat est géré dans la fonction main.py .
    
    """
 

    taille_txt = int(10 * (hauteurFenetre*0.0025))

    if souris_sur(largeurFenetre*0.15, largeurFenetre*0.37, hauteurFenetre*0.43, hauteurFenetre*0.50):

        #rectangle(largeurFenetre*0.17, hauteurFenetre*0.25, largeurFenetre*0.37, hauteurFenetre*0.50, couleur = "#FF00FF")
        texte((largeurFenetre*0.525)/2, (hauteurFenetre*0.50 + hauteurFenetre*0.90)/3, 'SAVE GAME', ancrage='center', couleur='#FF00FF',police = 'Fixedsys', taille = int(taille_txt),tag="save")

        if click_gauche(largeurFenetre*0.15, largeurFenetre*0.37, hauteurFenetre*0.43, hauteurFenetre*0.50):
            return True

    else:
        #rectangle(largeurFenetre*0.15, hauteurFenetre*0.43, largeurFenetre*0.37, hauteurFenetre*0.50, couleur = "green")
        texte((largeurFenetre*0.525)/2, (hauteurFenetre*0.50 + hauteurFenetre*0.90)/3, 'SAVE GAME', ancrage='center', couleur='White',police = 'Fixedsys', taille = int(taille_txt),tag="save")



def boutons_leave_game(largeurFenetre, hauteurFenetre):
    """
    Fonction qui affiche et gère le bouton 'SAVE' dans l'interface de jeu.

    Dessine un bouton 'SAVE' et change la couleur du texte lorsque la souris survole le bouton. 
    (Le dessin est automatique grâce aux dimensions de la fenêtre)

    Si un clic gauche est détecté dans la zone du bouton, la fonction renvoie `True` 
    Son resultat est géré dans la fonction main.py .
    
    """
    taille_txt = int(10 * (hauteurFenetre*0.0025))

    if souris_sur(largeurFenetre*0.15, largeurFenetre*0.37,hauteurFenetre*0.60, hauteurFenetre*0.70) :

        texte(largeurFenetre*0.26, hauteurFenetre*0.65, 'QUIT', ancrage='center', couleur='#FF00FF',police = 'Fixedsys', taille = int(taille_txt),tag="quit")

        if click_gauche(largeurFenetre*0.15, largeurFenetre*0.37,hauteurFenetre*0.60, hauteurFenetre*0.70):
            return True

    else:
        texte(largeurFenetre*0.26, hauteurFenetre*0.65, 'QUIT', ancrage='center', couleur='White',police = 'Fixedsys', taille = int(taille_txt),tag="quit")


def boutons_slot1(largeurFenetre, hauteurFenetre):
   
    

    if souris_sur(largeurFenetre * 0.55, largeurFenetre * 0.76,hauteurFenetre*0.07, hauteurFenetre*0.17,) :
        

        if click_gauche(largeurFenetre * 0.55, largeurFenetre * 0.76,hauteurFenetre*0.07, hauteurFenetre*0.17):
            return True


def boutons_slot2(largeurFenetre, hauteurFenetre):
   
   

    if souris_sur(largeurFenetre * 0.76, largeurFenetre * 0.97,hauteurFenetre * 0.07 , hauteurFenetre * 0.17) :

        if click_gauche(largeurFenetre * 0.76, largeurFenetre * 0.97,hauteurFenetre * 0.07 , hauteurFenetre * 0.17):
            return True


def boutons_slot3(largeurFenetre, hauteurFenetre):
   
    

    if souris_sur(largeurFenetre * 0.55,largeurFenetre * 0.76,hauteurFenetre * 0.17, hauteurFenetre * 0.27) :

        if click_gauche(largeurFenetre * 0.55,largeurFenetre * 0.76,hauteurFenetre * 0.17, hauteurFenetre * 0.27):
            return True


def boutons_slot4(largeurFenetre, hauteurFenetre):
   
   

    if souris_sur(largeurFenetre * 0.76, largeurFenetre * 0.97, hauteurFenetre * 0.17, hauteurFenetre * 0.27) :

        if click_gauche(largeurFenetre * 0.76, largeurFenetre * 0.97, hauteurFenetre * 0.17, hauteurFenetre * 0.27):
            return True


def boutons_slot5(largeurFenetre, hauteurFenetre):
   


    if souris_sur(largeurFenetre * 0.55, largeurFenetre * 0.76,hauteurFenetre * 0.27,hauteurFenetre * 0.37) :

        if click_gauche(largeurFenetre * 0.55, largeurFenetre * 0.76,hauteurFenetre * 0.27,hauteurFenetre * 0.37):
            return True


def boutons_slot6(largeurFenetre, hauteurFenetre):
   

    if souris_sur(largeurFenetre * 0.76,largeurFenetre * 0.97,hauteurFenetre * 0.27, hauteurFenetre * 0.37) :

        if click_gauche(largeurFenetre * 0.76,largeurFenetre * 0.97,hauteurFenetre * 0.27, hauteurFenetre * 0.37):
            return True



def bouton_plus(x1,y1,x2,y2):

    #rectangle(x1,y1,x2,y2,remplissage="green")
    if souris_sur(x1,x2,y1,y2) :
        
        if click_gauche(x1,x2,y1,y2):
            return True

def bouton_moins(x1,y1,x2,y2):

    #rectangle(x1,y1,x2,y2,remplissage="red")
    if souris_sur(x1,x2,y1,y2) :

        if click_gauche(x1,x2,y1,y2):
            return True

def bouton_save_para(largeurFenetre, hauteurFenetre):


    rectangle(largeurFenetre*0.288,hauteurFenetre*0.86,largeurFenetre*0.45,hauteurFenetre*0.91,remplissage="grey",tag="apply")
    if souris_sur(largeurFenetre*0.288,largeurFenetre*0.45,hauteurFenetre*0.86,hauteurFenetre*0.91) :

        if click_gauche(largeurFenetre*0.288,largeurFenetre*0.45,hauteurFenetre*0.86,hauteurFenetre*0.91):
            return True



