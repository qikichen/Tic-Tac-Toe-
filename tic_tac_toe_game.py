"""

Tic Tac Toe Game created as my first coding milestone! I learned how to use
function to create a simple game

@author: Qi Nohr Chen
"""

def clear_output():
    print('\n'*100)
#Command to get a new prebuild function that will clear out the board instead of giving a history

import random
#Library import for randint
    
def display_board(board):
    """
    DOCSTRING: Function displaying the gameboard
    Input: Empty string list multiplied by 10
    Output: gameboard
    """
    

    print(f"{board[7]}|{board[8]}|{board[9]}\n{board[4]}|{board[5]}|{board[6]}\n{board[1]}|{board[2]}|{board[3]}\n")
    #Simple board that is printed. Fromatting method used.

    #Command that sets the board up

def player_input(): #This will decide the markers
    """
    DOCSTRING: Function asking player 1, which marker they want to be
    Input: X or O
    Output: returns tuple (player1, player2)
    """
    marker= ""
    #Marker- Variable as an empty string

    while marker != "X" and marker != "O":
        marker = input("Do you want to be X or O:").upper()
    player1 = marker
    #While loop asking player 1 for their marker preference
    #While loop is active until assignation

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    #if and else statement outside of the while loop so that the while loop doesn't break

    return (player1,player2) #Returning a tuple


def choose_first():
    """
    DOCSTRING: Random number generator between 0 and 1 deciding which player starts first
    Input: None
    Output: Print statement of who starts first.
    """
    first= random.randint(0,1) #rand int imported from library
    if first == 1:
        print("Player 1 goes first")
        return "Player 1 goes first" 
    else:
        print("Player 2 goes first")
        return "Player 2 goes first"
    #If and else statements, deciding who goes first 

def player_choice(board):    
    next_pos = input("Where would you like to place it? (choose between 1-9):")
    while next_pos != range(9): 
        for x in next_pos:
            next_pos = int(next_pos)
            return next_pos ##While the next_pos variable is in between 1 and 9, it will iterate through the list and return the next_pos variable as an interger

def place_marker(board, marker, position):   
    board[position] = marker
        #Reassignment function
        
def win_check(board, mark):
    return (mark == board[1] and mark == board[2] and mark == board[3]) or (mark == board[4] and mark == board[5] and mark == board[6]) or (mark == board[7] and mark == board[8] and mark == board[9]) or (mark == board[1] and mark == board[4] and mark == board[7]) or (mark == board[7] and mark == board[5] and mark == board[3]) or (mark == board[9] and mark == board[5] and mark == board[1])
        #Function returning possible winning combinations
        
def space_check(board, position):
    return board[position] == " "
        #Function returning a boolean (True) if the position index is empty

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    #Return boolean whether board is full or not 
def replay():
    again = (input("Do you want to play again:")).upper()
    
    if again == "YES":
        return True
    elif again == "NO":
        return False
    else: 
        print("Please answer with yes or no")
        replay()
#Replay function asking players if they want to replay

# Game setup 

print('Welcome to Tic Tac Toe!')
while True:
    gameboard = [" "]*10 #Gameboard list
    player1, player2 = player_input() #Activate and assign marker_order variable
    turn= choose_first() #Turn variable
    game_on = input("Are you ready?:").upper() #game_on loop variable


    if game_on== "YES":
        game_on= True
    elif game_on =="NO":
        game_on= False

        #elif statements for turning the game on or off

    #Player 1

    while game_on == True:
        if turn== "Player 1 goes first" and full_board_check(gameboard)== False:
            display_board(gameboard)
            next_pos = player_choice(gameboard)
            win_check(gameboard, player1)

            if space_check(gameboard,next_pos) == True:      
                display_board(gameboard)
                place_marker(gameboard, player1, next_pos)
                clear_output()
                if win_check(gameboard, player1) == True:
                    print("Congratulations player 1, you have won")
                    game_on = False
                else:
                    turn="Player 2 goes first"
            if full_board_check(gameboard)==True:
                print("The board is full")
                game_on = False




    #Player 2
        if turn=="Player 2 goes first":
            display_board(gameboard)
            next_pos = player_choice(gameboard)
            win_check(gameboard, player2)

            if space_check(gameboard,next_pos) == True:      
                display_board(gameboard)
                place_marker(gameboard, player2, next_pos)
                turn ="Player 1 goes first"
                clear_output()
                if win_check(gameboard, player2) == True:
                    print("Congratulations player 2, you have won")
                    game_on = False
                else:
                    turn ="Player 1 goes first"
            if full_board_check(gameboard)==True:
                print("The board is full")
                game_on= False


    while game_on == False:
        if replay() == True:
            game_on = True
        else: 
            print("Thank you for playing!")
            break
    break #Double break to break out of two loops