# © 2020 Lukalot (Luke Arnold)

from random import choice
import os
import difflib
import json

title_art = '''                       _____   ___ 
 __ ____  _  ____ __  /  _  \ |   |
|  |  \ \/ \/ /  |  \/  /_\  \|   |
|  |  /\     /|  |  /    |    \   |
|____/  \/\_/ |____/\____|__  /___|
© 2020 Lukalot              \/     '''

help_text = '''================== uwuAI Help ==================
!h / !help : Looks like you found this one
!m / !memory : Output memory data
!ms / !memorysize : Output memory size (based on the amount of keys stored in json)
!r / !reset : Reset program to initial state
!f / !forget : Forget all memory data
!c / !clear : clear console
!sl / !shouldlearn : toggle learning on or off
!s / !save : save memory to save.json
!ld / !load : load memory from save.json
================================================'''

def console_fresh(title):
    os.system('cls')
    print(title)
    print('=' * 40)

response = '<NEW_CONVERSATION_INITIAL_VALUE>'
memory = {}
should_learn = True
save_location = "save.json"

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
            response = choice(memory.get(difflib.get_close_matches(user_input,
list(memory.keys()), 1, 0)[0]))
    else:
        print('NOTE: uwuAI has no learned data to respond with - turn on learning with the !learn special command')

    if response:
        print('>> ' + response)
    else:
        print('<NO_RESPONSE>')


console_fresh(title_art)
while True:
    user_input = input()
    if user_input == "!help" or user_input == "!h":
        print(help_text)
    elif user_input == "!memory" or user_input == "!m":
        print(memory)
    elif user_input == "!memorysize" or user_input == "!ms":
        print("Memory keys size: " + str(len(list(memory.keys()))))
    elif user_input == "!forget" or user_input == "!f":
        memory = {}
        response = '<NEW_CONVERSATION_INITIAL_VALUE>'
        print('Forgot all memory.')
    elif user_input == "!clear" or user_input == "!c":
        console_fresh(title_art)
    elif user_input == "!reset" or user_input == "!r":
        memory = {}
        response = '<NEW_CONVERSATION_INITIAL_VALUE>'
        console_fresh(title_art)
    elif user_input == "!shouldlearn" or user_input == "!sl":
        should_learn = not should_learn
        print("Learning set to " + str(should_learn))
    elif user_input == "!save" or user_input == "!s":
        with open(save_location, 'w') as f:
            json.dump(memory, f)
        print(str(len(list(memory.keys()))) + " memory keys saved to " + save_location)

    elif user_input == "!load" or user_input == "!ld":
        with open(save_location, "r") as f:
            memory = json.load(f)
        print('Loaded ' + str(len(list(memory.keys()))) + ' memory keys to memory from ' + save_location)
    else:
        converse(user_input)
