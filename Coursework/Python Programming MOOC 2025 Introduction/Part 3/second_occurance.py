word = input("Please type in a string: ")
substring = input("Please type in a substring: ")
word_index = word.find(substring)
second_index = word.find(substring, word_index + len(substring))

while True:
    if second_index == -1:
        print("The substring does not occur twice in the string.")
        break
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
        break