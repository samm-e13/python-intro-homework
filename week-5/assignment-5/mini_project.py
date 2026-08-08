numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

trigger = True
while trigger:

    print("""
    === Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit
        """)
    option = int(input("Choose an option (1-5)"))

    if option == 5:
        trigger = False
        print(f"Thanks!")
    else:

        if option == 1:
            first = numbers[0]
            for num in range(1, len(numbers)):
                if numbers[num] >= first:
                    continue
                else:
                    first = numbers[num]
            print(f"{first}")

        elif option == 2:
            first = numbers[0]
            for n in range(1, len(numbers)):
                if numbers[n] <= first:
                    continue
                else:
                    first = numbers[n]
            print(f"{first}")

        elif option == 3:
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
                print(f"{index_val}")
            else:
                print(f"not found")
    
        elif option == 4:
            for x in range(len(numbers)):
                smallest_num = x
                for y in range(x+1, len(numbers)):
                    if numbers[y] < numbers[smallest_num]:
                        smallest_num = y
                numbers[x], numbers[smallest_num] = numbers[smallest_num], numbers[x]
            print(f"{numbers}")






