word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)
while True:
    if index == -1:
        break
    else:
        if index + 3 > len(word):
            break
        else:
            print(word[index: index + 3])
            break
