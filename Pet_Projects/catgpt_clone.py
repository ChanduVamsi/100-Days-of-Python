# Clone implementation of https://catgpt.wvd.io/

import sys, random
sys.path.append("")

from util.helper import clear, colored_text, type_writer

def meow():
    type_writer(colored_text(f"\n{random.choice(['🐱', '🙀', '😿', '😼', '😺', '😻'])}: Meow{(random.randint(1, 10) * ' meow')}{random.choice(['.', '!', '?', '🐾'])}"))
    while input(f"\n\n{random.choice(['🤔', '🤧', '😂', '🤣', '😉', '😍', '🫣', '😲'])}: ").lower() != "grr":
        type_writer(colored_text(f"\n{random.choice(['🐱', '🙀', '😿', '😼', '😺', '😻'])}: Meow{(random.randint(1, 10) * ' meow')}{random.choice(['.', '!', '?', '🐾'])}"))

logo = '''   ______      __  __________  ______
  / ____/___ _/ /_/ ____/ __ \/_  __/
 / /   / __ `/ __/ / __/ /_/ / / /   
/ /___/ /_/ / /_/ /_/ / ____/ / /    
\____/\__,_/\__/\____/_/     /_/     
'''

catlogo = '''      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  '''

clear()
print(colored_text(logo), end="")
print(colored_text("\n What if CatGPT was on terminal?\n"))
meow()