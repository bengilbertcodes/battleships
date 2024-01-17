from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
from random import randint
import time
import re


# Create a title for the game.

print('')
print('         XXXX     X   XXXXX XXXXX X     XXXXX  XXXX X   X XXXXX XXXX  XXXX')
print('         X   X   X X    X     X   X     X      X    X   X   X   X   X X')
print('         XXXX   X   X   X     X   X     XXXXX  XXXX XXXXX   X   XXXX  XXXX')
print('         X   X XXXXXXX  X     X   X     X         X X   X   X   X        X')
print('         XXXX  X     X  X     X   XXXXX XXXXX  XXXX X   X XXXXX X     XXXX')
print('')
print(Fore.BLUE + "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("\n")


title_text = (Fore.YELLOW + "Welcome to Battleships\n")
x = title_text.center(80)
print(x)
title_text_two = (Fore.YELLOW + "Prepare for Battle\n")
y = title_text_two.center(80)
print(y)

print("\r")


username = input("Please enter your name: ")
while not username.isalpha():
    print(Fore.RED + "Invalid characters in username. Only use letters (aA-zZ)")
    username = input("Please enter your name: ")
while True:
    if len(username) < 3:
        print(Fore.RED + "Username should be at least 3 characters.")
    else:    
        greet_username = (f"Hello, Commander {username} \n")
        x = greet_username.center(80)
        print(Fore.YELLOW + x)
        break


def user_options():
    """
    User input to choose to start the game or view the instructions
    """
    
    # List containing instructions of how to play the game
    instructions = [
        "1. Aim of the game is to destroy all of the enemy ships.", ".",
        "2. Choose your ships by entering 5 coordinates.\n   Letter (a-h or A-H) Number (1-8) and a space eg: a1 b3 d5 g6 c8", ".",
        "3. Starting player is randomly chosen.", ".",
        "4. On your turn, choose a coordinate (letter and number (a5)) to fire at.", ".",
        "5. If you hit a ship your board is marked 'X'. A miss is marked 'O'.", ".",
        "6. Keep playing until somone wins!"
        ]

    
    print("Press " + Fore.YELLOW + "1 " + Fore.RESET + "to play game or " + Fore.YELLOW + "2 " + Fore.RESET + "for instructions..:")
    
    while True:
        choice = input("Your choice: ")
        
        if choice == "1":
            print("Running the main game...\n")
            # call main game functions
            break
        elif choice == "2":
            
            # print instructions
            i = 0
            while i < len(instructions):
                print(Fore.CYAN + instructions[i])
                i += 1
                time.sleep(1)
            print("\nPress " + Fore.YELLOW + "1 " + Fore.RESET + "to play game or " + Fore.YELLOW + "2 " + Fore.RESET + "for instructions..:")
        else:
            print("Incorrect choice. Press " + Fore.YELLOW + "1 " + Fore.RESET + "to play game or " + Fore.YELLOW + "2 " + Fore.RESET + "for instructions..:")
            
# user_options()

print(Fore.CYAN + "First, choose your ship locations. \n")

# Credit to Knowledge Maven's youtube series for help with the following functions
# https://github.com/gbrough/battleship/blob/main/single_player.py
# https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=565s&ab_channel=KnowledgeMavens


# Constants
BOARD_SIZE = 8
NUM_SHIPS = 5

ENEMY_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]
PLAYER_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]

ENEMY_GUESS_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]
PLAYER_GUESS_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]


def display_board(board, title):
    """
    Function to display the board
    """
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
    """
    User input to choose coordinates for placing ships and locating enemy
    ships in the game.
    Creates a list of coordinates from the input data

    Raises:
        ValueError, KeyError: Checks to ensure user chooses values A-H or 1-8

    Returns:
        column and row data
    """
    while True:
        try:
            column = input("Choose a column for your ship (A - H): \n").upper()
            if column in 'ABCDEFGH':
                column = letters_to_numbers[column]
                break
            else:
                # Error check to ensure a valid letter is entered by the player
                raise ValueError(Fore.RED + "Invalid column. Please enter a valid letter between A-H")
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
                raise ValueError(Fore.RED + "Invalid Row. Please enter a number between 1 and 8")
        except ValueError as e:
            print(f"Error: {e}")

    return row, column

def validate_coords(coords_list):
    # Define the pattern for the "a1" format (a letter followed by a digit)
    pattern = re.compile(r'^[a-zA-Z]\d$')

    # Check each element in the list against the pattern
    for element in coords_list:
        if not pattern.match(element):
            return False
    
    # If all elements match the pattern, return True
    return True

def player_place_ships():
    """
    Prompt for user input for 5 coordinates.
    Coordinates then split into list.
    """
    x = input(Fore.CYAN + "Enter five coordinates separated by a space (a1 b2 c3 d4 f5): " + Fore.RESET)
    player_coords_list = x.split(" ")
    print(player_coords_list)
    
    check_list = validate_coords(player_coords_list)
    
    if len(player_coords_list) != 5:
        print(Fore.RED + "Incorrect number of coordinates entered. Please enter 5 coordinates...")
        return player_place_ships()
    elif check_list:
        print(Fore.GREEN + "All coords match required format")
    else:
        print(Fore.RED + "Not all coords match required format (letter and number (a1)")
        return player_place_ships()
        
    return player_coords_list


def cpu_place_ships():
    """
    Randonly create a list of 5 coordinates for computer ships.
    """
    letters = "abcdefgh"
    cpu_coords_list = []
    
    for _ in range(5):
        letter = random.choice(letters)
        digit = random.randint(1, 8)
        cpu_coords_list.append(letter + str(digit))

    return cpu_coords_list

player_coords = player_place_ships()
print("Player Coordinates:", player_coords)

cpu_coords = cpu_place_ships()
print("CPU Coordinates:", cpu_coords)


def place_ships(board, NUM_SHIPS, title):
    """
    Places 'B' on the PLAYER_BOARD for ship locations
    Checks whether space is already used for a ship
    Args:
        board - refers to specific board
        NUM_SHIPS (constant)
        title - a name for the board
    """
    for ship in range(NUM_SHIPS):
        ship_row, ship_column = get_ship_location()
        while board[ship_row][ship_column] == "B":
            print("That location is already taken, choose another")
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "B"
        # Display the board after each ship placement
        display_board(board, title)  


def enemy_create_ships(board):
    """
    Uses randint to choose random numbers for computer ship coordinates
    Populates ENEMY_BOARD with 5 radomly plaaced ships
    """
    for ship in range(NUM_SHIPS):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "B":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "B"


def count_ships(board):
    """
    Counts the number of hits ('X') on the board.

    Returns:
        integer for count_ships
    """
    count = 0
    for row in board:
        for column in row:
            if column == (Fore.RED + "X" + Fore.RESET):
                count += 1
    return count

def who_plays_first():
    """
    uses random.choice to choose which player starts the game
    """
    return random.choice(['player', 'computer'])

def first_player():
    """
    Displays a message informing user who starts the game
    """
    first_player = who_plays_first()

    if first_player == 'player':
        print("    You play first!")
    else:
        print("    Computer plays first!")

def player_turn():
    """
    Player chooses a coordinate to fire at
    If location contains ship (B) then the location on PLAYER_GUESS_BOARD is marked with X
    If the shot misses a O is placed on PLAYER_GUESS_BOARD
    Checks that the user hasn't already chosen that coordinate and displays message
    """ 
    while (count_ships(ENEMY_BOARD)) < 5:
        print("Take your shot")
        display_board(PLAYER_GUESS_BOARD, "Player Guess Board")
        print(f'Enemy score:  {count_ships(ENEMY_GUESS_BOARD)}')
        print(f'Player score:  {count_ships(PLAYER_GUESS_BOARD)}')
        row, column = get_ship_location()
        if PLAYER_GUESS_BOARD[row][column] == "O":
            print(Fore.YELLOW + "    You already fired there! Pick another coordinate.")
        elif ENEMY_BOARD[row][column] == "B":
            print("    HIT!")
            PLAYER_GUESS_BOARD[row][column] = (Fore.RED + "X" + Fore.RESET)
            break
        else:
            print("    MISS!")
            PLAYER_GUESS_BOARD[row][column] = (Fore.GREEN + "O" + Fore.RESET)
            break
        
        

def computer_turn():
    """
    Randomly generate a computer shot.
    X = hit. O = miss.
    Checks to see if coordinates have already been chosen
    """
    while (count_ships(PLAYER_BOARD)) < 5:
        row, column = randint(0,7), randint(0,7)
        if PLAYER_BOARD[row][column] == "B":
            print("    Enemy has HIT your ship!")
            ENEMY_GUESS_BOARD[row][column] = (Fore.RED + "X" + Fore.RESET)
            break
        elif PLAYER_BOARD[row][column] == "O":
            computer_turn()
        elif ENEMY_GUESS_BOARD[row][column] == "X":
            computer_turn()
        else:
            print("    The enemy has MISSED!")
            ENEMY_GUESS_BOARD[row][column] = (Fore.GREEN + "O" + Fore.RESET)
            break
        
        
def main():
    """
    Runs the game functions
    """
    enemy_create_ships(ENEMY_BOARD)
    place_ships(PLAYER_BOARD, NUM_SHIPS, "   Your Board")
    display_board(ENEMY_BOARD, "   Enemy Board")
    
    first_player()
    
    current_player = (who_plays_first)

    while True:
        if current_player == 'player':
            player_turn()
            current_player = 'computer'
        else:
            computer_turn()
            current_player = 'player'
            
    
    # Check for game score after each turn and exits game if score is 5 and displays the winning board
        if count_ships(PLAYER_GUESS_BOARD) == 5:
            print("    You destroyed all the enemy's ships! You win")
            display_board(PLAYER_GUESS_BOARD, "    Player Board")
            break
        elif count_ships(ENEMY_GUESS_BOARD) == 5:
            print("    The enemy destroyed your fleet! You lose.")
            display_board(ENEMY_GUESS_BOARD, "    Enemy Guess Board")
            break
    
    


# main()
