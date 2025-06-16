def chessboard(n):
    for row in range(n):       
        for col in range(n):
            if (row + col) % 2 == 0:
                print("1", end="")
            else:
                print("0",end="") 
        print()                

# Testing the function
if __name__ == "__main__":
    chessboard(3)
