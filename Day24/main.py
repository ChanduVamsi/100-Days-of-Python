#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os

PLACEHOLDER = "[name]"


path_to_file = os.path.join(os.path.dirname(__file__), './Input/Names/invited_names.txt')
with open(path_to_file) as names_file:
    names = names_file.readlines()

path_to_file = os.path.join(os.path.dirname(__file__), './Input/Letters/starting_letter.txt')
with open(path_to_file) as letter_file:
    letter = letter_file.read()
    for name in names: 
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        path_to_file = os.path.join(os.path.dirname(__file__), f'./Output/ReadyToSend/letter_for_{name.strip()}.txt')
        with open(path_to_file, mode="w") as add_letter:
            add_letter.write(new_letter)