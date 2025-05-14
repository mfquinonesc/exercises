
class Renderer:

    def __init__(self):

        self.black_char = '█'
        self.white_char = ' '
        self.chars_by_row = 5 # 5 default rows value
        self.chars_by_col = 12  # 12 default columns value


    def print_board(self):

        board = [[self.get_char_square((c + r) % 2 == 0) for c in range(8)] for r in range(8)]  

        rows = [[ [ ''.join(line) for line in square ] for square in row] for row in board]  
        
        for row in rows:
            for index in range(self.chars_by_row):
                line = []
                for s in range(8):
                    line.append(row[s][index])

                print(''.join(line))


    def get_char_square(self, color=True):

        char = self.white_char if color else self.black_char
        return [[char for _ in range(self.chars_by_col)] for _ in range(self.chars_by_row)]
