student_score = {
    'Ivan'  : 5.00,
    'Alex'  : 3.50,
    'Maria' : 5.50,
    'Georgy': 5.00
}

for key, value in student_score.items():
    min_score = min(student_score.values())
    max_score = max(student_score.values())
    min_key = min(student_score, key=student_score.get)
    max_key = max(student_score, key=student_score.get)


print (f'{min_key} - {min_score}')
print (f'{max_key} - {max_score}')