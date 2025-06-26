import random

numbers = [2, 4, 6, 8, 0]
new_list = [n+1 for n in numbers]
print(new_list)

namez = 'Nageba'
letters_list = [letter for letter in namez]
print(letters_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie', 'Calvin']
capital_names = [name.upper() for name in names if len(name) < 5]
print(capital_names)

student_scores = {student:random.randint(0, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)