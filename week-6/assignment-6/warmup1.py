def greet(name, greeting="Hello"):
    print(f"{greeting.capitalize()}, {name.capitalize()}!")

greet("alex")
greet("alex", "good morning")
greet("alex", greeting="Hello")