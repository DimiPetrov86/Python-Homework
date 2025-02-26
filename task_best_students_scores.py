student_score = {
    'Ivan'  : 5.00,
    'Alex'  : 3.50,
    'Maria' : 5.50,
    'Georgy': 5.00
}


for key, value in student_score.items():
    if value > 4:
        print (f'{key} - {value}')