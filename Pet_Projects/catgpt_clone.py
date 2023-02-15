# Clone implementation of https://catgpt.wvd.io/

import sys, random
sys.path.append("")

from util.helper import clear, colored_text, type_writer

def meow():
    meom = "Meow"
    for _ in range(random.randint(1, 10)): meom += " meow"
    return meom + random.choice(['.', '!', '?'])

logo = '''   ______      __  __________  ______
  / ____/___ _/ /_/ ____/ __ \/_  __/
 / /   / __ `/ __/ / __/ /_/ / / /   
/ /___/ /_/ / /_/ /_/ / ____/ / /    
\____/\__,_/\__/\____/_/     /_/     
'''

clear()
print(colored_text(logo), end="")
print(colored_text("\n   What if ChatGPT were a cat?\n"))
while True:
    type_writer(f"\n🐱: {colored_text(meow())}")
    input(f"\n\n🤷: ")