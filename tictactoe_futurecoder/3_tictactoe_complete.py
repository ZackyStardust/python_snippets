'''
Futurecoder now gave me a list of functions for me to work. I was supposed to create the game itself.
The function of the game was supposed to be play_game(board_size, player1, player2).
They gave me the following functions below, already done.
Note, however, that the play_move function is commented: I modified it to better suit my purpose.
Also of note is that futurecoder said that I should consider that the players would only give correct inputs,
so I was not supposed to deal with wrong inputs. I, however, plan to change it so that if the players insert
a wrong input, the program warns that the input was invalid and that they should try again.
'''

def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings


def row_winner(board):
    return any(winning_line(row) for row in board)


def column_winner(board):
    return row_winner(zip(*board))


def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))


def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))


def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)


def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

'''
def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))
'''

def make_board(size):
    return [[' '] * size for _ in range(size)]


def print_winner(player):
    print(f'{player} wins!')


def print_draw():
    print("It's a draw!")


'''
I created the play_game function and added a new one, check_busy, to be implemented into the play_move function so that the player
would not overwrite any other movement already done. This was important not only for the "playability", but also because
I used the maximum ammount of movements into said board for it to calculate when it would be a draw. So it was possible
for a game to be considered a draw if one of the players overwrote one of the movements. Therefore, below is my play_game function,
as well as check_busy and my modified version of play_move.
'''

def play_move(board, player):
    active = True
    while active == True:
        print(f'{player} to play:')
        row = int(input()) - 1
        col = int(input()) - 1
        if check_busy(board, row, col) == False:
            pass
        else:
            board[row][col] = player
            print(format_board(board))
            active = False


def check_busy(board, row, col):
    if board[row][col] != ' ':
        return False
    else:
        return True


def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    current_player = player1
    for _ in range(board_size ** 2):
        play_move(board, current_player)
        if winner(board):
            print_winner(current_player)
            break
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        print_draw()
