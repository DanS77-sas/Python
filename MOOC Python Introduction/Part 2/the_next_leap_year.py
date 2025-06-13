year = int(input("Year: "))

next_year = year + 1

while True:
    #Checks if year is dvisible by 400 or 4 but NOT by 100.
    if next_year % 400 == 0 or (next_year % 4 == 0 and next_year % 100 != 0):
        print(f"The next leap year after {year} is {next_year}")
        break
    next_year += 1