def zone_de_spawn_libre(plateau,piece):
    # Vérifie si la pièce peut apparaître sans collision dans la zone centrale
    for i in range(len(piece[0])):
        for j in range(len(piece[0][0])):
            if plateau[i][j +(len(plateau[0])//2)-1] == 2:
                return False
    return True