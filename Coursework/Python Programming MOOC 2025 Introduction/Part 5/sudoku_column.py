# Write your solution here
def column_correct(sudoku : list, column_no : int):
    seen = set()
    counter = 0

    for x in sudoku:
        number = sudoku[counter][column_no]
        if number != 0:
            if number in seen:
                return False
        
            seen.add(number)
        counter += 1 

    return True

if __name__ == "__main__":
    print(column_correct(sudoku, 4))
