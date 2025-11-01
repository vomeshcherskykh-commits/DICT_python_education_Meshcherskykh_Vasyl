board = [['_','_','_'],['_','_','_'],['_','_','_']]
player = 'X'

def print_board():
    print('---------')
    for r in board:
        print(f'| {r[0]} {r[1]} {r[2]} |')
    print('---------')

def check_win():
    lines = [
        ''.join(board[0]), ''.join(board[1]), ''.join(board[2]),
        board[0][0]+board[1][0]+board[2][0],
        board[0][1]+board[1][1]+board[2][1],
        board[0][2]+board[1][2]+board[2][2],
        board[0][0]+board[1][1]+board[2][2],
        board[2][0]+board[1][1]+board[0][2]
    ]
    if 'XXX' in lines: return 'X'
    if 'OOO' in lines: return 'O'
    return None

print_board()

while True:
    coords = input('Enter the coordinates: ').split()

    if not all(c.isdigit() for c in coords):
        print('You should enter numbers!')
        continue

    x, y = map(int, coords)

    if not (1 <= x <= 3 and 1 <= y <= 3):
        print('Coordinates should be from 1 to 3!')
        continue

    r, c = x - 1, y - 1

    if board[r][c] != '_':
        print('This cell is occupied! Choose another one!')
        continue

    board[r][c] = player
    print_board()

    winner = check_win()
    if winner:
        print(f'{winner} wins')
        break
    if not any('_' in row for row in board):
        print('Draw')
        break

    player = 'O' if player == 'X' else 'X'