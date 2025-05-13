import math

class Piece():

    def __init__(self, row, col, color=True):
        self.row = row
        self.col = col
        self.color = color
        self.symbol = 'X'
        self.was_moved = False

    def is_valid_move(self, row, col):

        if (row < 0 or row > 7):
            return False

        if (col < 0 or col > 7):
            return False

        if (row == self.row and col == self.col):
            return False

        return True    


    def get_squares_between(self, row, col):

        squares = list()

        if self.is_valid_move(row, col):

            dist = math.sqrt(row**2 + col**2)
            current_dist = math.sqrt(self.row**2 + self.col**2)

            row0 = row if dist < current_dist else self.row
            row1 = self.row if dist < current_dist else row
            
            col0 = col if dist < current_dist else self.col
            col1 = self.col if dist < current_dist else col

            for x  in  range(col0, col1 + 1):
                for y in range(row0 , row1 + 1):
                    squares.append([y,x])

            squares.remove([self.row, self.col])
            squares.remove([row, col])
            
        return squares
    

    def is_same_piece_type_as(self, piece):
        return type(self) == type(piece)

    def compare_to(self, piece):
        return (self.is_same_piece_type_as(piece) and self.row == piece.row and self.col == piece.col and self.color == piece.color)
    
    def get_name(self):
        return str(type(self).__name__)
    
    def get_color(self):
        return 'White' if self.color else 'Black'

    def __str__(self):
        return self.symbol.upper() if self.color else self.symbol.lower()



class King(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'K'


    def is_valid_move(self, row, col):

        dist = math.sqrt((row - self.row)**2 + (col - self.col)**2)

        if (dist > math.sqrt(2)):
            return False

        return super().is_valid_move(row, col)    
   
  

class Rook(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'R'

    def is_valid_move(self, row, col):

        if (row != self.row and col != self.col):
            return False

        return super().is_valid_move(row, col)



class Bishop(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'B'

    def is_valid_move(self, row, col):

        b1 = self.row - self.col
        b2 = self.row + self.col

        if (row != (col + b1) and row != (-col + b2)):
            return False

        return super().is_valid_move(row, col)
    
    
    def get_squares_between(self, row, col):
        squares = super().get_squares_between(row, col)
        filter = list()
        for s in squares:
           if self.is_valid_move(s[0], s[1]):
               filter.append(s)

        return filter



class Queen(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'Q'

    def is_valid_move(self, row, col):

        rook = Rook(self.row, self.col)
        rook_move = rook.is_valid_move(row, col)

        bishop = Bishop(self.row, self.col)
        bishop_move = bishop.is_valid_move(row, col)

        return rook_move or bishop_move
    
    def get_squares_between(self, row, col):               
        rook_squares = Rook(self.row, self.col, self.color).get_squares_between(row, col)
        bishop_squares = Bishop(self.row, self.col, self.color).get_squares_between(row, col)
        
        if len(rook_squares) > 0:
            return rook_squares
        
        return bishop_squares



class Knight(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'N'

    def is_valid_move(self, row, col):

        y = abs(self.row - row)
        x = abs(self.col - col)

        if (not ([x, y] in [[1, 2], [2, 1]])):
            return False

        return super().is_valid_move(row, col)
    
    def get_squares_between(self, row, col):
        return list()



class Pawn(Piece):

    def __init__(self, row, col, color=True):
        super().__init__(row, col, color)
        self.symbol = 'P'

    def is_valid_move(self, row, col):

        if (self.color and not (row < self.row)):
            return False

        if (not self.color and not (row > self.row)):
            return False

        if (not self.color and self.row == 1 and row == 3 and self.col == col):
            return True

        if (self.color and self.row == 6 and row == 4 and self.col == col):
            return True

        dist = math.sqrt((self.col - col)**2 + (self.row - row)**2)

        if (dist > math.sqrt(2)):
            return False

        return super().is_valid_move(row, col)    