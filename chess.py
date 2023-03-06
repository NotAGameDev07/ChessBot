import movesets


class Chessboard:
	def __init__(self, size):
		#inits chessboard
		self.empty = Emptypiece()
		self.size = size
		self.board = []
		for i in range(self.size):
			self.board.append([])
			for _ in range(self.size):
				self.board[i].append(self.empty)
	#gets chesspiece at index
	def __getitem__(self, key):
		return self.board[key[1]][key[0]]
	#prints chessboard
	def __repr__(self):
		rstr = []
		rstr.append("X  " + " ".join(map(str, range(self.size))))
		for i, k in enumerate(self.board):
			rstr.append(f"{i}  " + " ".join(map(repr, k)))
		return "\n".join(rstr)
	#sets chesspiece at index
	def __setitem__(self, key, value):
		self.board[key[1]][key[0]] = value
	#makes piece movements
	def move(self, pos0, pos1):
		#checks if piece exists in the move to position
		exists = (self.board[pos1[1]][pos1[0]] != self.empty)
		#checks if piece can move
		if self.board[pos0[1]][pos0[0]].moveset(pos0, pos1, exists, not self.is_path_clear(pos0, pos1), self.board[pos0[1]][pos0[0]], self.board[pos1[1]][pos1[0]]):
			self.board[pos1[1]][pos1[0]] = self.board[pos0[1]][pos0[0]]
			self.board[pos0[1]][pos0[0]] = self.empty
	def is_path_clear(self, from_pos, to_pos):
		# Get the direction of the move
		from_row, from_col = from_pos
		to_row, to_col = to_pos
		delta_row = to_row - from_row
		delta_col = to_col - from_col
		
		# Check if move is horizontal
		if delta_row == 0:
			for col in range(from_col + delta_col // abs(delta_col), to_col, delta_col // abs(delta_col)):
				if self.board[from_row][col] != self.empty:
					return False
		# Check if move is vertical
		elif delta_col == 0:
			for row in range(from_row + delta_row // abs(delta_row), to_row, delta_row // abs(delta_row)):
				if self.board[row][from_col] != self.empty:
					return False
		# Check if move is diagonal
		elif abs(delta_row) == abs(delta_col):
			for i in range(1, abs(delta_row)):
				row = from_row + i * delta_row // abs(delta_row)
				col = from_col + i * delta_col // abs(delta_col)
				if self.board[row][col] != self.empty:
					return False
		else:
			return True
		
		return True



class Emptypiece:
	def __init__(self):
		self.exists = False
		self.team = None
	def __repr__(self):
		return "_"
	def __str__(self):
		return "empty"

class Chesspiece(Emptypiece):
	def __init__(self, name, symbol, moveset=None, team=None):
		super().__init__()
		self.exists = True
		self.name = name
		self.symbol = symbol
		if team is not None:
			self.team = team
		if moveset is not None:
			self.moveset = moveset
		else:
			self.moveset = self._moveset
	#prints chesspiece
	def __repr__(self):
		return self.symbol
	#moving logic
	def _moveset(self, frompos, topos, pieceExists, blocks, p0, p1):
		Team_question_mark = ((p0.team is None) and (p1.team is None)) or ((p0.team is not None) and (p1.team is None))
		if not Team_question_mark:
			return True
		if blocks == True:
			return False
		if (topos[1] >= frompos[1]):
			return False
		if (abs(frompos[1] - topos[1]) in [1, 2]) and (frompos[0] == topos[0]) and not pieceExists:
			return True
		if (abs(frompos[0] - topos[0]) in [1, 2]) and (abs(frompos[1] - topos[1]) in [1, 2]) and pieceExists:
			return True
		return False
		
	

board = Chessboard(8)
board[4, 5] = Chesspiece("Pawn", 'p', team=10)
board[6, 7] = Chesspiece("Queen", 'Q', movesets.queen_moveset, team=1)
print(repr(board))
board.move([4, 5], [4, 4])
board.move([6, 7], [6, 6])
board.move([6, 6], [4, 4])
print(repr(board))