hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

wages = hourly_wage * hours_worked
if day == "Sunday":
    wages *= 2

print(f"Daily wages: {wages} euros")