import os, sys

from time import sleep
from termcolor import colored

def clear():
	"""Clears the output terminal"""
	os.system("clear")

def type_writer(text, speed = 0.02):
	"""Prints the output in a typewriter format"""
	for char in text:
		sleep(speed)
		sys.stdout.write(char)
		sys.stdout.flush()

def colored_text(text, color = "light_green"):
	"""Returns the colored output. 
	Default is neon green"""
	return colored(text, color, attrs=['blink'])