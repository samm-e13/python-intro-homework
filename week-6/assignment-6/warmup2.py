def celsius_to_fahrenheit(c):
    value = (c*9/5) + 32
    print(f"{c}\u00b0C = {value:.1f}\u00b0F")

def fahrenheit_to_celsius(f):
    value = (f-32) * 5/9
    print(f"{f}\u00b0F = {value:.1f}\u00b0F")

celsius_to_fahrenheit(0)
celsius_to_fahrenheit(100)
fahrenheit_to_celsius(72)
