frequency = float(input("How many times a week do you eat lunch at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
weekly_shopping = float(input("How much money do you spend on groceries in a week? "))

total_weekly = weekly_shopping + (price * frequency)
daily_average = total_weekly / 7

print("\nAverage food expenditure:")
print(f"Daily: {daily_average:.2f} euros")
print(f"Weekly: {total_weekly:.2f} euros")
