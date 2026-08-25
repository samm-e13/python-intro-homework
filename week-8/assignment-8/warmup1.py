while True:
    user_input = input(f"Enter a number:")
    try:
        test_input = float(user_input)
        print(f"You entered: {test_input:.1f}")
        break
    except ValueError:
        print(f"That's not a valid number. Try again.")
