def deplacement(plateau, coord_piece, touche):

    """
    Déplace la pièce en cours vers la gauche ou la droite, en fonction de la touche pressée,
    et met à jour le plateau.

    La fonction efface d'abord les coordonnées de la pièce actuelle sur le plateau, puis déplace la pièce
    dans la direction spécifiée (gauche ou droite) si les conditions sont remplies (la pièce ne touche pas les bords du plateau).
    Ensuite, elle met à jour les nouvelles positions de la pièce sur le plateau.

    :param plateau: Une liste représentant l'état actuel du plateau de jeu. .
    :param coord_piece: Une liste de listes représentant les coordonnées de la pièce en cours, où chaque élément
                         est une liste de la forme [x, y, couleur], avec x et y étant les coordonnées de la pièce.
    :param touche: Une chaîne de caractères indiquant la direction du déplacement. Peut être :
                   - "Right" pour déplacer la pièce vers la droite,
                   - "Left" pour déplacer la pièce vers la gauche.

    Renvoie Le plateau mis à jour avec la pièce déplacée dans la direction spécifiée.
    """

    # Effacer toutes les positions de la pièce actuelle
    for i in coord_piece:
        plateau[i[0]][i[1]] = 0

    # Vérifier les conditions pour le déplacement
    
    if touche == "Right" and all(i[1] < len(plateau[0]) - 1 for i in coord_piece):
        # Déplacer chaque coordonnée vers la droite
        for i in range(len(coord_piece)):
            coord_piece[i][1] += 1

    elif touche == "Left" and all(i[1] > 0 for i in coord_piece):
        # Déplacer chaque coordonnée vers la gauche
        for i in range(len(coord_piece)):
            coord_piece[i][1] -= 1

    # Mettre à jour les nouvelles positions de la pièce sur le plateau
    for i in coord_piece:
        plateau[i[0]][i[1]] = 1

    return plateau
    