import pandas as pd
import numpy as np
from logo import logo

print(logo)
print("Welcome to my Tic Tac Toe game.\n")
print("Rules are simple.")
print("You will see a map where you will put your symbol based on location coordinates (top left corner is a0, middle is b1, bottom right corner is c2 etc.)\n")
print("Enjoy your game!\n\n")



while True:
    play_style = input('Play against "player" or "computer"? ').lower().strip()

    if play_style == "player" or play_style == "computer":
        break
    else:
        print('Invalid option. Please write "player" to play with another player or "computer" to play against computer. \n')

while True:
    playfield = input('Do you want to play on "3x3" field or "7x7" field? ').lower().strip()

    if playfield == "3x3" or playfield == "7x7":
        break
    else:
        print('Invalid option. Please write "3x3" or "7x7". \n')


if playfield == "3x3":
    data = {'A': ["_", "_", "_"],
            'B': ["_", "_", "_"],
            'C': ["_", "_", "_"]}

elif playfield == "7x7":
    data = {'A': ["_", "_", "_", "_", "_", "_", "_"],
            'B': ["_", "_", "_", "_", "_", "_", "_"],
            'C': ["_", "_", "_", "_", "_", "_", "_"],
            'D': ["_", "_", "_", "_", "_", "_", "_"],
            'E': ["_", "_", "_", "_", "_", "_", "_"],
            'F': ["_", "_", "_", "_", "_", "_", "_"],
            'G': ["_", "_", "_", "_", "_", "_", "_"]}

df = pd.DataFrame(data)


def computer():
    while True:
        row = np.random.choice(df.index)
        col = np.random.choice(df.columns)
        if playfield == "3x3":
            if col == "A":
                col = 0
            elif col == "B":
                col = 1
            else:
                col = 2

            if df.iloc[row, col] == "_":
                df.iloc[row, col] = "O"
                break

        elif playfield == "7x7":
            if col == "A":
                col = 0
            elif col == "B":
                col = 1
            elif col == "C":
                col = 2
            elif col == "D":
                col = 3
            elif col == "E":
                col = 4
            elif col == "F":
                col = 5
            else:
                col = 6

            if df.iloc[row, col] == "_":
                df.iloc[row, col] = "O"
                break


def player(player_num):
    player = True
    while player:
        if player_num == "player1":
            if play_style == "player":
                print("Player 1 turn")
            question = input("Where do you want to put 'X'? ").upper().strip()
        else:
            print("Player 2 turn")
            question = input("Where do you want to put 'O'? ").upper().strip()

        split = list(question)

        if playfield == "3x3":
            if "A" not in split and "B" not in split and "C" not in split:
                print("Invalid coordinates. Try again.")
            elif "0" not in split and "1" not in split and "2" not in split:
                print("Invalid coordinates. Try again.")
            else:
                row = int(split[1])
                if split[0] == 'A':
                    col = 0
                elif split[0] == 'B':
                    col = 1
                else:
                    col = 2

                if df.iloc[row, col] == "_":
                    if player_num == "player1":
                        df.iloc[row, col] = "X"
                    else:
                        df.iloc[row, col] = "O"
                    player = False
                else:
                    print("The field is already chosen. Try again.")

        elif playfield == "7x7":
            if "A" not in split and "B" not in split and "C" not in split and "D" not in split and "E" not in split and "F" not in split and "G" not in split:
                print("Invalid coordinates. Try again.")
            elif "0" not in split and "1" not in split and "2" not in split and "3" not in split and "4" not in split and "5" not in split and "6" not in split:
                print("Invalid coordinates. Try again.")
            else:
                row = int(split[1])
                if split[0] == 'A':
                    col = 0
                elif split[0] == 'B':
                    col = 1
                elif split[0] == 'C':
                    col = 2
                elif split[0] == 'D':
                    col = 3
                elif split[0] == 'E':
                    col = 4
                elif split[0] == 'F':
                    col = 5
                else:
                    col = 6

                if df.iloc[row, col] == "_":
                    if player_num == "player1":
                        df.iloc[row, col] = "X"
                    else:
                        df.iloc[row, col] = "O"
                    player = False
                else:
                    print("The field is already chosen. Try again.")

def game_over():
    loc = df.iloc
    # ----------------------- SMALL BRAIN ---------------------- #
    if playfield == "3x3":
        win_cases = [
            (loc[0, 0], loc[1, 0], loc[2, 0]),
            (loc[0, 1], loc[1, 1], loc[2, 1]),
            (loc[0, 2], loc[1, 2], loc[2, 2]),
            (loc[0, 0], loc[0, 1], loc[0, 2]),
            (loc[1, 0], loc[1, 1], loc[1, 2]),
            (loc[2, 0], loc[2, 1], loc[2, 2]),
            (loc[0, 0], loc[1, 1], loc[2, 2]),
            (loc[2, 0], loc[1, 1], loc[0, 2]),
        ]
        for case in win_cases:
            if case == ('X', 'X', 'X'):
                return True
            elif case == ('O', 'O', 'O'):
                if play_style == "computer":
                    print("You lost.")
                return True
        return False

    # ----------------------- BIG BRAIN ---------------------- #
    elif playfield == "7x7":
        win_cases = []

        # horizontal win cases
        for i in range(7):
            for j in range(3):
                win_cases.append((loc[i, j], loc[i, j + 1], loc[i, j + 2], loc[i, j + 3], loc[i, j + 4]))

        # vertical win cases
        for i in range(3):
            for j in range(7):
                win_cases.append((loc[i, j], loc[i + 1, j], loc[i + 2, j], loc[i + 3, j], loc[i + 4, j]))

        # diagonal win cases (top-left to bottom-right)
        for i in range(3):
            for j in range(3):
                win_cases.append(
                    (loc[i, j], loc[i + 1, j + 1], loc[i + 2, j + 2], loc[i + 3, j + 3], loc[i + 4, j + 4]))

        # diagonal win cases (top-right to bottom-left)
        for i in range(3):
            for j in range(4, 7):
                win_cases.append(
                    (loc[i, j], loc[i + 1, j - 1], loc[i + 2, j - 2], loc[i + 3, j - 3], loc[i + 4, j - 4]))

        for case in win_cases:
            if case == ('X', 'X', 'X', 'X', 'X'):
                return True
            elif case == ('O', 'O', 'O', 'O', 'O'):
                if play_style == "computer":
                    print("You lost.")
                return True
        return False


def clean_board():
    rows, cols = df.shape
    for row in range(rows):
        for col in range(cols):
            df.iloc[row, col] = "_"


if play_style == "computer":
    active = True
    while active:
        ask = True
        while ask:
            first = input("Do you want to start first? Y/N: ").upper().strip()
            is_active = True

            if first == "Y":
                ask = False
                print(df)
                while is_active:
                    player("player1")
                    if game_over():
                        print(df)
                        print("You win!!!")
                        clean_board()
                        break
                    computer()
                    print(df)
                    if game_over():
                        clean_board()
                        break

            elif first == "N":
                ask = False
                while is_active:
                    computer()
                    print(df)
                    if game_over():
                        clean_board()
                        break
                    player("player1")
                    if game_over():
                        print(df)
                        print("You win!!!")
                        clean_board()
                        break

            else:
                print("Invalid symbol. Try again.")

        another = input('Do you want to play another game? Press "N" for no: ').upper().strip()
        if another == "N":
            print("Thank you for playing. Hopefully we will be seen soon!")
            active = False

elif play_style == "player":
    active = True
    while active:
        is_active = True
        print(df)
        while is_active:
            player("player1")
            print(df)
            if game_over():
                print("Player 1 win!!!")
                clean_board()
                break
            player("player2")
            print(df)
            if game_over():
                print("Player 2 win!!!")
                clean_board()
                break

        another = input('Do you want to play another game? Press "N" for no: ').upper().strip()
        if another == "N":
            print("Thank you for playing. Hopefully we will be seen soon!")
            active = False
