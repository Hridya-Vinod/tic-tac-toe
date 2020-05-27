import os
def main():
    board = create_board()
    print_board(board)
    player = "x"
    pl = "player1"
    while True:
        choice = int(input(pl +" Enter the move: "))
        update_board(board, choice, player)
        player = player_turn(player)
        clear_screen()
        print_board(board)
        if win(board):
            print(pl + " won the game")
            break
        if draw(board):
            print("Draw")
            break
        pl = player_change(pl)




# creating the board
def create_board():
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    return board

# printing the board
def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

# updating the board
def update_board(board,choice, player):
        for i in range(3):
            for j in range(3):
                if board[i][j] == choice:
                    board[i][j] = player
def player_turn(player):
    if player == "x":
        return "o"
    else:
        return "x"

def player_change(pl):
    if pl == "player1":
        return "player2"
    else:
        return "player1"
# checking the win
def win(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return True
    for diag in range(3):
        if board[0][0] == board[1][1] == board[2][2]:
            return True
        if board[2][0] == board[1][1] == board[0][2]:
            return True
        return False


# checking the draw
def draw(board):
    for row in board:
        for col in row:
            if str(col).isdigit():
                return False
    return True

def clear_screen():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
main()
