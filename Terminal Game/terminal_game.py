from quiz_game import quiz_game
from learn_game import learn_game

def clear_console():
    import os
    os.system('cls')
    
while True:
    clear_console()
    print("Please pick a mode!")
    print("-"*30)
    print("1. Quiz Mode")
    print("2. Learn Mode")
    print("3. Place Holder")
    print("4. Quit")
    print("-"*30)
    player_input = input("> ")
    clear_console()

    if player_input == "1":
        quiz_game()
    elif player_input == "2":
        learn_game()
    elif player_input == "3":
        continue
    elif player_input == "4":
        exit()
    else:
        continue