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
            self.move = input('Type your move: ')
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

    def setup(self, piece, row, column):
            self.chess_board[row][column] = piece
       
    def move_piece(self):
            choice = input(f'Would you like to move a piece (y/n): ').lower()
            if choice == 'y':
                while(True):
                    row = int(input('Which row would you like to move from: '))
                    column = int(input('Which column would you like to move from: '))
                    if row > 8 or column > 8:
                        print('Wrong selection idiot')
                        continue

                    new_row = int(input('Which row would you like to move it to: '))
                    new_col = int(input('Which column would you like to move it to: '))
                    if new_row > 8 or new_col > 8:
                        print('Wrong move idiot')
                        continue
                    
                    elif self.chess_board[new_row][new_col] != '-':
                        print('That position is already occupied')
                        print('Options:')
                        print('1: Swap the two pieces')
                        print('2: Replace the piece')
                        choice = input('Type \'1\' or \'2\': ')
                    
                    if choice == '1':
                        self.chess_board[row][column], self.chess_board[new_row][new_col] = self.chess_board[new_row][new_col], self.chess_board[row][column]
                        break
                    else:
                        self.chess_board[row][column] = self.chess_board[new_row][new_col]
                        self.chess_board[row][column] = '-'
                        break

    def check_score(self):
        self.white_player = 0
        self.black_player = 0

        for row in self.chess_board:
            for piece in row:
                if piece in self.w_peices:
                    if piece == 'k':
                        self.white_player += 0
                    if piece == 'q':
                        self.white_player += 10
                    if piece == 'r':
                        self.white_player += 5
                    if piece == 'n':
                        self.white_player += 3.5
                    if piece == 'b':
                        self.white_player += 3
                    if piece == 'p':
                        self.white_player += 1
                elif piece in self.b_peices:
                    if piece == 'K':
                        self.black_player += 0
                    if piece == 'Q':
                        self.black_player += 10
                    if piece == 'R':
                        self.black_player += 5
                    if piece == 'N':
                        self.black_player += 3.5
                    if piece == 'B':
                        self.black_player += 3
                    if piece == 'P':
                        self.black_player += 1
        
        return self.white_player, self.black_player

def main():

    while(True):
        cb = ChessBoard()

        for i in range(8):
            piece, column = cb.parse_move() # get the details from players input
            cb.setup(piece, i, column) # pass it to this function to setup a row in the chessboard
            cb.print_chess_board() # print the final chessboard

        white_score, black_score = cb.check_score() # get the score for the chessboard
        print(f'White Score: {white_score}')
        print(f'Black Score: {black_score}')

        while(True): # Start playing the chessboard we just created above
            cb.move_piece()
            cb.print_chess_board()

            white_score, black_score = cb.check_score() # get the new score for the chessboard
            print(f'White Score: {white_score}')
            print(f'Black Score: {black_score}')

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

