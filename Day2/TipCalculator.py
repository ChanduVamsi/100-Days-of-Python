#Find the split bill each person need to pay after adding up the tip to the bill

bill = float(input("Welcome to tip calculator.\nWhat was the total bill? $"))
tip_percent = float(input("What percentage of tip would you like to give? 10, 12, or 15? "))/100
total_bill = bill + (bill * tip_percent)

number_of_people = int(input("How many people to split the bill? "))
print(f"Each person should pay: {round(total_bill/number_of_people,2)}")