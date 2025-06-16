def line(integer, string):
    if len(string) == 0:
        print(integer * "*")
    else:
        print(string[0] * integer)

def shape(width, char, height, char2):
    counter = 1
    while counter <= width:
        line(counter, char)
        counter += 1
    
    counter = 1
    while counter <= height:
        line(width, char2)
        counter += 1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")