from module.fltk import *


def verifie_lignes(plateau, coord_pieces_placer):

    """
    Vérifie si des lignes sont complètes sur le plateau et les supprime si nécessaire,
    en ajustant les positions des pièces placées au-dessus des lignes supprimées.

    La fonction parcourt chaque ligne du plateau pour vérifier si elle est complète. Si une ligne est
    complète, elle est supprimée, les pièces placées au-dessus de la ligne supprimée sont déplacées vers le bas,
    et le score est mis à jour en fonction du nombre de lignes supprimées..

    :param plateau: Une liste représentant l'état du plateau de jeu. Chaque élément du plateau peut être :

    :param coord_pieces_placer: Une liste de listes de coordonnées représentant les pièces déjà placées sur le plateau,
                                 où chaque élément est une sous-liste contenant les coordonnées [x, y, couleur] des cases occupées par une pièce.
    Renvoie plusieurs element :
             - 'score': Le score mis à jour en fonction des lignes supprimées.
             - 'compteur_l_supprimees': Le nombre de lignes supprimées.
             - 'plateau': Le plateau mis à jour après la suppression des lignes.
             - 'coord_pieces_placer': Les coordonnées des pièces placées mises à jour après le déplacement des pièces au-dessus.
    """

    score= 0
    compteur_l_supprimees= 0
    ancien_coord_pieces_placer = coord_pieces_placer[:]
    n = len(plateau[0])
    for i in range(len(plateau)):  # on parcourt les lignes du plateau
        c = sum(1 for j in plateau[i] if j == 2) # compte les cases remplies
        if c == n:  # on regarde si la ligne est complète
            compteur_l_supprimees += 1
            
            # Supprime les éléments de la ligne remplie de coord_pieces_placer
            for k in range(len(coord_pieces_placer)): # on ajoute la ligne supprimé dans le tableau
                coord_pieces_placer[k] = [ coord for coord in coord_pieces_placer[k] if coord[0] != i]

            coord_pieces_placer = [coord for coord in coord_pieces_placer if coord != []]
            
            plateau = [[0 for i in range(10)]for j in range(20)]

            # Appelle la fonction pour ajuster les lignes restantes
            ajuste_ligne(coord_pieces_placer, i)

            for k in range(len(coord_pieces_placer)):
                for l in range(len(coord_pieces_placer[k])):
                    plateau[coord_pieces_placer[k][l][0]][coord_pieces_placer[k][l][1]] = 2

            if compteur_l_supprimees == 1:
                score += 40
            elif compteur_l_supprimees == 2:
                score += 100
            elif compteur_l_supprimees == 3:
                score += 300
            elif compteur_l_supprimees == 4:
                score += 500
        
    return score, compteur_l_supprimees, plateau, coord_pieces_placer ,ancien_coord_pieces_placer



def ajuste_ligne(coord_pieces_placer, i):

    """
    Ajuste les coordonnées des pièces placées au-dessus de la ligne supprimée en les déplaçant vers le bas d'une ligne.

    Cette fonction parcourt les coordonnées des pièces placées sur le plateau et, si la coordonnée d'une pièce est
    située au-dessus de la ligne supprimée, elle incrémente sa position sur l'axe des ordonnées (x).

    :param coord_pieces_placer: Une liste de listes de coordonnées représentant les pièces déjà placées sur le plateau.
                                 Chaque élément est une sous-liste contenant les coordonnées [x, y, couleur] des cases occupées par une pièce.
    :param i: L'index de la ligne supprimée. Toutes les pièces au-dessus de cette ligne auront leur position ajustée.

    Renvoie la liste `coord_pieces_placer` mise à jour avec les coordonnées des pièces déplacées vers le bas.
    """
     
    # Incrémente les lignes au-dessus de la ligne supprimée
    for k in range(len(coord_pieces_placer)):
        for l in range(len(coord_pieces_placer[k])):
            if coord_pieces_placer[k][l][0] < i:
                coord_pieces_placer[k][l][0] += 1
    return coord_pieces_placer