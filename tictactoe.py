
from GameClass import *
from Gameplay import *



def Games_Rules(mygame):
    mygame.name = input("What is your name ?")
    print (colored (f"\n{mygame.name} Welcome in TIC TAC TOE Games\n", "yellow"))
    print(colored("RULE OF THE GAME", "green"))
    print("The first player to get 3 of his/her symbol in a row, column or diagonally win the game.")
    print(colored("\nHOW TO PLAY", "red"))
    print("You will be playing with an AI. Enter your row Number and your column number to put your symbol.")
    print("Row number is refered to horizontal ligne")
    print("Col number is refered to vertical ligne")
    print("The first player will be choose randomly")
    print("Your raw number and your column number should be in a range of 1 to 3 ")
    print("The Player symbol is 'X' and the AI symbol is 'O'")
    time.sleep(5)


def display_game(mygame):
    
    print(f" {mygame.map[0][0]} | {mygame.map[0][1]} | {mygame.map[0][2]} " )
    print("___|___|___")
    print(f" {mygame.map[1][0]} | {mygame.map[1][1]} | {mygame.map[1][2]} ")
    print("___|___|___")
    print(f" {mygame.map[2][0]} | {mygame.map[2][1]} | {mygame.map[2][2]} ")

def check_winner(mygame):
    check_row(mygame) 
    check_col(mygame) 
    check_diagonal(mygame)
    check_tie_game(mygame)

def player_loop(mygame):
    player(mygame)
    display_game(mygame)
    check_winner(mygame)

def AI_loop(mygame):
    AI_turn(mygame)
    display_game(mygame)
    check_winner(mygame)

def play(mygame): 
    x = random.randint(0,1)
    if x == 0 :
        print("\nThe player will start \n")
    else :
        print("\nThe AI will start \n")
    while True :
        if x == 0 :
            player_loop(mygame)
            AI_loop(mygame) 
        else :
            AI_loop(mygame) 
            player_loop(mygame)
        print ("\n")

   
mygame = Player_record()
Games_Rules(mygame)
play(mygame)
