def placer_piece(plateau,couleur_piece,tag):

    """
    Place une pièce sur le plateau de jeu en ajoutant ses coordonnées et sa couleur.
    La fonction parcourt le plateau pour trouver les cases occupées par la pièce 
    (celles marquées par `1`), puis les ajoute à une liste des coordonnées des pièces placées. 
    Ensuite, elle marque ces cases comme étant définitivement occupées (en les passant à `2`).

    Paramètres :
    - plateau: Le plateau de jeu actuel.
    - couleur_piece: La couleur de la pièce à placer. 

    Renvoie :
    - coord_piece_placer: Une liste des coordonnées de la pièce placée sur le plateau. 
      Chaque élément de cette liste est une sous-liste `[i, j, couleur_piece]`, où `i` et `j` sont les 
      coordonnées de la case et `couleur_piece` est la couleur associée.
    - plateau: Le plateau mis à jour, avec les cases occupées par la pièce maintenant marquées comme `2`.

    """
    coord_piece_placer = []
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == 1:
                coord_piece_placer.append([i,j,couleur_piece,tag])
                plateau[i][j] = 2
    return coord_piece_placer, plateau