from random import randint

global couleur
couleur = ""
global num_piece
num_piece = 0

def generer_piece():
    global couleur
    global num_piece

    """
    Génère une pièce aléatoire de Tetris avec une couleur aléatoire.

    La fonction sélectionne une forme de pièce parmi les pièces classiques de Tetris 
    (carré, barre, T, L, J, S, Z) et lui attribue une couleur aléatoire. Elle garantit 
    que la couleur générée est différente de la couleur précédente pour éviter une répétition immédiate.

    La fonction retourne une liste contenant :
        - La matrice représentant la forme de la pièce,
        - La couleur de la pièce,
        - Le nom de la pièce.
    """
    
    carre = [[1, 1], 
             [1, 1]]
    
    barre = [[1,1,1,1]]

    t_piece = [[0, 1, 0],
               [1, 1, 1]]
    
    l_piece = [[1, 0], 
               [1, 0],
               [1, 1]]
    
    j_piece = [[0, 1], 
               [0, 1],
               [1, 1]]
    
    s_piece = [[0, 1, 1], 
               [1, 1, 0]]
    
    z_piece = [[1, 1, 0],
               [0, 1, 1]]
    
    # Dictionnaire contenant toutes les pièces
    piece = {
        'carre': carre,
        'barre': barre,
        't_piece': t_piece,
        'l_piece': l_piece,
        'j_piece': j_piece,
        's_piece': s_piece,
        'z_piece': z_piece
    }
    
    couleurs = [
    "cyan",       
    "magenta2",    
    "red2",    
    "lawn green",      
    "yellow",        
    "purple",
    "orangered2",
    "blue3"           
    ]

    res_couleur = randint(0,len(couleurs)-1)

    while couleurs[res_couleur] == couleur : 
        res_couleur = randint(0,len(couleurs)-1)

    couleur = couleurs[res_couleur]
    # Liste des clés pour sélectionner une pièce aléatoire
    liste_piece = list(piece.keys())
    
    # Choisir une pièce aléatoire
    res = randint(0, len(liste_piece) - 1)
    num_piece +=1
    return [piece[liste_piece[res]],couleur,liste_piece[res],f"{liste_piece[res]}{num_piece}"]
