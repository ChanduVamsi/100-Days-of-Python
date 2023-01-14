#Prime code
def prime_checker(num):
    if num < 2: return False
    else: 
        for i in range(2, num): 
            if num % i == 0: return False
    return True

num = int(input("Enter a number to check if it's a prime: "))
if prime_checker(num): print(f"{num} is a prime number.")
else: print(f"{num} is not a prime number.")