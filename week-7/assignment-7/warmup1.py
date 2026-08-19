n = 0;

with open('../data/notes.txt', 'r') as data_file:
    for record in data_file:
        n += 1
        print(f"Line {n}: {record.strip()}")