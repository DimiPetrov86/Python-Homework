student_score = {
    'Ivan'  : 5.00,
    'Alex'  : 3.50,
    'Maria' : 5.50,
    'Georgy': 5.00
}

for key, values in student_score.items():
    min_score = min(student_score.values())
    max_score = max(student_score.values())
print (f'{key} - {min_score}')
print (f'{key} - {max_score}')