numerator = int(input(f"Enter the numerator:"))
denominator = int(input(f"Enter the denominator:"))

try:
    result = (numerator / denominator)
    print(f"{numerator} \u00f7 {denominator} = {result:.1f}")
except ZeroDivisionError:
    print(f"Can't divide by zero - please try a non-zero denominator.")




    