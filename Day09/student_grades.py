student_scores = {
    'Harry':81,
    'Ron':78,
    'Hermione':99,
    'Draco':74,
    'Neville':62,
}

student_grades = {}

# Grading criteria
    # 91-100 "Outstanding"
    # 81-90 "Exceeds Expections"
    # 71-80 "Acceptable"
    # 70 or lower "Fail"

for key in student_scores:
    score = student_scores[key]
    if score>90 and score<=100:
        student_grades[key] = 'Outstanding'
    elif score>80 and score<=90:
        student_grades[key] = 'Exceeds Expectations'
    elif score>70 and score<=80:
        student_grades[key] = 'Acceptable'
    elif score<=70:
        student_grades[key] = 'Fail'


for items in student_grades.items():
    print(items)