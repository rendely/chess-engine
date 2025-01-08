class Board:
    def __init__(self):
        self.squares = [Square(j,i) for i in range(1,9) for j in range(1,9)]
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
        for square in self.squares:
            #white pawns
            if square.y == 2:
                square.piece = Piece('Pawn', 'w', '♙')

            #black pawns
            if square.y == 7:
                square.piece = Piece('Pawn', 'b', '♟')
    
        #w pawns

    def print(self):
        print(' '+'-'*39)
        for square in self.squares:            
            if square.x == 1:
                print('|',end='')
            print(f' {square.printable()} |',end='')
            if square.x == 8:
                print()
                print(' '+'-'*39)
            

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.connected = []
        self.piece = None
        self.name = 'ABCDEFGH'[x-1] + str(y)

    def printable(self):
        if self.piece is None:
            return self.name
        else:
            return self.piece.symbol+' '
    
    def __repr__(self):
        connected_names = [sq.name for sq in self.connected]
        return f'Square: {self.name}, piece: {self.piece}, connected: {connected_names}'

class Piece:
    def __init__(self,type, color, symbol):
        self.type = type
        self.color = color
        self.symbol = symbol
    
    def __repr__(self):
        return f'{self.symbol}'

if __name__ == '__main__':
    board = Board()
    board.print()