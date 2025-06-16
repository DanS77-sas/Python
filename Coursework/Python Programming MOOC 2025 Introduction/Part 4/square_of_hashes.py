def line(integer, string):
    if len(string) == 0:
        print(integer * "*")
    else:
        print(string[0] * integer)

def square_of_hashes(size):
    counter = size
    while counter > 0:
        line(size, "#")
        counter -= 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
