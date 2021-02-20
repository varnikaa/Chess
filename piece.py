import enum

class Type(enum.Enum):
    PAWN = 1
    ROOK = 2 
    BISHOP = 3 
    KING = 4 
    KNIGHT = 5 
    QUEEN = 6
    VACANT = 7
   
class Piece():
    def __init__(self, type, color):
        self.killed = False
        self.type = type
        self.color = color
    def getColor(piece):
        return piece.color
    
    def getType(piece):
        return piece.type

class King(Piece):
    def __init__(piece, color):
        piece.type = Type.KING
        piece.color = color


