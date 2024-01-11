from colorama import Fore, Back, Style
import random

print('')
print('XXXX     X   XXXXX XXXXX X     XXXXX  XXXX X   X XXXXX XXXX  XXXX')
print('X   X   X X    X     X   X     X      X    X   X   X   X   X X')
print('XXXX   X   X   X     X   X     XXXXX  XXXX XXXXX   X   XXXX  XXXX')
print('X   X XXXXXXX  X     X   X     X         X X   X   X   X        X')
print('XXXX  X     X  X     X   XXXXX XXXXX  XXXX X   X XXXXX X     XXXX')
print('')

ENEMY_BOARD = [[' '] * 8 for x in range(8)]
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

def create_board(board):
    print('')
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, '|'.join(row)))
        row_number += 1


create_board(ENEMY_BOARD)
create_board(PLAYER_BOARD)

