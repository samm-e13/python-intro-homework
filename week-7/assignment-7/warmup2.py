import csv

with open('../data/students.csv', 'r') as data_file:
    the_file = csv.DictReader(data_file)
    for line in the_file:
        print(f"{line['name']}: {line['score']}")
