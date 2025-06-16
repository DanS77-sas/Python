# Write your solution here
numbers = []
print(f"The list is now {numbers}")
counter = 1
while True:
    action = input("a(d)d, (r)emove or e(x)it: ")
    
    if action == "d":
        numbers.append(counter)
        counter += 1 

    elif action == "r":
        numbers.pop()
        counter -= 1

    else:
        print("Bye!")
        break

    print(f"The list is now {numbers}")
    