#Conditional and nested statements
#Leap year - every year evenly divisible by 4 is a leap year exceot every year that is evenly divisible by 100 unless it is also evenly divisible by 400

year = int(input("Enter a year: "))
if year%4 == 0:
    if year%100 != 0:
        print(f"{year} is a leap year")
    elif year%400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

#How to not make print statement go next line
print("Hi there!")
print("How're you? ", end='')
print("I wish you well!")

#Logical operators: and or not
a = 12
if a>10 and a<13: print("AND BOTH YES")
if a>10 or a<13: print("OR BOTH YES")
if a>10 and a>13: print("AND ONE YES ONE NO")
if a>10 or a>13: print("OR ONE YES ONE NO")
if not a==13: print("NOT OPERATOR")

