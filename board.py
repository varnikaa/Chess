import piece
class Board:
    def __init__(self):
        self.rows, self.cols = (9, 9)
        self.boardd = [[piece.Piece(piece.Type.VACANT, 'nope')]*self.cols]*self.rows
    
    def initializePawn(self, color):
        for i in range(9):
            print(self.boardd[1][i].getColor())
        for i in range(9):
            self.boardd[1][i] = piece.Piece(piece.Type.PAWN, 'white')
        for i in range(9):
            print(self.boardd[2][i].getColor())

            
    def initializeRanked(self, color):
        """for i in range(9):
            self.boardd[1][i] = piece.Piece(piece.Type.PAWN, color)"""
        pass
    
    def initializePiece(self):
        self.initializePawn('white')
        #self.initializePawn('black')


    def resetBoard(self):
        self.boardd = [[piece.Piece(piece.Type.VACANT, 'nope')]*self.cols]*self.rows
        self.initializePiece()


board = Board()
board.resetBoard()
