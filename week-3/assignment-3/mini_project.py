day = input("what day is it? ").lower()
time = input("What time of day? ").lower()

dow = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
tod = ["morning", "afternoon", "evening"]

dow_group1 = ["monday", "tuesday", "wednesday"]
dow_group2 = ["thursday", "friday"]
dow_group3 = ["saturday", "sunday"]

if day not in dow:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
if  time not in tod:
    print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening...")

if day == 'monday' and time == "morning":
    print("Front-half week morning's are perfect time for a jog or walk.")
if day == 'monday' and time == "afternoon":
    print("Front-half week afternoon's are perfect time for a jog or walk.")
if day == 'monday' and time == "evening":
    print("Front-half week evening's are perfect time for a jog or walk.")
elif day == 'tuesday' and time == "morning":
    print("Front-half week morning's are perfect siesta or book reading time")
elif day == 'tuesday' and time == "afternoon":
    print("Front-half week afternoon's are perfect siesta or book reading time")
elif day == 'tuesday' and time == "evening":
    print("Front-half week afternoon's are perfect siesta or book reading time")
elif day == 'wednesday' and time == "morning":
    print("Wednesday morning's are perfect for board-games!")
elif day == 'wednesday' and time == "afternoon":
    print("Wednesday afternoon's are perfect for board-games!")
elif day == 'wednesday' and time == "evening":
    print(""Wednesday evening's are perfect for board-games!")
elif day == 'thursday' and time == "morning":
    print("Latter-half of week morning's are perfect time for a coffee shop visit.")
elif day == 'thursday' and time == "afternoon":
    print("Latter-half of week afternoon's are perfect time for a coffee shop visit.")
elif day == 'thursday' and time == "evening":
    print("Latter-half of week evening's are perfect time for a coffee shop visit.")
elif day == 'friday' and time == "morning":
    print("Friday morning's are made for lunch with friends.")
elif day == 'friday' and time == "afternoon":
    print("Friday afternoon's are made for lunch with friends.")
elif day == 'friday' and time == "evening":
    print("Friday evening's are made for lunch with friends.")
elif day == 'saturday' and time == "morning":
    print("Weekend morning's were created for wine!")
elif day == 'saturday' and time == "afternoon":
    print("Weekend afternoon's were created for wine!")
elif day == 'saturday' and time == "evening":
    print("Weekend evening's were created for wine!")
elif day == 'sunday' and time == "morning":
    print("Weekend morning's are perfect for home-cooked breakfast.")
elif day == 'sunday' and time == "afternoon":
    print("Weekend afternoon's are perfect for home-cooked breakfast.")
elif day == 'sunday' and time == "evening":
    print("Weekend evening's are perfect for home-cooked breakfast.")



