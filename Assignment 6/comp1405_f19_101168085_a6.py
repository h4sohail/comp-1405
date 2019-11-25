# Name: Hamza Sohail
# Student Number: 101168085

class ChessBoard():
    def __init__(self):
        """
        This is the default constructor that initializes the ChessBoard class
        Generates a 2-D list used to represent the chessboard

        Args:
            self: instance of the class  
        """
        self.chess_board = [] # Empty chessboard list

        self.w_peices = ['k','q','r','n','b','p'] # White peices            
        self.b_peices = ['K','Q','R','N','B','P'] # Black peices

        for i in range(8): # Itterate over 8x8 list
            row = []
            for j in range(8):
                row.append('-') 
            self.chess_board.append(row) # Append '-' to each cell in 8x8 list

    def print_chess_board(self):
        """
        Prints the current state of the chessboard

        Args:
            self: instance of the class  
        """
        for row in self.chess_board: # Get each row in the chessboard list
            for item in row: # Get each item in the row
                print(f'  {item}  ', end=('')) # Print the item with some spaces as the buffer
            print('\n') # Print a new line to go to the next row

    def parse_move(self):
        """
        Parses the user input to get the piece and the position

        Args:
            self: instance of the class  
        Returns:
            peice (string): The peice provided by the user, '-' if none provided
            column (int): The column position of the piece, '0' if no peice provided
        """
        while(True): # Loop for input validation
            self.move = input('Initialize the board: ') # Get the user input
            if len(self.move) != 8: # Make sure the input was valid
                print('Wrong move idiot') 
                continue
            else:
                break

        piece = self.move.strip('-') # Strip the '-' characters
        if piece == '': # (Edge case) No piece provided
            piece = '-' # Set the piece to '-'

        for i in range(len(self.move)): # Get the column position of the piece
            if self.move[i] == piece: 
                column = i

        return piece, column # Return the piece and the column

    def setup(self):
        """
        Sets up the chessboard from the user input for all 8 rows and prints it after each row

        Args:
            self: instance of the class  
        """
        for row in range(8): # Itterate over 8 rows in the chessboard
            piece, column = self.parse_move() # Call the parse_move method and store the returns
            self.chess_board[row][column] = piece # Apply the input to the chessboard
            self.print_chess_board() # Print the final chessboard
       
    def move_piece(self):
        """
        Moves a piece based on user input

        Args:
            self: instance of the class  
        """
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

    def calculate_score(self):
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
        chess_board.calculate_score() # get the new score for the chessboard

        while(True): # Start playing the chessboard we just created above
            chess_board.move_piece()
            chess_board.print_chess_board()
            chess_board.calculate_score() # get the new score for the chessboard       

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

