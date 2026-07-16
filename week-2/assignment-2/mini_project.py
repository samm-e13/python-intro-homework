f = float(input("Enter a temperature in Fahrenheit: "))
c = round(((f - 32) * 5)/9, 1)
print(f"{f:.1f}\N{DEGREE SIGN}F is {c:.1f}\N{DEGREE SIGN}C")