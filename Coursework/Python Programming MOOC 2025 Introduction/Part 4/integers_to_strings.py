# Write your solution here
def formatted(numbers : list):
    new_list = [f"{number:.2f}" for number in numbers]
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)