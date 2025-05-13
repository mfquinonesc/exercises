from piece import *


class Board:

    def __init__(self):
        self.setup()
        self.is_player1 = True

    def setup(self):

        self.pieces = list()

        self.pieces.append(Rook(0, 0, False))
        self.pieces.append(Rook(0, 7, False))
        self.pieces.append(Rook(7, 0))
        self.pieces.append(Rook(7, 7))

        self.pieces.append(Knight(0, 1, False))
        self.pieces.append(Knight(0, 6, False))
        self.pieces.append(Knight(7, 1))
        self.pieces.append(Knight(7, 6))

        self.pieces.append(Bishop(0, 2, False))
        self.pieces.append(Bishop(0, 5, False))
        self.pieces.append(Bishop(7, 2))
        self.pieces.append(Bishop(7, 5))

        self.pieces.append(Queen(0, 3, False))
        self.pieces.append(Queen(7, 3))

        self.pieces.append(King(0, 4, False))
        self.pieces.append(King(7, 4))

        for i in range(8):
            self.pieces.append(Pawn(1, i, False))
            self.pieces.append(Pawn(6, i,))


    def is_valid_to_move(self, piece, row, col):

        if (piece.color != self.is_player1):
            return False

        target_piece = None
        exists_piece = False

        for p in self.pieces:
            if (p.row == row and p.col == col):
                target_piece = p

            if (piece.compare_to(p)):
                exists_piece = True

        if (not exists_piece):
            return False

        if (target_piece != None and (target_piece.is_same_piece_type_as(King(0, 0)) or target_piece.color == piece.color)):
            return False

        if (target_piece != None and piece.is_same_piece_type_as(Pawn(0, 0)) and piece.col == col):
            return False

        if not piece.is_valid_move(row, col):
            return False
    
        squares = piece.get_squares_between(row, col)
        return self.get_are_empty_squares(squares)      
    

    def move_piece(self, piece, row, col):

        if (not self.is_valid_to_move(piece, row, col)):
            return

        current_piece = self.get_piece(row, col)     
        self.pieces.remove(current_piece)

        piece.row = row
        piece.col = col
        piece.was_moved = True
        self.pieces.append(piece)
        self.is_player1 = not self.is_player1


    def get_piece(self, row, col):

        piece = None
        for p in self.pieces:
            if p.row == row and p.col == col:
                piece = p
                break

        return piece
    

    def get_pieces_by_name_and_color(self, name, color):

        pieces = list()
        for p in self.pieces:
            if p.get_name() == name and p.color == color:
                pieces.append(p)

        return pieces
    

    def get_is_empty_square(self, row, col):

        for p in self.pieces:
            if p.row == row and p.col == col:
                return False

        return True
    

    def get_are_empty_squares(self, squares):

        n = 0
        while n < len(squares):
            if not self.get_is_empty_square(squares[n][0], squares[n][1]):
                return False

            n = n + 1

        return True
    
    
    def get_is_incheck(self):

        pieces = list()
        rooks = self.get_pieces_by_name_and_color("Rook", not self.is_player1)
        pieces.extend(rooks)
        bishops = self.get_pieces_by_name_and_color("Bishop", not self.is_player1)
        pieces.extend(bishops)
        knights = self.get_pieces_by_name_and_color("Knight", not self.is_player1)
        pieces.extend(knights)
        pawns = self.get_pieces_by_name_and_color("Pawn", not self.is_player1)
        pieces.extend(pawns)
        queens = self.get_pieces_by_name_and_color("Queen", not self.is_player1)
        pieces.extend(queens)        

        king = self.get_pieces_by_name_and_color('King', self.is_player1)[0]

        row = king.row
        col = king.col      

        for p in pieces:
            squares = p.get_squares_between(row, col)
            if p.is_valid_move(row, col) and self.get_are_empty_squares(squares):
                return True

        return False
    

    def get_is_incheckmate(self):

        if not self.get_is_incheck():
            return False
           
        for piece in [p for p in self.pieces if p.color == self.is_player1]:
            for row in range(8):
                for col in range(8):

                    copy = Board()
                    copy.pieces = self.pieces
                    copy.is_player1 = self.is_player1
                    copy.move_piece(piece, row, col)

                    if not copy.get_is_incheck():
                        return False

        return True
    

    def __str__(self):       

        text = ''
        for p in self.pieces:
            text = text + f'[{p.row},{p.col}] - {p.get_color()} {p.get_name()}\n'

        return text