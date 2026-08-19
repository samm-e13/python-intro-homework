import os 
import csv

the_path = os.path.join('..', 'data', 'expenses.csv')

print(f"{os.getcwd()}")

if not os.path.exists(the_path):
    print(f"expenses.csv not found.")
else:
    print(f"expenses.csv found.\n{the_path}")
    


