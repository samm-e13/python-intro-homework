day = input("what day is it? ").lower()
time = input("What time of day? ").lower()

dow = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
tod = ["morning", "afternoon", "evening"]

dow_group1 = ["monday", "tuesday", "wednesday"]
dow_group2 = ["thursday", "friday"]
dow_group3 = ["saturday", "sunday"]

if day.lower() not in dow:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")

if time.lower() not in tod:
    print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening...")

if day.lower() in dow_group1 and time.lower() == "morning":
    print("Front-half week morning's are perfect time for a jog or walk.")
elif day.lower() in dow_group1 and time.lower() == "afternoon":
    print("Front-half week afternoon's are perfect siesta or book reading time")
elif day.lower() in dow_group1 and time.lower() == "evening":
    print("Front-half week evening's are perfect for board-games!")
elif day.lower() in dow_group2 and time.lower() == "morning":
    print("Latter-half of week morning's are perfect time for a coffee shop visit.")
elif day.lower() in dow_group2 and time.lower() == "afternoon":
    print("Latter-half of week afternoon's are made for lunch with friends.")
elif day.lower() in dow_group2 and time.lower() == "evening":
    print("Latter-half of week evening's were created for wine!")
elif day.lower() in dow_group3 and time.lower() == "morning":
    print("Weekend morning's are perfect for home-cooked breakfast.")
elif day.lower() in dow_group3 and time.lower() == "afternoon":
    print("Weekend afternoon's are made for fishing.")
elif day.lower() in dow_group3 and time.lower() == "evening":
    print("Weekend evening's were created for movies!")

