class Board:
    def __init__(self):
        self.squares = [Square(i,j) for i in range(1,9) for j in range(1,9)]
        self.setup()

    def setup(self):
        self.connect_squares()
        self.place_pieces()

    def connect_squares(self):
        for curr_square in self.squares:
            for square in self.squares:
                if abs(curr_square.x - square.x) <= 1 \
                and abs(curr_square.y - square.y) <= 1\
                and square is not curr_square:
                    curr_square.connected.append(square)

    def place_pieces(self):
        #pawns
        for square in self.squares:
            if square.y == 2 or square.y == 7:
                square.piece = Piece('pawn', 'w' if square.y == 2 else 'b')
    
        #w pawns

    def print(self):
        for square in self.squares:
            print(square)

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.connected = []
        self.piece = None
        self.name = 'ABCDEFGH'[x-1] + str(y)
    
    def __repr__(self):
        connected_names = [sq.name for sq in self.connected]
        return f'Square: {self.name}, piece: {self.piece}, connected: {connected_names}'

class Piece:
    def __init__(self,type, color):
        self.type = type
        self.color = color
    
    def __repr__(self):
        return self.type

if __name__ == '__main__':
    board = Board()
    board.print()