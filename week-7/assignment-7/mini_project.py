import os 
import csv
import datetime

the_path = os.path.join('..', 'data', 'expenses.csv')

if not os.path.exists(the_path):
    print(f"expenses.csv not found.")
else:
    with open(the_path, 'r') as the_file:
        the_list = list(csv.DictReader(the_file))

    for record in the_list:
        record['amount'] = float(record['amount'])

    filtered = [record for record in the_list if record['category'] == 'Food']

    total_spent = sum(filtered_item['amount'] for filtered_item in filtered)

    with open('food_report.txt', 'w') as file:
        current_date = datetime.datetime.now()
        file.write(f"Food Expense Report — generated {current_date.strftime('%B %d, %Y')}\n")
        for element in filtered:
            file.write(f"{element['date']}: ${element['amount']:.2f}\n")
        file.write(f"Total: ${total_spent:.2f}\n")    

with open('food_report.txt', 'r') as file:
    print(file.read())