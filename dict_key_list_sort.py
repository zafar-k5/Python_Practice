student_grades = {
    "Alice": [85, 92, 88, 95],
    "Bob": [78, 85, 90, 82],
    "Charlie": [92, 88, 95, 91]
}

# for key in student_grades:
#     student_grades[key].sort()

# print(student_grades)

my_dict = {key:sorted(value) for key,value in student_grades.items()}
print(my_dict)
