import argparse
import copy

parser = argparse.ArgumentParser(
    description='Solve triangular puzzle peg game with 15 pegs')
parser.add_argument('-b', '--begin', type=int, default=13,
                    help='The location of the hole when the game begins, e.g. 13')
parser.add_argument('-e', '--end', type=int, default=13,
                    help='The location of the last peg, e.g. 13')
args = parser.parse_args()

PEG = 'P'
HOLE = 'H'

MOVES = [
    [1, 2, 4],
    [1, 3, 6],
    [2, 4, 7],
    [2, 5, 9],
    [3, 5, 8],
    [3, 6, 10],
    [4, 2, 1],
    [4, 5, 6],
    [4, 7, 11],
    [4, 8, 13],
    [5, 8, 12],
    [5, 9, 14],
    [6, 3, 1],
    [6, 5, 4],
    [6, 9, 13],
    [6, 10, 15],
    [7, 4, 2],
    [7, 8, 9],
    [8, 5, 3],
    [8, 9, 10],
    [9, 5, 2],
    [9, 8, 7],
    [10, 6, 3],
    [10, 9, 8],
    [11, 7, 4],
    [11, 12, 13],
    [12, 8, 5],
    [12, 13, 14],
    [13, 12, 11],
    [13, 8, 4],
    [13, 9, 6],
    [13, 14, 15],
    [14, 13, 12],
    [14, 9, 5],
    [15, 10, 6],
    [15, 14, 13]
]


boards = []

jumps = []


def main():
  
    begin = args.begin
    end = args.end
    if not betweenInclusive(1, 15, begin):
        print('Valid range for location has to be 1 to 15, inclusive')
        exit(1)

    if not betweenInclusive(1, 15, end):
        print('Valid range for location has to be 1 to 15, inclusive')
        exit(1)

 
    board = []
    board.append(' ')  

    for i in range(1, 16, 1):
        if begin == i:
            board.insert(i, HOLE)
        else:
            board.insert(i, PEG)
    original = copy.deepcopy(board)


    if solve(board, end):
       
        print('Initial board')
        print(printBoard(original))

        j = 0
        for i in range(len(jumps) - 1, -1, -1):
            print(jumps[i])
            print(printBoard(boards[j]))
            j += 1
    else:
        print('No solution could be found for this combination')


def betweenInclusive(lower: int, upper: int, num: int):
   
    if num >= lower and num <= upper:
        return True
    else:
        return False


def count(array: list, value: str):
   
    count = 0
    for char in array:
        if char == value:
            count += 1
    return count


def printBoard(board: list):
  
    string = ''
    string += '    ' + board[1] + '\n'
    string += '   ' + board[2] + ' ' + board[3] + '\n'
    string += '  ' + board[4] + ' ' + board[5] + ' ' + board[6] + '\n'
    string += ' ' + board[7] + ' ' + board[8] + \
        ' ' + board[9] + ' ' + board[10] + '\n'
    string += board[11] + ' ' + board[12] + ' ' + \
        board[13] + ' ' + board[14] + ' ' + board[15]
    return string


def solve(board: list, end: int):
 
    for move in MOVES:
   
        if board[move[0]] == PEG and board[move[1]] == PEG and board[move[2]] == HOLE:
 
            board[move[0]] = HOLE
            board[move[1]] = HOLE
            board[move[2]] = PEG

  
            clone = copy.deepcopy(board)
            boards.append(clone)

            if solve(board, end):
                jumps.append(
                    'Moved ' + str(move[0]) + ' to ' + str(move[2]) + ', jumping over ' + str(move[1]))
                return True

            if clone in boards:
                boards.remove(clone)

            board[move[0]] = PEG
            board[move[1]] = PEG
            board[move[2]] = HOLE
            
    pegCount = count(board, PEG)
    if pegCount == 1 and end == -1:
        return True

    elif pegCount == 1 and board[end] == PEG:
        return True

    else:
        return False

if __name__ == "__main__":
    main()