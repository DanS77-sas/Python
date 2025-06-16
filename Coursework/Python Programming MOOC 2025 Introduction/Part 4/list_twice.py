# Write your solution here
numbers = []

while True:
    item = int(input("New item: "))

    if item == 0:
        print("Bye!")
        break
    
    numbers.append(item)
    list_sort = sorted(numbers)


    print(f"The list now: {numbers}")
    print(f"The list in order: {list_sort}")
    