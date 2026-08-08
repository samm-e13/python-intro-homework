names = ["Roy", "David", "Marcus","Elizabeth"]

name_var = input("Enter a name to search for: ").capitalize()
success = False

for n in range(len(names)):
    if names[n] == name_var:
        ind = n
        success = True
        break

if success:
    print(f"Found \"{name_var}\" at index {ind}.")
else:
    print(f" \"{name_var}\" was not found in the list.")