def collision(plateau, coord_piece, res):
    """
    Vérifie la collision entre la pièce en cours et les pièces déjà posées sur le plateau de jeu,
    elle permet aussi de voir si la pièce en cour peut ce deplacer.

    La fonction vérifie si la pièce en cours entre en collision avec d'autres pièces déjà placées 
    sur le plateau ou si elle atteint les bords du plateau. 
    Elle peut vérifier des collisions pour trois directions :
    - Le bas (`Bottom`), 
    - La gauche (`Left`),
    - La droite (`Right`).

    :param plateau: Une liste 2D représentant l'état actuel du plateau de jeu. .
    :param coord_piece: Une liste de sous_listes représentant les coordonnées de la pièce en cours, 
                         où chaque sous_liste est de la forme [x, y, couleur].
    :param res: Une chaîne de caractères qui spécifie la direction à vérifier. Elle peut être :
                - 'Bottom' pour vérifier la collision en bas de la pièce,
                - 'Left' pour vérifier la collision à gauche de la pièce,
                - 'Right' pour vérifier la collision à droite de la pièce.

    Renvoie 'True' si une collision est détectée dans la direction spécifiée, sinon 'False'.
    """
    
    coord_collision = []  # stockage des coordonnées des pièces déjà posées

    # Récupérer toutes les coordonnées des pièces déjà posées
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == 2:  # Si la case est occupée
                coord_collision.append((i, j))

    if res == 'Bottom':
        for x, y, _,t in coord_piece:
            # Vérifiez si la case en dessous est occupée ou si la pièce est au bord inférieur
            if x == len(plateau)-1 or (x + 1, y) in coord_collision or y == 0 or (x, y-1) in coord_collision or (x+1,y-1) in coord_collision :
                return True
        
    elif res == 'Left':
        for x, y, _,t in coord_piece:
            if y - 1 < 0 or (x, y - 1) in coord_collision:
                return True
    
    elif res == 'Right':
        for x, y, _,t in coord_piece:
            if x + 1 >= len(plateau[0]) or (x+1, y) in coord_collision:
                return True

    return False