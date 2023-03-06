def queen_moveset(frompos, topos, pieceExists, blocks, p0, p1):
	Team_question_mark = ((p0.team is None) and (p1.team is None)) or ((p0.team is not None) and (p1.team is None))
	if not Team_question_mark:
		return False
	if blocks == True:
		return False
	if (abs(frompos[0] - topos[0]) >= 1) and (abs(frompos[1] - topos[1]) == 0):
		return True
	if (abs(frompos[1] - topos[1]) >= 1) and (abs(frompos[0] - topos[0]) == 0):
		return True
	if (abs(frompos[0] - topos[0]) == abs(frompos[1] - topos[1])):
		return True

def knight_moveset(frompos, topos, pieceExists, blocks, p0, p1):
	if (abs(frompos[0] - topos[0]) == 2) and (abs(frompos[1] - topos[1]) == 1):
		return True
	return False