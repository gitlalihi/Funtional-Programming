#Python program that creates a list of dictionaries containing student information (name, age, grade) and uses the filter function to extract students with a grade greater than or equal to 95.
# Define a list of dictionaries containing student information
students = [
    {"name": "Canditate 1", "age": 17, "grade": 97},
    {"name": "Candtate 2", "age": 16, "grade": 92},
    {"name": "Canditate 3", "age": 17, "grade": 90},
    {"name": "Canditae 4", "age": 16, "grade": 94},
    {"name": "Candidate 5", "age": 17, "grade": 100},
]
print("Student information:")
print(students)

def has_high_grade(student):
    return student["grade"] >= 95


high_grade_students = list(filter(has_high_grade, students))
print("\nStudents with high grades:")

print(high_grade_students)
