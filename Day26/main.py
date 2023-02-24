import os, pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

path_to_file = os.path.join(os.path.dirname(__file__), 'nato_phonetic_alphabet.csv')
data = pandas.read_csv(path_to_file)
nato_dict = {row.letter: row.code for (_, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

username = input("My name is ").upper()
spell_name = [nato_dict[letter] for letter in list(username)]
print(spell_name)
