# Write your solution here
items = int(input("How many items: "))
list = []
for i in range(1, items + 1):
    add_list = int(input(f"Item {i}: "))
    list.append(add_list)

print(list)