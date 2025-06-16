def squared(word, times):
    counter = 0

    for row in range(times):
        for col in range(times):
            print(word[counter % len(word)], end="")
            counter += 1 
        print()


# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
