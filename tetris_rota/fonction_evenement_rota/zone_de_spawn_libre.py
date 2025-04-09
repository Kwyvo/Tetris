def zone_de_spawn_libre(plateau,piece):
    # Vérifie si la pièce peut apparaître sans collision dans la zone centrale
    for i in range(len(piece[0])):
        for j in range(len(piece[0][0])):
            if plateau[i][len(plateau[0])-1 - j ] == 2:
                return False
    return True