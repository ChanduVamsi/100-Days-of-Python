#Password Generator Project
import os, random
os.system("clear")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pswd = ""
for i in range(0, nr_letters): pswd += random.choice(letters)
for i in range(0, nr_symbols): pswd += random.choice(symbols)
for i in range(0, nr_numbers): pswd += random.choice(numbers)

os.system("clear")
print(f"\nPassword generated just for you: {pswd}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pswd_list = (list(pswd.strip('')))
random.shuffle(pswd_list)

new_pswd = ""
for c in pswd_list: new_pswd += c

print(f"Randomized password for the above is {new_pswd}\n")