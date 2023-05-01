# -- Global Declaration---
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_is_going = True
current_player = "x"
winner = None


def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])



def play_game():
    while game_is_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_game()

    if winner == "X" or winner == "O":
        print("The winner  is - ", winner)
    else:
        print("Its a tie.")

def handle_turn():

    #while
    pos = int(input("\nChoose a position from 1 to 9  -  "))
    print("You have entered -", pos)

    position = pos - 1
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_diagonal():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


def check_coloumn():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


def check_rows():
    global game_is_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        pass



def check_for_winner():
    global  winner

    #check rows
    row_winner =  check_rows()
    #check coloumns
    coloumn_winner = check_coloumn()
    #check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner =  row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif check_diagonal:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_if_tie():
    pass

def flip_game():
    pass



def main():
    print("\n---WellCome---\n")
    play_game()

if __name__ == "__main__":
    main()
