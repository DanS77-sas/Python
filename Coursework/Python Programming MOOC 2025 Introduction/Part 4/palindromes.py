def palindromes(word):
    return word == word[::-1]

def main():
    while True:
        string = input("Please type in a palindrome: ")
        if palindromes(string):
            print(f"{string} is a plaindrome!")
            break
        print(f"{string} wasn't a palindrome")

main()


