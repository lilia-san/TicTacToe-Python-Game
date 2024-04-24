import random
import time
from colorama import init
from termcolor import colored


def error(mygame):
    while True:
        try:
            mygame.rowplayer = int(input("Please enter your row :"))
            mygame.colplayer = int(input("Please enter your coloumn :"))
            if mygame.map[mygame.rowplayer -1][mygame.colplayer -1] == " ":
                break
            else :
                print("Sorry this position is taken...")
        except ValueError as msg:
            print(f"Error: {msg}")
        except TypeError as msg:
            print(f"Error: {msg}")  
        except IndexError as msg:
            print(f"Error: {msg}")
        except KeyboardInterrupt:
            print("\nProgram interrupted by the user.")
            exit()

def player(mygame):
    print(colored(f"\n{mygame.name} it's your turn ...\n", "magenta"))
    error(mygame)
    while mygame.map[mygame.rowplayer -1][mygame.colplayer -1] != " ":
       error(mygame)

    mygame.map[mygame.rowplayer -1][mygame.colplayer-1] = 'X'

def AI_turn(mygame):
    print(colored("The Ai turn ....\n", "blue"))
    time.sleep(2)
    ai_row = random.randint(0,2)
    ai_col = random.randint(0,2)
    while mygame.map[ai_row][ai_col] != " ":
        ai_row = random.randint(0,2)
        ai_col = random.randint(0,2)

    mygame.map[ai_row][ai_col] = 'O'

def check_row(mygame):
    for row in mygame.map:
        if row[0] == row[1] and row[1] ==row[2]:
            if row[0] == 'X':
                mygame.winner = 'X'
                print(colored(f"{mygame.name} YOU WIN ....","magenta"))
                #mygame.insert_score_database(mygame.name)
                exit()
            elif row[0] == 'O':
                    mygame.winner = 'O'
                    print(colored(f"The AI WIN , sorry you loose  ....", "blue"))
                    #mygame.insert_score_database("AI")
                    exit()

def check_col(mygame):
    for x in range(0, len(mygame.map[0])):
        if mygame.map[0][x] == mygame.map[1][x] and mygame.map[1][x] == mygame.map[2][x]: 
            if mygame.map[0][x] == 'X':
                mygame.winner = 'X'
                print(colored(f"{mygame.name} YOU WIN ....","magenta"))

                exit()  
            elif mygame.map[0][x] == 'O':
                mygame.winner = 'O'
                print(colored(f"The AI WIN , sorry you loose  ....", "blue"))
                exit()

def check_diagonal(mygame):
    if mygame.map[0][0] == mygame.map[1][1] == mygame.map[2][2]  \
    or mygame.map[0][2] == mygame.map[1][1] == mygame.map[2][0] :
        if mygame.map[1][1] == 'X':
            mygame.winner = 'X'
            print(colored(f"{mygame.name} YOU WIN ....","magenta"))
            exit()  
        elif  mygame.map[1][1] == 'O':
            mygame.winner = 'O'
            print(colored(f"The AI WIN , sorry you loose  ....", "blue"))
            exit()

def check_tie_game(mygame):
    for row in mygame.map:
        for x in row:
            if x == " ":
                return True
    print(colored(f"Sorry the game is tie ....", "red"))
    exit()       
    