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
    ancien_coord_pieces_placer = coord_pieces_placer[:] #coordonnées des pieces placées avant modifications
    coord_pieces_placer_temp = ancien_coord_pieces_placer[:]
    i = len(plateau)-1
    compteur = 1
    
    while compteur <= len(plateau):
        bloc_a_supp=[] #blocs sur la meme diagonale
        j = 0
        i_temp = i
        while i_temp <= len(plateau)-1: #on recupere les coord des pieces sur la meme diagonale
            if plateau[i_temp][j] == 2:
                bloc_a_supp.append((i_temp,j))
            i_temp+=1
            j+=1
        
        if len(bloc_a_supp) == compteur: #si la diagonale est complète
            compteur_l_supprimees +=1
            for elt in bloc_a_supp: #on supprime les blocs de la diagonale complète
                plateau[elt[0]][elt[1]] = 0
            coord_pieces_placer_temp = [[bloc for bloc in piece if (bloc[0], bloc[1]) not in bloc_a_supp]for piece in coord_pieces_placer_temp]
            
            score += 100 
        coord_pieces_placer = coord_pieces_placer_temp[:]

        
        if not 2 in plateau[len(plateau)-1] and all(plateau[k][0] != 2 for k in range(len(plateau)-1)): #si la ligne du bas est vide et que la premiere colonne est vide
            coord_pieces_placer = ajuste_ligne(coord_pieces_placer,plateau)
            plateau = [[0 for i in range(len(plateau[0]))] for j in range(len(plateau))]
            for piece in coord_pieces_placer: #on replace les pièces sur le plateau avec leurs nouvelles coordonnées
                for bloc in piece:
                    plateau[bloc[0]][bloc[1]] = 2
        
        compteur+=1
        i-=1

    return score, compteur_l_supprimees, plateau, coord_pieces_placer ,ancien_coord_pieces_placer



def ajuste_ligne(coord_pieces_placer,plateau):

    """
    Ajuste les coordonnées des pièces placées au-dessus de la ligne supprimée en les déplaçant vers le bas d'une ligne.

    Cette fonction parcourt les coordonnées des pièces placées sur le plateau et, si la coordonnée d'une pièce est
    située au-dessus de la ligne supprimée, elle incrémente sa position sur l'axe des ordonnées (x).

    :param coord_pieces_placer: Une liste de listes de coordonnées représentant les pièces déjà placées sur le plateau.
                                 Chaque élément est une sous-liste contenant les coordonnées [x, y, couleur] des cases occupées par une pièce.

    Renvoie la liste `coord_pieces_placer` mise à jour avec les coordonnées des pièces déplacées vers le bas.
    """
    
    # Incrémente les lignes au-dessus de la diagonale supprimée
    chute = True
    for k in range(len(coord_pieces_placer)):
        for l in range(len(coord_pieces_placer[k])):
            if (coord_pieces_placer[k][l][0] + 1) < len(plateau) or (coord_pieces_placer[k][l][1] - 1) >= 0: #si la pièce ne sort pas du plateau
                coord_pieces_placer[k][l][0] += 1
                coord_pieces_placer[k][l][1] -= 1
            else: #si la pièce sort du plateau on arrete de deplacer les pieces
                chute = False 
                break
        if not chute:
            break
    return coord_pieces_placer
