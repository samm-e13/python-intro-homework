numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    first = numbers[0]
    for num in range(1, len(numbers)):
        if numbers[num] >= first:
            continue
        else:
            first = numbers[num]
    return first
    
def find_max(numbers):
    first = numbers[0]
    for n in range(1, len(numbers)):
        if numbers[n] <= first:
            continue
        else:
            first = numbers[n]
    return first

def search(numbers, user_num):
    success = False
    for i in range(len(numbers)):
        if user_num == numbers[i]:
            index_val = i
            success = True
            break
        else:
            continue
    if success:
        return index_val
    else:
        return -1
    
def bubble_sort(numbers):
    num_list = numbers.copy()
    for x in range(len(num_list)):
        smallest_num = x
        for y in range(x+1, len(num_list)):
            if num_list[y] < num_list[smallest_num]:
                smallest_num = y
        num_list[x], num_list[smallest_num] = num_list[smallest_num], num_list[x]
    return num_list
    
def show_menu():
    print("""
        === Number Cruncher ===
        1. Find minimum
        2. Find maximum
        3. Search for a number
        4. Sort the list
        5. Quit
            """)
    option = input("Choose an option (1-5)")
    
    return option

def main():
    trigger = True
    while trigger:
        menu_entry = show_menu()
        if menu_entry == "5":
            trigger = False
            print(f"Thanks!")
        else:
            if menu_entry == "1":
                print(find_min(numbers))
            elif menu_entry == "2":
                print(find_max(numbers))
            elif menu_entry == "3":
                entry = int(input("Enter an integer: "))
                output = search(numbers, entry)
                if output < 0:
                    print(f"Not found")
                else:
                    print(f"Found at index {output}")
            elif menu_entry == "4":
                print(bubble_sort(numbers))

main()
