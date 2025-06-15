factorial = 1

while True:
    n = int(input("Please type in a number: "))
    if n <= 0:
        print("Thanks and bye!")
        break
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"The factorial of the number {n} is {factorial}")

    factorial = 1 #reset factorial value