correct_pin = 4321
attempts = 0

while True:
    pin = int(input("PIN: "))
    attempts += 1

    if pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")

