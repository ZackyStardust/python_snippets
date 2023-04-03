'''
This is a function that futurecoder asked to make to print the tictactoe board. This time, the way I did was exactly how they proposed.
'''


def format_board(board):
    string = ""
    for i in range(len(board)):
        for char in board[i]:
            string += char
        if i != len(board) - 1:
            string += '\n'
    return string


'''
However, they showed a solution using join(). I was not able to fully grasp join() before this point.
'''


def format_board(board):
    joined_rows = []
    for row in board:
        joined_rows.append("".join(row))
    return "\n".join(joined_rows)


'''
As a bonus, they asked me to make a printer that displays the board as such:

X|O|X
-+-+-
 |O|O
-+-+-
 |X|

This is the first result I did, without join().
'''

def format_board(board):
    string = ""
    for i in range(len(board)):
        sep = 0
        for char in board[i]:
            string += char
            if sep < 2:
                string += '|'
                sep += 1
        if i != len(board) - 1:
            string += '\n'
            string += '-+-+-\n'
    return string
  

'''
And now, a solution using join(). They did not provide a result of their own for this one. I think I could have done better in the following line:

sep = "\n" + sep + "\n"

But, right not, I don't see how.

'''


def format_board(board):
    joined_rows = []
    sep = []
    for row in board:
        joined_rows.append("|".join(row))
        sep.append("-")
    sep = "+".join(sep)
    sep = "\n" + sep + "\n"
    return sep.join(joined_rows)


'''
From what I understood, join() takes the elements in the parameter, which apparently takes only lists, and inserts the element before it in between.
Below I will make an implementation of join. Since I don't know how the element before the function exactly works, I will insert is as a parameter.
'''

def join(separator, to_append):
    size = 1
    result = ""
    for element in to_append:
        result += element
        if size < len(to_append):
            result += separator
        size += 1
    else:
        return result


'''
Then, I had to create a printer that would print the board with numbers on top and on the left as coordinates. For example:

 123
1XOX
2 OO
3 X

And I came up with the following solution:
'''


def format_board(board):
    joined_rows = []
    string = ""
    for i in range(len(board)):
        string += str(i + 1)
    joined_rows.append(" " + string)
    for i in range(len(board)):
        string = f'{str(i + 1)}{"".join(board[i])}'
        joined_rows.append("".join(string))
    return "\n".join(joined_rows)

