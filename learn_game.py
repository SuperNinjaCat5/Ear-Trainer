def learn_game():   
    import winsound
    import os
    import random
    import getpass

    debug_mode = False #Toggle for debug text.

    def clear_console():
        os.system('cls')

    def debug_print(text): 
        if debug_mode == False:
            return
        print(text)

    #full

    note_freqs = {
        'C1': 32, 'C#1': 35, 'D1': 37, 'D#1': 39, 'E1': 41, 'F1': 44, 'F#1': 46, 'G1': 49, 'G#1': 52, 'A1': 55, 'A#1': 58, 'B1': 62,
        'C2': 65, 'C#2': 69, 'D2': 73, 'D#2': 78, 'E2': 82, 'F2': 87, 'F#2': 93, 'G2': 98, 'G#2': 104, 'A2': 110, 'A#2': 117, 'B2': 123,
        'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156, 'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196, 'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
        'C4': 262, 'C#4': 277, 'D4': 294, 'D#4': 311, 'E4': 330, 'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494
    }

    #levels
    e = {
        1: 'C4',
        2: 'D4',
        3: 'E4',
        4: 'F4',
        5: 'G4',
        6: 'A4',
        7: 'B4'
    }

    m = {
        1: 'C4',
        2: 'C#4',
        3: 'D4',
        4: 'D#4',
        5: 'E4',
        6: 'F4',
        7: 'F#4',
        8: 'G4',
        9: 'G#4',
        10: 'A4',
        11: 'A#4',
        12: 'B4',
        13: 'C3',
        14: 'D3',
        15: 'E3',
        16: 'F3',
        17: 'G3'
    }

    h = {
        1: 'C2',
        2: 'C#2',
        3: 'D2',
        4: 'D#2',
        5: 'E2',
        6: 'F2',
        7: 'F#2',
        8: 'G2',
        9: 'G#2',
        10: 'A2',
        11: 'A#2',
        12: 'B2',
        13: 'C3',
        14: 'C#3',
        15: 'D3',
        16: 'D#3',
        17: 'E3',
        18: 'F3',
        19: 'F#3',
        20: 'G3',
        21: 'G#3',
        22: 'A3',
        23: 'A#3',
        24: 'B3',
        25: 'C4',
        26: 'C#4',
        27: 'D4',
        28: 'D#4',
        29: 'E4',
        30: 'F4',
        31: 'F#4',
        32: 'G4',
        33: 'G#4',
        34: 'A4',
        35: 'A#4',
        36: 'B4'
    }

    b = {
        1: 'C1',
        2: 'C#1',
        3: 'D1',
        4: 'D#1',
        5: 'E1',
        6: 'F1',
        7: 'F#1',
        8: 'G1',
        9: 'G#1',
        10: 'A1',
        11: 'A#1',
        12: 'B1',
        13: 'C2',
        14: 'C#2',
        15: 'D2',
        16: 'D#2',
        17: 'E2',
        18: 'F2',
        19: 'F#2',
        20: 'G2',
        21: 'G#2',
        22: 'A2',
        23: 'A#2',
        24: 'B2',
        25: 'C3',
        26: 'C#3',
        27: 'D3',
        28: 'D#3',
        29: 'E3',
        30: 'F3',
        31: 'F#3',
        32: 'G3',
        33: 'G#3',
        34: 'A3',
        35: 'A#3',
        36: 'B3',
        37: 'C4',
        38: 'C#4',
        39: 'D4',
        40: 'D#4',
        41: 'E4',
        42: 'F4',
        43: 'F#4',
        44: 'G4',
        45: 'G#4',
        46: 'A4',
        47: 'A#4',
        48: 'B4'
    }

    note_types = {
        '1': 2000,    # Whole note (1 beat)
        '1/2': 1000,  # Half note (1/2 beat)
        '1/4': 500,   # Quarter note
        '1/8': 250    # Eighth note 
    }

    def play_note(note, level, delay=2000):
        if delay != 2000:
            delay = note_types.get(delay)

        debug_print(f"Getting: note-{note}, level-{level}")
        freq = level.get(note)

        if freq:
            winsound.Beep(freq, delay)
        else:
            print(f"Unknown note: {note}")

    def menu_duration():     
        print("Please pick a note duration!")
        print("-"*30)
        print("1. Whole Notes")
        print("2. Half Notes")
        print("3. Quarter Notes")
        print("4. Sixteenth Notes")
        print("-"*30)
        player_input = input("> ")
        clear_console()

        if player_input == "1":
            note_duration = '1'
        elif player_input == "2":
            note_duration = '1/2'
        elif player_input == "3":
            note_duration = '1/4'
        elif player_input == "4":
            note_duration = '1/8'

        return note_duration

    def menu_level():     
        print("Please pick a note duration!")
        print("-"*30)
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Beethoven")
        print("-"*30)
        player_input = input("> ")
        clear_console()

        if player_input == "1":
            level = 'e'
        elif player_input == "2":
            level = 'm'
        elif player_input == "3":
            level = 'h'
        elif player_input == "4":
            level = 'b'

        levels = {'e': e, 'm': m, 'h': h, 'b': b}
            
        current_level_dict = levels.get(level)

        return current_level_dict


    def menu_action():
        print("Please pick a mode!")
        print("-"*30)
        print("1. Guess")
        print("2. Leaderboard") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO MEEEEEEEEEEEEEEEEEEEEE
        print("3. Delete Data") # ANDD MEEEEE LATER
        print("4. Quit")
        print("-"*30)
        player_input = input("> ")
        clear_console()

        if player_input == "1":
            return False
        elif player_input == "2":
            level = 'm'
        elif player_input == "3":
            level = 'h'
        elif player_input == "4":
            return True

    while True: #Ear Trainer main-loop
        if menu_action():
            return
        
        print("Welcome To Ear Trainer!")
        while True: #get note_duration, level. Checks if they are present
            level = menu_level()

            note_duration = menu_duration()
        
            if note_duration and level:
                score = 0
                break
            else:
                print("Something Failed Im sorry :(")
        
        while True: #game-loop

            note_key = random.choice(list(level.keys()))     
            note_name = level[note_key]                       
            freq = note_freqs.get(note_name)

            while True:
                print(f'Note: {note_name}')

                if freq:
                    winsound.Beep(freq, note_types[note_duration])
                else:
                    print(f"Unknown note frequency for {note_name}")

                choice = input("1. New Note\n2. Play again\n3. Quit\n> ")
                
                choice = int(choice)

                clear_console()

                debug_print(input)

                if choice == 1:
                    break
                elif choice == 2:
                    choice
                elif choice == 3:
                    return
                else:
                    print("Misunderstood Choice")

if __name__ == "__main__":
    learn_game()