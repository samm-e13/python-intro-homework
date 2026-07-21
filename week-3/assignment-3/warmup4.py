num = int(input("Enter a number:"))

if num == 0:
    print(f"{num} is zero.")
elif num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")

if num % 2 == 0:
    print(f"{num} is even.")
elif num == 0:
    print(f"{num} is even.")
else: 
    print(f"{num} is odd.")
