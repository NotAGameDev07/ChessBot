class Chessboard:
	def __init__(self, size):
		self.empty = Emptypiece()
		self.size = size
		self.board = []
		for i in range(self.size):
			self.board.append([])
			for j in range(self.size):
				self.board[i].append(Chesspiece(None, "_"))
	def __getitem__(self, key):
		return self.board[key[1]][key[0]]
	def __repr__(self):
		rstr = []
		rstr.append("X  " + " ".join(map(str, range(self.size))))
		for i, k in enumerate(self.board):
			rstr.append(f"{i}  " + " ".join(map(repr, k)))
		return "\n".join(rstr)
	def __setitem__(self, key, value):
		self.board[key[1]][key[0]] = value

class Emptypiece:
	def __init__(self):
		self.exists = False
	def __repr__(self):
		return "_"
	def __str__(self):
		return "empty"

class Chesspiece(Emptypiece):
	def __init__(self, name, symbol, moveset=None):
		super().__init__()
		self.exists = True
		self.name = name
		self.symbol = symbol
		if moveset is not None:
			self.moveset = moveset
		else:
			self.moveset = self._moveset
	def __repr__(self):
		return self.symbol
	def _moveset(self, frompos, topos, pieceExists):
		if (abs(frompos[1] - topos[1]) in [1, 2]) and not pieceExists:
			return True
		if (abs(frompos[0] - topos[0]) in [1, 2]) and (abs(frompos[1] - topos[1]) in [1, 2]) and pieceExists:
			return True
		return False
		
	

board = Chessboard(8)
print(board[4, 5])
print(repr(board))