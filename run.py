from colorama import Fore, Back, Style


print('')
print('XXXX     X   XXXXX XXXXX X     XXXXX  XXXX X   X XXXXX XXXX  XXXX')
print('X   X   X X    X     X   X     X      X    X   X   X   X   X X')
print('XXXX   X   X   X     X   X     XXXXX  XXXX XXXXX   X   XXXX  XXXX')
print('X   X XXXXXXX  X     X   X     X         X X   X   X   X        X')
print('XXXX  X     X  X     X   XXXXX XXXXX  XXXX X   X XXXXX X     XXXX')
print('')

CPU_BOARD = [[' '] * 8 for x in range(8)]
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

def print_board(board):
    print('')
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, '|'.join(row)))
        row_number += 1
        
print_board(CPU_BOARD)
print_board(PLAYER_BOARD)