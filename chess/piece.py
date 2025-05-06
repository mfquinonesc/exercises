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

    def is_same_piece_as(self, piece):
        return type(self) == type(piece)

    def compare_to(self, piece):
        return (self.is_same_piece_as(piece) and self.row == piece.row and self.col == piece.col and self.color == piece.color)

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