class Board:
    def __init__(self):
        self.squares = [Square(i,j) for i in range(1,9) for j in range(1,9)]
    
    def print(self):
        for square in self.squares:
            print(square)


class Square:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        self.name = 'ABCDEFGH'[x-1] + str(y)
    
    def __repr__(self):
        return self.name

if __name__ == '__main__':
    board = Board()
    board.print()