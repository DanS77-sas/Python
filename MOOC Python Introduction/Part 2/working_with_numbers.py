print("Please type in integer numbers. Type in 0 to finish.")

count = 0 
sum_num = 0
negative = 0
positive = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break

    count += 1
    sum_num += num
    
    if num > 0:
        positive += 1 
    else:
        negative += 1

print(f"Numbers type in {count}")
print(f"The sum of the numbers is {sum_num}")
print(f"The mean of the numbers is {sum_num / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")