for n in range(1,31):
    if (n % 3 == 0 and n % 5 == 0):
        print(f"FizzBuzz")
    elif n % 3 == 0:
        print(f"Fizz")
    elif n % 5 == 0:
        print(f"Buzz")
    else:
        print(f"{n}")