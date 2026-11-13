

students = [
    ("Asha", [72, 33, 80]),
    ("Ravi", [30, 31, 29]),
    ("Meena", [99, 45, 38]),
]

PASS_MARK = 35
MAX_MARKS = 100

for name, marks in students:
    grace_left = 10
    final_marks = []
    for m in marks:
        if m < PASS_MARK and PASS_MARK - m <= 5 and grace_left >= PASS_MARK - m:
            need = PASS_MARK - m
            m = m + need
            grace_left = grace_left - need
        if m > MAX_MARKS:
            m = MAX_MARKS
        final_marks.append(m)

    result = "PASS"
    for m in final_marks:
        if m < PASS_MARK:
            result = "FAIL"

    average = sum(final_marks) / len(final_marks)
    if result == "FAIL":
        grade = "Fail"
    elif average >= 75:
        grade = "Distinction"
    elif average >= 60:
        grade = "First Class"
    else:
        grade = "Second Class"

    print(name, "| Original:", marks, "| After grace:", final_marks, "|", result, "|", grade)
