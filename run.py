from colorama import Fore, Back, Style
from random import randint


# Create a title for the game.

print('')
print('XXXX     X   XXXXX XXXXX X     XXXXX  XXXX X   X XXXXX XXXX  XXXX')
print('X   X   X X    X     X   X     X      X    X   X   X   X   X X')
print('XXXX   X   X   X     X   X     XXXXX  XXXX XXXXX   X   XXXX  XXXX')
print('X   X XXXXXXX  X     X   X     X         X X   X   X   X        X')
print('XXXX  X     X  X     X   XXXXX XXXXX  XXXX X   X XXXXX X     XXXX')
print('')


# Constants
BOARD_SIZE = 8
NUM_SHIPS = 5

ENEMY_BOARD = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]
PLAYER_BOARD = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]

ENEMY_GUESS_BOARD = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]
PLAYER_GUESS_BOARD = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# ...

def display_board(board, title):
    # Function to display the board
    print(f"\n{title}")
    print('  A B C D E F G H')
    print(' -----------------')
    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}|")
        row_number += 1
        
# convert column letters into numbers 
letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
}

def get_ship_location():
    # Function to get ship location from the player
    while True:
        try:
            column = input("Choose a column for your ship (A - H): \n").upper()
            if column in 'ABCDEFGH':
                column = letters_to_numbers[column]
                break
            else:
                # Error check to ensure a valid letter is entered by the player
                raise ValueError("Invalid column. Please enter a valid letter between A-H")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    while True:
        try:
            row = input("Choose the row for your ship (1-8): \n")
            if row in "12345678":
                row = int(row) - 1
                break
            else:
                # error check to ensure a valid number is eneterd by the player
                raise ValueError("Invalid Row. Please enter a number between 1 and 8")
        except ValueError as e:
            print(f"Error: {e}")

    return row, column

def place_ships(board, num_ships, title):
    # Function to place ships on the board
    for ship in range(num_ships):
        ship_row, ship_column = get_ship_location()
        while board[ship_row][ship_column] == "B":
            print("That location is already taken, choose another")
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "B"
        # Display the board after each ship placement
        display_board(board, title)  

def enemy_create_ships(board):
    # Function to randomly place enemy ships on the board
    for ship in range(NUM_SHIPS):
        ship_row, ship_column = randint(0, BOARD_SIZE - 1), randint(0, BOARD_SIZE - 1)
        while board[ship_row][ship_column] == "B":
            ship_row, ship_column = randint(0, BOARD_SIZE - 1), randint(0, BOARD_SIZE - 1)
        board[ship_row][ship_column] = "B"
        # Display the board after each ship placement
        display_board(board, "Enemy's Board")  

def player_create_ships(board):
    # Function to allow the player to place their ships on the board
    place_ships(board, NUM_SHIPS, "Your Board")
    
def count_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count
            

def main():
    # Main game logic functions
    enemy_create_ships(ENEMY_BOARD)
    player_create_ships(PLAYER_BOARD)
    count_ships(ENEMY_BOARD)
    

if __name__ == "__main__":
    main()
