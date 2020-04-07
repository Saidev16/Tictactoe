#-----------------Defind the Table------------
board = ["1","2","3",
         "4","5","6",
         "7","8","9"]

def board_display():
    print(board[0]+"|" + board[1]+"|"+ board[2])
    print(board[3]+"|"+ board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+ board[8])

game_still_going = True
winner = None
current_player="X"
def play_game():

    board_display()

    #while the game is still going
    while game_still_going:
        #Composent of each turn
        turn_switch(current_player)

        #check if the game has ended
        check_if_game_over()

        #switch to the other player
        flip_player()
    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("Tie")



#Composent of each player turn
def turn_switch(player):
    print(player+"'s Turn")
    position = (input("Choose your postition from 1-9 "))
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = (input(" Invalid position. Choose your postition from 1-9 "))

    position = int(position) -1
    board[position] = player
    board_display()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    columns_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    #get the winner
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    #if any rows have a match
    if row_1 or row_2 or row_3:
        game_still_going = False
    #knows the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6]
    column_2 = board[1] == board[4] == board[7]
    column_3 = board[2] == board[5] == board[8]
    #if any column have a match
    if column_1 or column_2 or column_3:
        game_still_going = False
    #knows the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8]
    diagonals_2 = board[6] == board[4] == board[2]
    # if any diagonals have a match
    if diagonals_1 or diagonals_2 :
        game_still_going = False
    # knows the winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]


    return



def check_if_tie():
    global game_still_going
    count = 0
    for a in range(0, 9):
        if board[a] == "X" or board[a] == "O":
            count += 1
    if count == 9:
        game_still_going = False

    return

def flip_player():
    #set variable at global to edit on it
    global current_player
    #change turns between players
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()

