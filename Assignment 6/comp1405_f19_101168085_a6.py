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

        self.w_pieces = ['k','q','r','n','b','p'] # White pieces            
        self.b_pieces = ['K','Q','R','N','B','P'] # Black pieces

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
            piece (string): The piece provided by the user, '-' if none provided
            column (int): The column position of the piece, '0' if no piece provided
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
        choice = input(f'Would you like to move a piece (y/n): ').lower() # Ask the user if they would like to move a piece
        if choice == 'y': # If they say yes, continue
            while(True):
                row = int(input('Which row would you like to move from (top left is 0,0): ')) # Ask for the row to move from
                column = int(input('Which column would you like to move from (top left is 0,0): ')) # Ask for the col to move from
                if row >= 8 or row < 0 or column >= 8 or column < 0: # Input validation
                    print('Wrong selection, please try again')
                    continue # Keep looping

                new_row = int(input('Which row would you like to move it to (top left is 0,0): ')) # Ask for the row to move to
                new_col = int(input('Which column would you like to move it to (top left is 0,0): ')) # Ask for the col to move to
                if new_row >= 8 or new_row < 0 or new_col >= 8 or new_col < 0: # Input validation
                    print('Wrong move, please try again')
                    continue # Keep looping
                
                elif self.chess_board[new_row][new_col] != '-': # If there is a piece already at the new position
                    print(f'The position ({new_row}, {new_col}) is already occupied')
                    print('Options:') # Offer two choices, they can either swap or replace
                    print('1: Swap the two pieces')
                    print('2: Replace the piece')
                    choice = input('Type \'1\' or \'2\': ') # Get the user choice
                
                if choice == '1': # If they ask to swap the pieces
                    # Tuple matching to swap the two positions in the chessboard
                    self.chess_board[row][column], self.chess_board[new_row][new_col] = self.chess_board[new_row][new_col], self.chess_board[row][column]
                    break # Break the loop
                else: # If they ask to replace the piece
                    self.chess_board[new_row][new_col] = self.chess_board[row][column] # Replace the new position with the old one
                    self.chess_board[row][column] = '-' # Change the old position to a default of '-'
                    break # Break the loop

    def calculate_score(self):
        """
        Calculates the score of the chessboard based on individual pieces each player has

        Args:
            self: instance of the class  
        """
        white_score = 0 # Score for white pieces
        black_score = 0 # Score for black pieces

        for row in self.chess_board: # Itterate over each row in the chessboard
            for piece in row: # Itterate over each piece in the row
                if piece in self.w_pieces: # Check if the piece is from the white piece list
                    if piece == 'k': # If the piece is a King
                        white_score += 0 
                    if piece == 'q': # If the piece is a Queen
                        white_score += 10 
                    if piece == 'r': # If the piece is a Rook
                        white_score += 5 
                    if piece == 'n': # If the piece is a Knignt
                        white_score += 3.5
                    if piece == 'b': # If the piece is a Bishop
                        white_score += 3
                    if piece == 'p': # If the piece is a Pawn
                        white_score += 1
                elif piece in self.b_pieces: # Check if the piece is from the black piece list
                    if piece == 'K': # If the piece is a King
                        black_score += 0
                    if piece == 'Q': # If the piece is a Queen
                        black_score += 10
                    if piece == 'R': # If the piece is a Rook
                        black_score += 5
                    if piece == 'N': # If the piece is a Knight
                        black_score += 3.5
                    if piece == 'B': # If the piece is a Bishop
                        black_score += 3
                    if piece == 'P': # If the piece is a Pawn
                        black_score += 1
        
        print(f'White Score: {white_score}') # Print white pieces score
        print(f'Black Score: {black_score}') # Print black pieces score


def main(): # Main function
    
    print('-Welcome to the chessboard simulator-\n')
    print('Instructions:')
    print('Firstly make a new chessboard, to put a piece on the chessboard,') 
    print('input an 8 character long string with \'-\' and a piece')
    print('Example inputs: ')
    print('\t--------')
    print('\t---k----')
    print('\t-------Q')
    print('After the board has been populated you may chose to move pieces,') 
    print('remember for reference, the top left point is (0,0) and the bottom')
    print('right piece is (7,7)\n')

    while(True): # Outter loop to remake the chessboard
        chess_board = ChessBoard() # Instantiate the ChessBoard class and generate a 2D list
        chess_board.setup() # Call the setup method to populate the 2D list
        chess_board.calculate_score() # Call the calculate_score method to display the score

        while(True): # Inner loop to keep playing the chessboard we just created above
            chess_board.move_piece() # Call the move_piece method to ask the user if they would like to move
            chess_board.print_chess_board() # Print the chessboard
            chess_board.calculate_score() # Call the calculate_score method to print the score of the chessboard      

            exit_condition = input('Would you like to continue playing on this chessboard? (y/n): ').lower() # Ask for the exit condition and lower case it
            if exit_condition == 'n': # If user said no
                break # Break the inner loop

        exit_condition = input('Would you like to create a new chessboard? (y/n): ').lower() # Ask the user for the exit condition and lower case it
        if exit_condition == 'n': # If the user said no
            print('Goodbye!')
            break # Break the outter loop


# Entry point of the program
if __name__ == '__main__':
    main()

