import random
import time
import re
import os
from random import randint
from colorama import Fore, Back, Style, init
init(autoreset=True)


# Create a title and intro text for the game.
def create_title():
    with open("title.txt", "r") as f:
        title = f.readlines()
    for line in title:
        print(line.rstrip())
    with open("line.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        print(Fore.BLUE + line)
        
    title_text = (Fore.YELLOW + "Welcome to Battleships \n")
    x = title_text.center(80)
    print(x)
    title_text_two = (Fore.YELLOW + "Prepare for Battle \n")
    y = title_text_two.center(80)
    print(y)

    print("\r")

def create_username():
    global username  # Use the global keyword to modify the global variable
    
    while True:
        user_input = input("Please enter your name: ")
        if not user_input.isalpha():
            print(Fore.RED + "Invalid characters in username. Only use letters (aA-zZ)")
            continue
        elif len(user_input) < 3:
            print(Fore.RED + "Username should be at least 3 characters.")
            continue
        else:
            username = user_input  # Update the global variable
            greet_username = f"Hello, Commander {username}\n"
            x = greet_username.center(75)
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


# Credit to Knowledge Maven's youtube series for help with the following 
# constants and display_board functions
# https://github.com/gbrough/battleship/blob/main/single_player.py
# https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=565s&ab_channel=KnowledgeMavens


# Constants
BOARD_SIZE = 8
NUM_SHIPS = 5

ENEMY_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]
PLAYER_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]

ENEMY_GUESS_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]
PLAYER_GUESS_BOARD = [[' '] * BOARD_SIZE for x in range(BOARD_SIZE)]

# global variables
# List of player coordinates
player_coords_list = []
# list of compuer coordinates
cpu_coords_list = []
# Name entered by player
username = ""
# List of tried shots by player
tried_shots = set()
# List of computer tried shots
cpu_tried_shots = set()

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


def validate_coords(coords_list):
    # Define the pattern for the "a1" format (a letter followed by a digit)
    pattern = re.compile(r'^[a-hA-H][1-8]$')

    # Check each element in the list against the pattern
    for element in coords_list:
        if not pattern.match(element):
            return False
        
    if len(set(coords_list)) != len(coords_list):
        return False
    
    # If all elements match the pattern, return True
    return True


def player_place_ships():
    """
    Prompt for user input for 5 coordinates.
    Coordinates then split into a list.
    """
    global player_coords_list

    while True:
        x = input(Fore.CYAN + "\nEnter five coordinates (a1 to h8) separated by a space eg. a1 b2 c3 d4 f5: " + Fore.RESET)
        player_coords_list = x.split(" ")

        check_list = validate_coords(player_coords_list)

        if len(player_coords_list) != 5 or not check_list:
            print(Fore.RED + "Incorrect coordinates entered. Please enter 5 unique coordinates...")
        elif check_list:
            print(Fore.GREEN + "All coordinates match the required format")
            # convert coordinates to indices
            player_coords_list = [convert_to_indices(entry) for entry in player_coords_list]
            break
        else:
            print(Fore.RED + "Not all coords match the required format (letter and number, e.g., a1)")

    return player_coords_list


def cpu_place_ships():
    """
    Randomly create a list of 5 coordinates for computer ships.
    """
    global cpu_coords_list

    letters = "abcdefgh"
    cpu_coords_list = set()

    while len(cpu_coords_list) < 5:
        letter = random.choice(letters)
        digit = random.randint(1, 8)
        new_coord = letter + str(digit)

        # Check if the coordinate is already in the set
        if new_coord not in cpu_coords_list:
            cpu_coords_list.add(new_coord)

    cpu_coords_list = [convert_to_indices(coord) for coord in cpu_coords_list]
    
    return list(cpu_coords_list)


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


def first_player():
    """
    Displays a message informing user who starts the game
    """
    first_player = random.choice(['player', 'computer'])

    if first_player == 'player':
        print(Fore.YELLOW + f"\nCommander {username} to play first!")
    else:
        print(Fore.YELLOW + "\nComputer Enemy plays first!")
    return first_player


def convert_to_indices(user_input):
    """
    Takes user input eg. a1, changes letter to number
    returns coordinate to reference coordinates list
    """
    
    column_letter = user_input[0].upper()  
    row = int(user_input[1:])

    # Convert the letter to a corresponding index
    column = ord(column_letter) - ord('A')

    return column, row


def is_valid_input(user_input):
    if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isdigit():
        return True
    return False


def player_shot():
    while True:
        user_input = input("Please enter a coordinate for your shot (a1 - h8): ")
        result = validate_coords([user_input])

        if not result:
            print(Fore.RED + "Invalid coordinates!!!")
            continue

        shot_coords = convert_to_indices(user_input)
        return shot_coords


def player_turn():
    """
    Takes user input from player shot.
    Checks against cpu_coords_list.
    If match is True = Hit
    Updates the PLAYER_GUESS_BOARD with X or O (Hit or Miss)
    Adds coordinate to list of tried shots to avoid repeats OR checks BOARD???
    """
    global tried_shots
    print(cpu_coords_list)

    while True:
        shot_coords = player_shot()
        
        if shot_coords is None:
            print("Error: player_shot returned None")
            continue

        column, row = shot_coords

        if (column, row) in tried_shots:
            print("You already tried that one")
            continue

        tried_shots.add((column, row))

        if (column, row) in cpu_coords_list:
            print("Hit!")
            PLAYER_GUESS_BOARD[row - 1][column] = (Fore.RED + "X" + Fore.RESET)
            display_board(PLAYER_GUESS_BOARD, (Fore.YELLOW + f" {username}'s Guess Board"))
            break
        else:
            print("Miss")
            PLAYER_GUESS_BOARD[row - 1][column] = (Fore.GREEN + "O" + Fore.RESET)
            display_board(PLAYER_GUESS_BOARD, (Fore.CYAN + f" {username}'s Guess Board"))
            break


def computer_turn():
    """
    Generate random coordinate.
    Check against player_coords list.
    If match is true = HIT else Miss
    Add coordinate to list of tried coordinates to avoid repeats
    """
    while True:
        # Generate random coordinates within the valid range
        column, row = randint(0, 7), randint(0, 7)
        cpu_shot = column, row 
        
        if cpu_shot in cpu_tried_shots:
            continue
        else:
            cpu_tried_shots.add(cpu_shot)

        if cpu_shot in player_coords_list:
            print("Hit! Enemy has destroyed one of your ships!")
            ENEMY_GUESS_BOARD[row - 1][column] = (Fore.RED + "X" + Fore.RESET)
            display_board(ENEMY_GUESS_BOARD, Fore.BLUE + "Enemy's Guess Board")
            break
        else:
            print("Enemy has missed.")
            ENEMY_GUESS_BOARD[row - 1][column] = (Fore.GREEN + "O" + Fore.RESET)
            display_board(ENEMY_GUESS_BOARD, Fore.BLUE + "Enemy's Guess Board")
            break


def main():
    """
    Runs the game functions
    """
    create_title()
    create_username()
    user_options()
    
    os.system('clear')
    create_title()
    print(Fore.CYAN + "First, choose your 5 ship locations. \n")
    
    display_board(PLAYER_BOARD, Fore.CYAN + "Here's your board:")

    user_input = player_place_ships()
    cpu_input = cpu_place_ships()
    
    print("Player coords list: ", player_coords_list)
    print("cpu coords list: ", cpu_coords_list)
    
    # first_player()
    
    current_player = first_player()
    
    while True:
        if current_player == 'player':
            os.system('clear')
            create_title()
            print(Fore.CYAN + f"\n{username}'s turn: \n")
            player_turn()
            current_player = 'computer'
        else:
            print(Fore.CYAN + "\nEnemy's turn: \n")
            computer_turn()
            current_player = 'player'
            
    # Check for game score after each turn and exits game if score is 5 and displays the winning board
        if count_ships(PLAYER_GUESS_BOARD) == 5:
            print("    You destroyed all the enemy's ships! You win")
            display_board(PLAYER_GUESS_BOARD, f"{username}'s Board")
            break
        elif count_ships(ENEMY_GUESS_BOARD) == 5:
            print("    The enemy destroyed your fleet! You lose.")
            display_board(ENEMY_GUESS_BOARD, "Enemy's Guess Board")
            break


main()
