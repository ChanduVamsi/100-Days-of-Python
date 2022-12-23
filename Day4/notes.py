#Randomization - Mersenne twister - https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
import random
import os

# from sample_package import pi
os.system("clear")

print(random.randint(-6, 35)) #inclusive of a,b - int
print(random.randrange(1, 10, 2)) #start stop step - int

print(random.random()) #only inclusive of a - float - always between 0 and 1
print(random.uniform(1,5)) #float with start and stop range

# print(pi)

print(20e7,"\n")

#Lists
characters = ["GLiTCH", "ASURA"]
characters.append("The Black Spade")
characters.extend(["The crazy monk", "KARMA"])
characters.insert(3, "z3ro")

print(characters[-2])
print(characters,"\n")

#Nested Lists
hustlers = ["Mr. God", "Nyx", "Neo"]
losers = ["Red pill", "Netflix", "Dopamine"]

people = [hustlers, losers]
print(people)