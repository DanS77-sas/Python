# Write your solution here
def spruce(size):
    print("a spruce!")
    for row in range(1, size + 1):
        spaces = size - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)
    print(" " * (size - 1) + "*")  




# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)