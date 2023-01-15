import os, sys

from time import sleep
from termcolor import colored

def clear():
	os.system("clear")

def type_writer(text, speed = 0.02):
	for char in text:
		sleep(speed)
		sys.stdout.write(char)
		sys.stdout.flush()

def colored_text(text, color = "light_green"):
	return colored(text, color, attrs=['blink'])