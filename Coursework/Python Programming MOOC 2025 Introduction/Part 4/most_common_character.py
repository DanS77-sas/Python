# Write your solution here
def most_common_character(word):
    common = word[0]
    for i in word:
        if word.count(i) > word.count(common):
            common = i
    return common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))