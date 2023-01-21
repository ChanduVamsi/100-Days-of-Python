import sys
sys.path.append("")

from util.helper import clear, colored_text

def add_item(travel_log, country_visited, total_visits, cities_visited):

    travel_log.append({
        "country": country_visited,
        "cities_visited": cities_visited,
        "total_visits": total_visits
    })
    
    # travel_log.extend(({
    #     "country": country_visited,
    #     "cities_visited": cities_visited,
    #     "total_visits": total_visits
    # },
    # {
    #     "country": "India",
    #     "cities_visited": ["New Delhi", "Goa", "Hyderabad", "Bangalore"],
    #     "total_visits": 12
    # }))

# Dictionaries = {key: value, key: value, .....}

# Dictionary definition and declaration
encyclopedia = {
    "Apple" : "A sweet and tart fruit which is usually bright red or green with subtle crunchy texture", 
    "Banana": "A sweet fruit with curved shape high with potassium",
    "Orange": "A citrus fruit with high levels of vitamin D essential for your daily intake"
}

# Accessing specific items in dictionary using key
clear()
print(encyclopedia["Banana"],"\n")

# Add a new item to the dictionary
encyclopedia["Pineapple"] = "A tropical citrus fruit with high amounts of bromaline"

# Loop through a dictionary
for fruit in encyclopedia: print(f"{fruit}: {encyclopedia[fruit]}")

# Empty Dictionary
# encyclopedia = {}
# clear()
# print(encyclopedia)

# Edit an item in dictionary
print("")
encyclopedia["Pineapple"] = "A tropical citrus fruit with goes well with cocktails and other drinks on a hot summer day"
for fruit in encyclopedia: print(f"{fruit}: {encyclopedia[fruit]}")

clear()
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90: student_grades[student] = "S"
    elif student_scores[student] > 80: student_grades[student] = "A"
    elif student_scores[student] > 70: student_grades[student] = "B"
    elif student_scores[student] > 60: student_grades[student] = "C"
    elif student_scores[student] > 50: student_grades[student] = "D"
    else: student_grades[student] = "F"
    print(f"{student} is graded {student_grades[student]}")

clear()

#Nesting dictionaries
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 4
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 3
        }
}
print(colored_text(travel_log, "light_green"))

# Nesting dictionaries inside lists
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 4
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 3
    }
]
print(colored_text(travel_log, "red"), end = "\n\n")

clear()
add_item(travel_log, "Russia", 2, ["Moscow", "Saint Petersburg"])
print(colored_text(travel_log, "red"), end="\n\n")