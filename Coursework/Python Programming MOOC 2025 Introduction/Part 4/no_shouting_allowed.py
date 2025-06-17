# Write your solution here
def no_shouting(words : list):
    new_list = [word for word in words if not word.isupper()]
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)