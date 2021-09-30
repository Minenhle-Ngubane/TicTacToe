class TicTacToe:

    def __init__(self):
        self.board = [
            ["[ ]","[ ]","[ ]"], 
            ["[ ]","[ ]", "[ ]"], 
            ["[ ]","[ ]","[ ]"]
        ] # initial empty board

        self.moves = 0 # initial number of moves made (maximum number of moves in 9)
        self.current_player = "X" # initial player (player 1)
        self.display_board() # Call the display_board() function on start to display game board
        self.play() # Call play() function to start playing game

    # Function to display / draw game board on the terminal
    def display_board(self):
        for row in self.board:
            for value in row:
                print(value, end = " ")
            print() # Print a new line

        print() # Live empty line below board

    # Function to update the game board after a player makes a move
    def update_board(self, row, column):
        if self.current_player == "X":
            token = "[X]"
        else:
            token = "[O]"

        if self.board[int(row)-1][int(column)-1] == "[ ]": # if the position is empty than update with current player token
            self.board[int(row)-1][int(column)-1] = token
            self.moves += 1 # increment number of moves by 1
            self.display_board() # Call the display_board() function to display updated game board on the terminal

            if self.moves != 9:

                if self.check_winner(token): # Check if there is a winner
                    print()
                    print("===========================")
                    print("Game Over : {} Player wins.".format(self.current_player))
                    print("===========================")
                
                else:
                    self.change_current_player() # if no winner than change to next player

                self.play() # Call the play() function to continue game if there is no winner
                    
            else: # No more moves left, end game with a draw
                print()
                print("========================================================================")
                print("It is a draw : No winner for this game. Do you want to play again? (Y/N)")
                print("========================================================================")

        else: # Position entered is already played
            print()
            print("============================================================")
            print("This position is already played, please try another position")
            print("============================================================")
            print()

            self.play() # Call the play() function for player to continue playing but re-enter available/empty positions

    def check_winner(self, token): # Check if current player has won
        
        if (
            """      
              0 1 2 
            0 [][][] -> Horizontal
            1 [][][] |  Vertical
            2 [][][] /  Diagonal
            """
            # Horizontal Check
            (self.board[0][0] == token and self.board[0][1] == token and self.board[0][2] == token) or 
            (self.board[1][0] == token and self.board[1][1] == token and self.board[1][2] == token) or
            (self.board[2][0] == token and self.board[2][1] == token and self.board[2][2] == token) or

            # Vertical Check
            (self.board[0][0] == token and self.board[1][0] == token and self.board[2][0] == token) or 
            (self.board[0][1] == token and self.board[1][1] == token and self.board[2][1] == token) or
            (self.board[0][2] == token and self.board[1][2] == token and self.board[2][2] == token) or
            
            # Diagonal Check
            (self.board[0][0] == token and self.board[1][1] == token and self.board[2][2] == token) or 
            (self.board[0][2] == token and self.board[1][1] == token and self.board[2][0] == token)
        ):
            return True # Return true if current plyer has won the game

        else: 
            return False # Return false if current player has not won the game
           

    def play(self): # Prompt current player to enter position
    
        row = input("Enter a row ( 1 , 2 , or 3 ) for player {}: ".format(self.current_player))
        while int(row) > 3 or int(row) < 1 : # force the player to enter only a valid input (1, 2, or 3)
            row = input("Input not allowed. Please Enter a row ( 1 , 2 , or 3 ) for player {}: ".format(self.current_player))

        column = input("Enter a column ( 1 , 2 , or 3 ) for player {}: ".format(self.current_player))
        while int(column) > 3 or int(column) < 1:  # force the player to enter only a valid input (1, 2, or 3)   
            column = input("Input not allowed. Please Enter a column ( 1 , 2 , or 3 ) for player {}: ".format(self.current_player))
       
        self.update_board(row, column) # Call the update_board() funtion to update game board with new postion


    # Method to change to the next player (If the current player is X than it will change to the next player O)
    def change_current_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

TicTacToe() # Call the TicTacToe class


    



  
    



