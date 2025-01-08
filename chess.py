class Board:
    def __init__(self):
        self.squares = [Square(j,i) for i in range(8,0,-1) for j in range(1,9)]
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
        # https://www.namecheap.com/visual/font-generator/chess-symbols/
        for square in self.squares:
            #white pawns
            if square.y == 2:
                square.piece = Piece('Pawn', 'w', '♙')
            #black pawns
            if square.y == 7:
                square.piece = Piece('Pawn', 'b', '♟')
            #white rooks
            if square.y == 1 and (square.x == 1 or square.x == 8):
                square.piece = Piece('Rook','w','♖')
            #black rooks
            if square.y == 8 and (square.x == 1 or square.x == 8):
                square.piece = Piece('Rook','b','♜')
            #white knights
            if square.y == 1 and (square.x == 2 or square.x == 7):
                square.piece = Piece('Knight','w','♘')
            #black knights
            if square.y == 8 and (square.x == 2 or square.x == 7):
                square.piece = Piece('Knight','b','♞')
            #white bishops
            if square.y == 1 and (square.x == 3 or square.x == 6):
                square.piece = Piece('Bishop','w','♗')
            #black bishops
            if square.y == 8 and (square.x == 3 or square.x == 6):
                square.piece = Piece('Bishop','b','♝')
            #white queen
            if square.y == 1 and square.x == 4:
                square.piece = Piece('Queen','w','♕')
            #black queen
            if square.y == 8 and square.x == 4:
                square.piece = Piece('Queen','b','♛')
            #white king 
            if square.y == 1 and square.x == 5:
                square.piece = Piece('King','w','♔')
            #black king
            if square.y == 8 and square.x == 5:
                square.piece = Piece('King','b','♚')
    
        #w pawns

    def print(self):
        print('  '+'-'*32)
        for square in self.squares:            
            if square.x == 1:
                print(f'{square.name[1]}|',end='')
            print(f'{square.printable()}|',end='')
            if square.x == 8:
                print()
                print('  '+'-'*32)
        print(' ',end='')       
        [print(f'  {'ABCDEFGH'[i]} ', end='') for i in range(0,8)]
            

class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = 'white' if (self.x%2 + self.y%2 == 1) else 'black'
        self.connected = []
        self.piece = None
        self.name = 'ABCDEFGH'[x-1] + str(y)

    def printable(self):
        if self.piece is None:
            return '   ' if self.color == 'white' else '   '
        else:
            return ' '+self.piece.symbol+' '
    
    def __repr__(self):
        connected_names = [sq.name for sq in self.connected]
        return self.name
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
    print(board.squares)
    board.print()