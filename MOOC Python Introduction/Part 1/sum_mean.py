numbers = []
for i in range(1, 5):
    num = int(input(f"Number {i}: "))
    numbers.append(num)

total = sum(numbers)
mean = total / len(numbers)
print(f"The sum of the numbers is {total} and the mean is {mean}")