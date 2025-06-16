number = int(input("Please type in a number: "))

for i in range(2, number + 1, 2):
    print(i)
    print(i - 1)
    
if number % 2 != 0:
    print(number)