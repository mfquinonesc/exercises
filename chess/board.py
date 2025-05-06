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

        square_piece = None       
        found_piece = False

        for p in self.pieces:
            if(p.row == row and p.col == col):
                square_piece = p

            if(piece.compare_to(p)):
                found_piece = True


        if(not found_piece):
            return False
        
        if(square_piece != None and (square_piece.is_same_piece_as(King(0,0)) or square_piece.color == piece.color)):
            return False

        if not piece.is_valid_move(row, col):
            return False        

        return True
 
    def move(self, piece, row, col):

        if(not self.is_valid_to_move(piece, row, col)):
            return
        
        found_piece = None

        for p in self.pieces:
            if piece.compare_to(p):
                found_piece = p
        
        
        self.pieces.remove(found_piece)
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
              
        return piece
        

    def __str__(self):

        text = ''
        for i in range(8):
            for j in range(8):
                piece = None
                for p in self.pieces:
                    if p.col == j and p.row == i:
                        piece = p

                text = text + (str('.') if piece == None else str(piece))

            text = text + '\n'

        return text