numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    first = numbers[0]
    for num in range(1, len(numbers)):
        if numbers[num] >= first:
            continue
        else:
            first = numbers[num]
    print(f"{first}")
    
def find_max(numbers):
    first = numbers[0]
    for n in range(1, len(numbers)):
        if numbers[n] <= first:
            continue
        else:
            first = numbers[n]
    print(f"{first}")

def search(numbers):
    user_num = int(input("Enter an integer: "))
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
    
def bubble_sort():
    number_list = numbers.copy()
    for x in range(len(number_list)):
        smallest_num = x
        for y in range(x+1, len(number_list)):
            if number_list[y] < number_list[smallest_num]:
                smallest_num = y
        number_list[x], number_list[smallest_num] = number_list[smallest_num], number_list[x]
    return number_list
    
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
        input = show_menu()
        if input == "5":
            trigger = False
            print(f"Thanks!")
        else:
            if input == "1":
                find_min(numbers)
            elif input == "2":
                find_max(numbers)
            elif input == "3":
                output = search(numbers)
                if output < 0:
                    print(f"Not found")
                else:
                    print(f"Found at index {output}")
            elif input == "4":
                print(bubble_sort())

main()
