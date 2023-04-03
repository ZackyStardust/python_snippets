'''
The way I made the functions are widely different from the ones futurecoder showed me how it could be easily and most effectively done.
Therefore, for study purposes, I wanted to save my results and compare to the results that futurecoder gave me.
'''

def winner(board):
    if row_winner(board) == True:
        return True
    if column_winner(board) == True:
        return True
    if diagonal_winner(board) == True:
        return True
    return False


def row_winner(board):
    len_x = len(board)
    for row in board:
        first = row[0]
        won = 0
        for char in row:
            if char is first and char != ' ':
              won += 1
            if won is len_x:
                return True
    else:
        return False


def column_winner(board):
    len_y = len(board[0])
    len_x = len(board)
    y = 0
    while y < len_y:
        x = 0
        first = board[x][y]
        won = 0
        while x < len_x:
            if board[x][y] is first and board[x][y] != ' ':
                won += 1
            x += 1
        if won is len_y:
            return True
        y += 1
    else:
        return False


def diagonal_winner(board):
    len_board = len(board)
    x = 0
    y = 0
    first = board[0][0]
    won = 0
    while x < len_board:
        if first == board[x][x] and board[x][x] != ' ':
            won += 1
        x += 1
        if won == len_board:
            return True
    x -= 1
    first = board[x][y]
    while x > 0:
        if first == board[x][y] and board[x][y] != ' ':
            won += 1
        x -= 1
        y += 1
        if won == len_board:
            return True
    return False


# The assert_equal is a function from futurecoder to test the functions I make.
assert_equal(
    winner(
        [
            ['X', 'X', 'X', ' '],
            ['X', 'X', ' ', ' '],
            ['X', ' ', 'O', 'X'],
            [' ', ' ', 'O', 'X']
        ]
    ),
    False
)


assert_equal(
    winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O']
        ]
    ),
    True
)


assert_equal(
    winner(
        [
            ['X', ' '],
            ['X', 'O']
        ]
    ),
    True
)
