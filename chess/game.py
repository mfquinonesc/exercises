from board import *


class Game:

    def __init__(self):

        self.board = Board()
        self.black_char = '█'
        self.white_char = ' '
        self.chars_by_row = 5 # 5 default rows value
        self.chars_by_col = 12  # 12 default columns value

    def simulate_by_notation(notation):
        pass  