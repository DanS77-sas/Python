from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

cal1 = (-b  + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
cal2 = (-b  - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f"The roots are {cal1} and {cal2}")
