students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Sort by age (second item of each tuple)
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
