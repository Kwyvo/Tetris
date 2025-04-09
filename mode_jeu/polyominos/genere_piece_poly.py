from random import randint

global couleur
couleur = ""

global num_piece
num_piece = 0



def piece_polyominos(fichier):
    """
    Fonction qui parcourt un fichier et qui transforme les "+" en pièces.
    Si il y a un espace entre deux lignes, il s'agit d'une autre pièce


    La fonction retourne une liste contenant :
        - Une liste contenant toute les pièces
        
    """

    l = []
    piece = []
    with open(fichier,'r') as f1:
        tout_ligne_fichier = f1.readlines()
        for i in range(len(tout_ligne_fichier)):
            ligne_piece = []
            if '+' in tout_ligne_fichier[i]:
                for char in tout_ligne_fichier[i].replace("\n",''):
                    if char == '+':
                        ligne_piece.append(1)
                    else:
                        ligne_piece.append(0)
                piece.append(ligne_piece)
            elif '+' not in tout_ligne_fichier[i] and piece != []:
                l.append(piece)
                piece = list()
        if piece != []:
            l.append(piece)

    for pieces in l:
        val = max(len(sous_piece) for sous_piece in pieces)
        for sous_piece in pieces:
            while len(sous_piece) < val:
                sous_piece.append(0)   
    return l


def generer_piece():
    global couleur
    global num_piece


    """
    Génère une pièce aléatoire selon les pièces des polyminos avec une couleur aléatoire.

    La fonction retourne une liste contenant :
        - La matrice représentant la forme de la pièce,
        - La couleur de la pièce,
        - Le nom de la pièce.
    """
    
    
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
    liste_piece = piece_polyominos("mode_jeu/polyominos/polyominos.txt")
    
    # Choisir une pièce aléatoire
    res = randint(0, len(liste_piece) - 1)
    num_piece +=1
    
    return [liste_piece[res],couleur,"polyominos",f"polyominos{num_piece}"]