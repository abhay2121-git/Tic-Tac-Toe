#Implementing tic tac toe game

#Fuction to print tic tac toe game
def print_tic_tac_toe(values):
    #print("\n")
    #print("\t____|____|____")
    print("\t {}  | {}  | {}".format(values[0], values[1], values[2]))
    print("\t____|____|____")
    #print("\t    |    |    ")
    print("\t {}  | {}  | {}".format(values[3], values[4], values[5]))
    print("\t____|____|____")
    print("\t {}  | {}  | {}".format(values[6], values[7], values[8]))
    print("\t    |    |    ")  

#Function to print the score board for the game.
def print_scoreboard(score_board):
    print("\t---------------------------------")
    print("            SCOREBOARD FOR TIC TAC TOE")
    print("\t---------------------------------")
    players = list(score_board.keys())
    print("\t", players[0], "\t", score_board[players[0]])
    print("\t", players[1], "\t", score_board[players[1]])
    print("\t-------------------------------\n")

#Function to check if any player has won the game.
def check_winner(player_positon, current_player):
    #All possible winnig combinations for the players
    pos_win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    #loop to check if wiining combination is satisfied or not
    for x in pos_win:
        if all(y in player_positon[current_player] for y in x):
            #wiining cominations astisfies
            return True 
    return False

#Function to check if the game is a draw
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

#Function for a single Tic Tac Toe game
def single_game(current_player):
    values = [' ' for x in range(9)]
    #store the positon occupied by X and O
    player_position = {'X': [], 'O': []}

    #Game loop for a single game
    while True:
        print_tic_tac_toe(values)

        #Try exception blocks for MOVE input
        try:
            print("player", current_player, "turn which box?:", end=" ")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        #sanity check for MOVE input
        if move < 1 or move > 9:
            print("Please choose the right number between 1 to 9")
            continue

        #check if cell is occupied or not
        if values[move - 1] != ' ':
            print("The place you have chosen is already filled. Try Again!!")
            continue

        #update game status 
        #updating board status
        values[move - 1] = current_player
        #updating player positions
        player_position[current_player].append(move)

        #Function call for checking winner
        if check_winner(player_position, current_player):
            print_tic_tac_toe(values)
            print("Player", current_player, "has won the game!!")
            print("\n")
            return current_player
        
        #Function call for checking draw game
        if check_draw(player_position):
            print_tic_tac_toe(values)
            print("Game is a Draw")
            print("\n")
            return "Draw"
        
        #switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":
    print("player 1 DEtails")
    player1 = input("Enter the name of the player: ")
    print("\n")

    print("player 2 Details")
    player2 = input("Enter the name of the player: ")
    print("\n")

    #stores the player who chooses X and O 
    current_player = player1
    player_choice = {'X': " ", 'O': " "}

    #store the options
    options = ['X', 'O']

    #store the scoreboard details
    score_board = {player1 : 0, player2 :0}
    print_scoreboard(score_board)

    #Game loop for a series of tic tac toe 
    #the loop runs until either of the players choose to quit
    while True:
        #player choice Menu
        print("Turn to choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for quit")

        #Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!!  Try Agian\n")
            continue

        #condition for player choice 
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else: 
                player_choice['O'] = player1
        
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['O'] = player1

        else:
            print("Wrong choice!!! Try again\n")

        #stores the winner in a single game
        winner = single_game(options[choice - 1])

        #scoreboard edits accordingly to the winner 
        if winner != "Draw":
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
        
        print_scoreboard(score_board)

        #switch player who chooses X or O
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1