try:
    with open('../data/missing.txt', 'r') as f:
        needed_file = f.read()

except FileNotFoundError:
    print(f'Error: "missing.txt" was not found. Please check the file path and try again.')
