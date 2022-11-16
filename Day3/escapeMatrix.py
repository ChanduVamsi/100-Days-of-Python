import os
import sys

os.system("pip3 install playsound")
os.system("clear")

from time import sleep
from playsound import playsound

#Welcome to the real world, Neo!

os.system("clear")
intro = "\nHi Neo, this is Morpheus!\n"
decision = "\nI offer you two pills. \n\nYou take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. \n\nYou take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes!"
angel = '''\n\n     __/)     (\__
  ,-'~~(   _   )~~`-.
 /      \/'_`\/      \
|       /_(_)_\       |
|     _(/(\_/)\)_     |
|    / // \ / \\ \    |
 \  | ``  / \ ''  |  /
  \  )   /   \   (  /
   )/   /     \   \(
   '    `-`-'-'    `\n\n'''
love = "\nYou'll have to sacrifice everything and everyone you love if you go down this road. If you still want to continue: Press Yes else No: "
matrix = "\nGood. Now let's break the matrix. You are no longer a puppet for the elite!\n\nWelcome to the real world!"

for char in intro:
    sleep(0.07)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in decision:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in angel:
    sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()

pill = input("Select one: Blue pill or Red pill: ")

if "red" in pill.lower():
    for char in love:
        sleep(0.08)
        sys.stdout.write(char)
        sys.stdout.flush()
    choice = input()
    os.system("clear")
    if "yes" in choice.lower():
        for char in matrix:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound("Day3/matrix.mp3")
else:
    os.system("clear")