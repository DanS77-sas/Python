sentence = ""
previous_word = None

while True:
    word = input("Please type in a word: ")
    
    if word == "end" or word == previous_word:
        break
    
    sentence += word + " "
    previous_word = word

print(sentence)