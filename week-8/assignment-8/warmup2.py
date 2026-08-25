numerator = input(f"Enter the numerator:")
denominator = input(f"Enter the denominator:")

try:
    result = (float(numerator) / float(denominator))
    print(f"{float(numerator)} \u00f7 {float(denominator)} = {result:.1f}")
except ZeroDivisionError:
    print(f"Can't divide by zero \u2014 please try a non-zero denominator.")




    