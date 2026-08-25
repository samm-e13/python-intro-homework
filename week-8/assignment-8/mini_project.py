import os
import csv

messy_path = os.path.join("..", "data", "messy_data.csv")

try:
    with open(messy_path, "r") as f:
        file = csv.DictReader(f)
        messy_file = list(file)
except FileNotFoundError:
    print(f"Error. File not found.")

else:
    messy_list = []
    clean = []
    for row_value, line in enumerate(messy_file, start=1):
        if None in line:
            key_error = f"Row {row_value}: extra column detected - skipped"
            messy_list.append(key_error)
        try:
            cost_list_dict = {
                "name": line["name"],
                "category": line["category"],
                "amount": float(line["amount"])
            }

            clean.append(cost_list_dict)
        except ValueError as e:
            skip = f"Row {row_value}: ValuueError - {e}"
            messy_list.append(skip)
    
    skipped = len(messy_list)
    cleann = len(clean)
    total = skipped + cleann

    print(f"=== CSV Report ===")
    print(f"Rows attempted: {total}")
    print(f"Rows parsed:    {cleann}")
    print(f"Rows skipped:    {skipped}")

    print()
    print(f"Skipped rows:")
    for line in messy_list:
        print(f" {line}") 
    
    print()
    print(f"Clean data:")
    for line in clean:
        print(f"{line['name']} | {line['category']} | ${line['amount']:.2f}")