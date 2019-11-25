# Name: Hamza Sohail
# Student Number: 101168085

class ChessBoard():
    def __init__(self):
        self.chess_board = []

        self.w_peices = ['k','q','r','n','b','p']            
        self.w_score = 0

        self.b_peices = ['K','Q','R','N','B','P']
        self.b_score = 0

        for i in range(8):
            row = []
            for j in range(8):
                row.append('-')
            self.chess_board.append(row)

    def print_chess_board(self):
        for row in self.chess_board:
            for item in row:
                print(f'  {item}  ', end=(''))
            print('\n')

    def parse_move(self):
        while(True):
            self.move = input('Initialize the board: ')
            if len(self.move) != 8:
                print('Wrong move idiot')
                continue
            else:
                break

        piece = self.move.strip('-')
        if piece == '':
            piece = '-'

        for i in range(len(self.move)):
            if self.move[i] == piece:
                column = i

        return piece, column

    def setup(self):
        for row in range(8):
            piece, column = self.parse_move() # get the details from players input
            self.chess_board[row][column] = piece
            self.print_chess_board() # print the final chessboard
       
    def move_piece(self):
            choice = input(f'Would you like to move a piece (y/n): ').lower()
            if choice == 'y':
                while(True):
                    row = int(input('Which row would you like to move from (top left is 0,0): '))
                    column = int(input('Which column would you like to move from (top left is 0,0): '))
                    if row >= 8 or row < 0 or column >= 8 or column < 0:
                        print('Wrong selection idiot')
                        continue

                    new_row = int(input('Which row would you like to move it to (top left is 0,0): '))
                    new_col = int(input('Which column would you like to move it to (top left is 0,0): '))
                    if new_row >= 8 or new_row < 0 or new_col >= 8 or new_col < 0:
                        print('Wrong move idiot')
                        continue
                    
                    elif self.chess_board[new_row][new_col] != '-':
                        print(f'The position ({new_row}, {new_col}) is already occupied')
                        print('Options:')
                        print('1: Swap the two pieces')
                        print('2: Replace the piece')
                        choice = input('Type \'1\' or \'2\': ')
                    
                    if choice == '1':
                        self.chess_board[row][column], self.chess_board[new_row][new_col] = self.chess_board[new_row][new_col], self.chess_board[row][column]
                        break
                    else:
                        self.chess_board[new_row][new_col] = self.chess_board[row][column]
                        self.chess_board[row][column] = '-'
                        break

    def check_score(self):
        self.white_score = 0
        self.black_score = 0

        for row in self.chess_board:
            for piece in row:
                if piece in self.w_peices:
                    if piece == 'k':
                        self.white_score += 0
                    if piece == 'q':
                        self.white_score += 10
                    if piece == 'r':
                        self.white_score += 5
                    if piece == 'n':
                        self.white_score += 3.5
                    if piece == 'b':
                        self.white_score += 3
                    if piece == 'p':
                        self.white_score += 1
                elif piece in self.b_peices:
                    if piece == 'K':
                        self.black_score += 0
                    if piece == 'Q':
                        self.black_score += 10
                    if piece == 'R':
                        self.black_score += 5
                    if piece == 'N':
                        self.black_score += 3.5
                    if piece == 'B':
                        self.black_score += 3
                    if piece == 'P':
                        self.black_score += 1
        
        print(f'White Score: {self.white_score}')
        print(f'Black Score: {self.black_score}')

def main():
    while(True):
        chess_board = ChessBoard()
        chess_board.setup()
        chess_board.check_score() # get the new score for the chessboard

        while(True): # Start playing the chessboard we just created above
            chess_board.move_piece()
            chess_board.print_chess_board()
            chess_board.check_score() # get the new score for the chessboard
            
            exit_condition = input('Would you like to continue playing on this chessboard? (y/n): ').lower()
            if exit_condition == 'n':
                break

        exit_condition = input('Would you like to create a new chessboard? (y/n): ').lower()
        if exit_condition == 'n':
            print('Goodbye!')
            break

# Entry point of the program
if __name__ == '__main__':
    main()

