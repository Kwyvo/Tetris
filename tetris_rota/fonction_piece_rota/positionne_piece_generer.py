def positionne_piece_generer(plateau,piece):

    """
    Cette fonction place la pièce générée au sommet du plateau, centrée horizontalement.

    Paramètres :
    - plateau: Le plateau de jeu actuel.
    - piece: La pièce à positionner.

    Renvoie :
    - plateau: Le plateau mis à jour avec la pièce positionnée, avec les cases où la pièce est 
      placée marquées par `1`.
    """    
    for i in range(len(piece)):
        j_plateau = len(plateau[i]) - len(piece[0])
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                plateau[i][j_plateau]= 1
            j_plateau+=1
            
    return plateau
