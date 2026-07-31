students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

current_max = 0
top_scorer = {}
for student in students:
    if student["score"] <= current_max:
        continue
    else:
        current_max = student["score"]
        top_scorer["name"] = student["name"]
        top_scorer["score"] = student["score"]

print(f"Top scorer: {top_scorer['name']} ({top_scorer['score']})")

total_score = 0
for student in students:
    total_score += student["score"]
avg = total_score / len(students)
print(f"Class average: {avg:.1f}")

subjects = set()
for student in students:
    subjects.add(student["subject"])
print(f"Subjects offered: {subjects}")

high_scores = []
for student in students:
    if student["score"] > 75:
        high_scores.append(student["name"])
print(f"High scorers: {high_scores}")

