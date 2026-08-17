def celsius_to_fahrenheit(c):
    value = (c*9/5) + 32
    
    return value  

def fahrenheit_to_celsius(f):
    value = (f-32) * 5/9
    return value
  
print(f"0\u00b0C = {celsius_to_fahrenheit(0):.1f}\u00b0F")
print(f"100\u00b0C = {celsius_to_fahrenheit(100):.1f}\u00b0F")
print(f"72\u00b0F = {fahrenheit_to_celsius(72):.1f}\u00b0C")



