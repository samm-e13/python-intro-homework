student = {"name": "Roy"
               , "grade": 73
               , "subjects": ["Calculus1", "Calculus2", "Calculus3"]}

for x, y in student.items():
    print(f"{x}: {y}")

student["graduated"] = False

print(student["graduated"])

for x, y in student.items():
    print(f"{x}: {y}")