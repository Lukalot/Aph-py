# © 2020 Lukalot (Luke Arnold)

from random import choice
import os
import difflib
import json

title_art_old = '''                       _____   ___ 
 __ ____  _  ____ __  /  _  \ |   |
|  |  \ \/ \/ /  |  \/  /_\  \|   |
|  |  /\     /|  |  /    |    \   |
|____/  \/\_/ |____/\____|__  /___|
© 2020 Lukalot              \/     '''

title_art = '''
  █████╗ ██████╗ ███╗ ███╗
 ██╔══██╗██╔══██╗██╔╝ ██╔╝
 ███████║██████╔╝███████║
 ██╔══██║██╔═══╝ ██╔══██║
 ██║  ██║██║     ██║  ██║
 ╚═╝  ╚═╝╚═╝    ███║ ███║
 © 2020 Lukalot ╚══╝ ╚══╝'''

help_text = '''================== uwuAI Help ==================
!h / !help : Looks like you found this one
!m / !memory : Output memory data
!ms / !memorysize : Output memory size (based on the amount of keys stored in json)
!r / !reset : Reset program to initial state
!f / !forget : Forget all memory data
!c / !clear : Clear console
!sl / !shouldlearn : Toggle learning on or off
!s / !save : Save memory to the given save file
!ld / !load : Load memory from the given save file
================================================'''

selection_range = 1

def console_fresh(title):
    os.system('cls')
    print(title)
    print('=' * 40)

response = ""
memory = {}
should_learn = True

def converse(user_input):
    global response
    global memory

    if should_learn:
        if memory.get(response) == None:
            memory[response] = []
        memory[response].append(user_input)
        response = None

    if len(list(memory.keys())) > 0:
        if memory.get(user_input):
            response = choice(memory.get(user_input))
        else:
            response = choice(memory.get(difflib.get_close_matches(user_input, list(memory.keys()), selection_range, 0)[0]))
    else:
        print('uwuAI has no learned data to respond with - turn on learning with the !learn special command.')

    if response:
        print('>> ' + response)
    else:
        print('<NO_RESPONSE>')


console_fresh(title_art)
while True:
    user_input = input()

    if user_input.startswith('!'):
        arguments = user_input[1:].split(' ')
        
        if arguments[0] == "help" or arguments[0] == "h":
            print(help_text)
        elif arguments[0] == "memory" or arguments[0] == "m":
            print(memory)
        elif arguments[0] == "memorysize" or arguments[0] == "ms":
            print("Memory keys size: " + str(len(list(memory.keys()))))
        elif arguments[0] == "forget" or arguments[0] == "f":
            memory = {}
            response = ""
            print('Forgot all memory.')
        elif arguments[0] == "clear" or arguments[0] == "c":
            console_fresh(title_art)
        elif arguments[0] == "reset" or arguments[0] == "r":
            memory = {}
            response = ""
            console_fresh(title_art)
        elif arguments[0] == "shouldlearn" or arguments[0] == "sl":
            should_learn = not should_learn
            print("Learning set to " + str(should_learn))
        elif arguments[0] == "save" or arguments[0] == "s":
            if len(arguments) >= 2:
                with open('saves/' + arguments[1] + '.json', 'w') as f:
                    json.dump(memory, f)
                print("Saved" + str(len(list(memory.keys()))) + " memory keys to saves/" + arguments[1] + '.json')
            else:
                with open('saves/_default.json', 'w') as f:
                    json.dump(memory, f)
                print('Saved ' + str(len(list(memory.keys()))) + ' memory keys to default save location')

        elif arguments[0] == "load" or arguments[0] == "ld":
            if len(arguments) >= 2:
                with open('saves/' + arguments[1] + '.json', "r") as f:
                    memory = json.load(f)
                print('Loaded ' + str(len(list(memory.keys()))) + ' memory keys to memory from saves/' + arguments[1] + '.json')
            else:
                with open('saves/_default.json', "r") as f:
                    memory = json.load(f)
                print('Loaded ' + str(len(list(memory.keys()))) + ' memory keys to memory from default save location')
    else:
        converse(user_input)
