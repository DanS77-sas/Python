def line(integer, string):
    if len(string) == 0:
        print(integer * "*")
    else:
        print(string[0] * integer)

def square(size, character):
    counter = 1
    while counter <= size:
        line(size, character)
        counter += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")