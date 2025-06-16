temperature = int(input("Please type in a temperature(F): "))
calculation = (temperature - 32) * 5 / 9

print(f"{temperature} degrees Fahrenheit equals {calculation} degrees Celsius")
if calculation < 0:
    print("Brr! It's cold in here!")