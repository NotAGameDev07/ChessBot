def queen_moveset(frompos, topos, pieceExists, blocks):
    if blocks == True:
        return False
    if (abs(frompos[0] - topos[0]) >= 1) and (abs(frompos[1] - topos[1]) == 0):
        return True
    if (abs(frompos[1] - topos[1]) >= 1) and (abs(frompos[0] - topos[0]) == 0):
        return True
    if (abs(frompos[0] - topos[0]) == abs(frompos[1] - topos[1])):
        return True