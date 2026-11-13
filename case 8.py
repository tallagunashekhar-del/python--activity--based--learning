

students = ["Asha", "Ravi", "Meena", "Kiran"]
subjects = ["Maths", "Physics", "Python"]
marks = [
    [85, 78, 92],
    [45, 52, 60],
    [90, 88, 95],
    [40, 35, 48],
]

# Row-wise: total and average per student
print("--- Student-wise ---")
best_total = 0
topper = ""
for i in range(len(students)):
    total = sum(marks[i])
    print(students[i], "| Total:", total, "| Average:", round(total / len(subjects), 2))
    if total > best_total:
        best_total = total
        topper = students[i]
print("Topper:", topper, "with", best_total, "marks")

# Column-wise: average per subject
print("\n--- Subject-wise ---")
for j in range(len(subjects)):
    col_total = 0
    for i in range(len(students)):
        col_total = col_total + marks[i][j]
    avg = col_total / len(students)
    print(subjects[j], "| Average:", round(avg, 2), end="")
    if avg < 60:
        print("  <-- Low average subject", end="")
    print()
