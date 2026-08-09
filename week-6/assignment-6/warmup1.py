def greeting(name, greet="hello"):
    print(f"{greet.capitalize()}, {name.capitalize()}!")

greeting("alex")
greeting("alex", "good morning")
greeting("alex", greet="hello")