numerator = float(input(f"Enter the numerator:"))
denominator = float(input(f"Enter the denominator:"))

try:
    result = (numerator / denominator)
    print(f"{numerator} \u00f7 {denominator} = {result:.1f}")
except ZeroDivisionError:
    print(f"Can't divide by zero \u2014 please try a non-zero denominator.")




    