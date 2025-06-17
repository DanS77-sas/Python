# Write your solution here
def everything_reversed(words : list):
    new_list = [word[::-1] for word in words]
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)