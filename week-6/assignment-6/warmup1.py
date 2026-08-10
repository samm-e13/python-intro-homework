def greet(name, greeting="hello"):
    print(f"{greeting.capitalize()}, {name.capitalize()}!")

greet("alex")
greet("alex", "good morning")
greet("alex", greeting="hello")