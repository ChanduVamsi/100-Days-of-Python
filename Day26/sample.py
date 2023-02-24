# import random, pandas

# arr = {n:n+1 for n in [1,2,3,4,5]}
# print(arr)

# arr = [n*2 for n in range(1,10) if n%2!=0]
# print(arr)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1,100) for student in names}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 40}

# dic_for_df = {"student": [student for student in passed_students.keys()], "score": [score for score in passed_students.values()]}
# passed_df = pandas.DataFrame(dic_for_df)
# for (index, row) in passed_df.iterrows():
#     print(row.score)