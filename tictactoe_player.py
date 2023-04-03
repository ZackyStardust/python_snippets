'''
Now, futurecoder provided me with two functions:
- format_board(board): prints the map
- play_game(): a simple way for the game to work, taking only two inputs: one from player X and other from player O - then it stops.

Both of them are displayed below,
'''


def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)


def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    print(format_board(board))
    print('\nX to play:\n')
    play_move(board, 'X')
    print(format_board(board))
    print('\nO to play:\n')
    play_move(board, 'O')
    print(format_board(board))


'''
It asked me to crate a function play_move(board, player) in order to make the actual movements.
I would take two inputs: first the y axis, and then the x axis. Them, it would insert the current player in the right position.
The play_game() funciton would, then, print the state of the board after the movement. So I made the following:
'''


def play_move(board, player):
    y = int(input()) - 1
    x = int(input()) - 1
    board[y][x] = player
