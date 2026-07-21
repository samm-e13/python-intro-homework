day = input("what day is it? ").lower()
time = input("What time of day? ").lower()

dow = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
tod = ["morning", "afternoon", "evening"]

dow_group1 = ["monday", "tuesday", "wednesday"]
dow_group2 = ["thursday", "friday"]
dow_group3 = ["saturday", "sunday"]

if day not in dow:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
elif  time not in tod:
    print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening...")

elif day == 'monday' and time == "morning":
    print("Suggestion: Monday morning's are perfect time for a jog or walk.")
elif day == 'monday' and time == "afternoon":
    print("Suggestion: Monday afternoon's are perfect time for coding.")
elif day == 'monday' and time == "evening":
    print("Suggestion: Monday evening's are perfect time learning.")
elif day == 'tuesday' and time == "morning":
    print("Suggestion: Tuesday morning's are perfect siesta or book reading time")
elif day == 'tuesday' and time == "afternoon":
    print("Suggestion: Tuesday afternoon's are perfect for eating")
elif day == 'tuesday' and time == "evening":
    print("Suggestion: Tuesday evening's should include weights")
elif day == 'wednesday' and time == "morning":
    print("Suggestion: Wednesday morning's are perfect for board-games!")
elif day == 'wednesday' and time == "afternoon":
    print("Suggestion: Wednesday afternoon's require focus time!")
elif day == 'wednesday' and time == "evening":
    print("Suggestion: Wednesday evening's are better with family")
elif day == 'thursday' and time == "morning":
    print("Suggestion: Latter-half of week morning's are perfect time for a coffee shop visit.")
elif day == 'thursday' and time == "afternoon":
    print("Suggestion: Thursday afternoon's are boring.")
elif day == 'thursday' and time == "evening":
    print("Suggestion: Thursday evening news is a must have.")
elif day == 'friday' and time == "morning":
    print("Suggestion: Friday morning's are made for lunch with friends.")
elif day == 'friday' and time == "afternoon":
    print("Suggestion: Friday afternoon's require happy hour.")
elif day == 'friday' and time == "evening":
    print("Suggestion: Friday evening's need supervision")
elif day == 'saturday' and time == "morning":
    print("Suggestion: Saturday morning's were created for wine!")
elif day == 'saturday' and time == "afternoon":
    print("Suggestion: Have more wine.")
elif day == 'saturday' and time == "evening":
    print("Suggestion: Have some cold water")
elif day == 'sunday' and time == "morning":
    print("Suggestion: Weekend morning's are perfect for home-cooked breakfast.")
elif day == 'sunday' and time == "afternoon":
    print("Suggestion: Sunday is time for church.")
elif day == 'sunday' and time == "evening":
    print("Suggestion: Menudo for breakfast is not for the feint-hearted")



