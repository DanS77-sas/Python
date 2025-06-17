# Write your solution here
def no_vowels(word):
    new_word = ""
    alphabet = ["a", "e", "i", "o", "u"]
    for x in word:
        if x in alphabet:
            continue
        new_word += x
    return  new_word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))