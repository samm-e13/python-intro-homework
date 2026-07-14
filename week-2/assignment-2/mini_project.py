f = float(input("Enter a temperature in Farenheit: "))
c = round(((f - 32) * 5)/9, 1)
print(f"Enter a temperature in Farenheit: {f}")
print(f"{f:.1f}\N{DEGREE SIGN}F is {c:.1f}\N{DEGREE SIGN}C")