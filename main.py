import player
class Game:
    def __init__(self, player1, player2):
        board = board.Board()
        self.varnika = player1
        self.sahitya = player2
        print("chess program. enter moves in algebraic notation separated by space")



varnika = player.Player('white', True)
sahitya = player.Player('black', False)
game = Game(varnika, sahitya)
print(varnika.getColor())
print(varnika.turn)
print(sahitya.getColor())