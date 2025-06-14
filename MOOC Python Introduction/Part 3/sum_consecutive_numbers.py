number = int(input("Limit: "))
sum = 0
counter = 1
calculation = "The consecutive sum: "

while sum < number:
    sum += counter
    calculation += f"{counter}"
    counter += 1
    if sum < number:
        calculation += " + "

calculation  += f"= {sum}"

print(calculation)