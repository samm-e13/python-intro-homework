score = int(input("Enter a score: "))
def is_valid_score(score):
    if score >= 0 and score <=100:
        return True
    else:
        return False

if is_valid_score(score):
    print(f"Valid score.")
else:
    print(f"Invalid score — must be between 0 and 100.")
    