# Write your solution here
year = int(input("Year: "))

if year % 400 == 0 or year % 4 == 0 and (year + 4) % 100 != 0:
    print(f"The next leap year after {year} is {year + 4}")
else:
    if ((year + 1) % 400 == 0) or ((year + 1) % 4 == 0 and (year + 1) % 100 != 0):
        print(f"The next leap year after {year} is {year + 1}")
    elif ((year + 2) % 400 == 0) or ((year + 2) % 4 == 0 and (year + 2) % 100 != 0):
        print(f"The next leap year after {year} is {year + 2}")
    elif ((year + 3) % 400 == 0) or ((year + 3) % 4 == 0 and (year + 3) % 100 != 0):
        print(f"The next leap year after {year} is {year + 3}")
    else:
        for i in range(1, 9):
            if ((year + i) % 400 == 0) or ((year + i) % 4 == 0 and (year + i) % 100 != 0):
                print(f"The next leap year after {year} is {year + i}")