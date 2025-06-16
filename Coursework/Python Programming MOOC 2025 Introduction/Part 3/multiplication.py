number = int(input("Please type in a number: "))
for i in range(1, number + 1):
    for x in range(1, number + 1):
        print(f"{i} x {x} = {i * x}")