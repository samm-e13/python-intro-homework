def celsius_to_fahrenheit(c):
    value = (c*9/5) + 32
    return c, value
   

def fahrenheit_to_celsius(f):
    value = (f-32) * 5/9
    return f, value
  
c_1 = celsius_to_fahrenheit(0) 
c_2 = celsius_to_fahrenheit(100)
f_1 = fahrenheit_to_celsius(72)
print(f"{c_1[0]}\u00b0C = {c_1[1]:.1f}\u00b0F")
print(f"{c_2[0]}\u00b0C = {c_2[1]:.1f}\u00b0F")
print(f"{f_1[0]}\u00b0F = {f_1[1]:.1f}\u00b0C")



