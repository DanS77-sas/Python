# Write your solution here
def even_numbers(numbers : list):
    new_list = [x for x in numbers if x % 2 == 0]
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)