def rotation(plateau, coord_piece, coord_pieces_placer, piece, i_index):

    """
    Effectue la rotation de la pièce actuelle autour de son centre et met à jour 
    le plateau en fonction de la nouvelle orientation. Si la rotation entraîne une collision ou un 
    dépassement du bord du plateau, la rotation est annulée.


    Paramètres :
    - plateau: Le plateau de jeu actuel.
    - coord_piece: La liste des coordonnées actuelles de la pièce.
    - coord_pieces_placer: La liste des coordonnées des pièces déjà placées sur le plateau.
    - piece: Une liste
    - i_index (int): L'indice de la ligne où la rotation doit commencer.

    Renvoie :
    - plateau2: Le nouveau plateau après la rotation de la pièce, avec les cases mises à jour.
    - nv_coord_piece: Les nouvelles coordonnées de la pièce après rotation.
    - len(nv_piece): La taille de la nouvelle pièce.
    - nv_piece: La matrice de la pièce après rotation.

    Si la rotation est invalide, la fonction 
    renvoie les valeurs suivantes :
    - plateau : Le plateau inchangé.
    - coord_piece : Les coordonnées de la pièce avant la rotation.
    - len(pieces) : La taille d'origine de la pièce.
    - pieces : La matrice de la pièce avant la rotation.

    """
    # On récupère la matrice de la pièce actuelle
    pieces = piece[0]

    # Rotation de la pièce (pivot autour de son centre)
    nv_piece = [[0 for j in range(len(pieces))] for i in range(len(pieces[0]))]
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            nv_piece[j][len(pieces) - 1 - i] = pieces[i][j]

    # Création d'un nouveau plateau temporaire pour la nouvelle pièce
    plateau2 = [[0 for _ in range(len(plateau[0]))] for _ in range(len(plateau))]

    # Utiliser les coordonnées minimales en y pour aligner la nouvelle pièce avec la position d'origine
    ind_i = i_index
    y_min = min([coord[1] for coord in coord_piece])  # Coordonnée minimale en y
    try:
        for i in range(len(nv_piece)):
            ind_j = y_min  # Commencer avec y_min pour garder la même position horizontale
            for j in range(len(nv_piece[i])):
                if nv_piece[i][j] == 1:
                    plateau2[ind_i][ind_j] = 1
                ind_j += 1  # Avancer dans la ligne pour la prochaine colonne
            ind_i += 1  # Avancer vers la ligne suivante

    except IndexError:
        # Si la pièce sort du plateau, on annule la rotation
        return plateau, coord_piece, len(pieces), pieces

    # Récupération des nouvelles coordonnées de la pièce
    nv_coord_piece = []
    for i in range(len(plateau2)):
        for j in range(len(plateau2[i])):
            if plateau2[i][j] == 1:
                if plateau[i][j] == 2:  # Collision avec une autre pièce
                    return plateau, coord_piece, len(pieces), pieces
                nv_coord_piece.append([i, j, piece[1],piece[3]])

    # Remet les autres pièces déjà placées
    for i in range(len(coord_pieces_placer)):
        for j in range(len(coord_pieces_placer[i])):
            plateau2[coord_pieces_placer[i][j][0]][coord_pieces_placer[i][j][1]] = 2

    return plateau2, nv_coord_piece, len(nv_piece), nv_piece