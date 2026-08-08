
while True:
    value_entered = input("Enter a positive integer: ")
    if value_entered.isdigit():
        value_entered = int(value_entered)
        if value_entered <= 0:
            print("That's not a positive integer. Try again. ")
            continue
        else:
            print(f"Got it: {value_entered}")
        break
    else:
        print(f"That's not a positive integer. Try again. ")
        continue
        