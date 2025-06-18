# Write your solution here
def row_correct(sudoku : list, row_no  : int):
    seen  = set()

    for number in sudoku[row_no]:
        if number  == 0:
            continue
        if number in seen:
            return False
        seen.add(number)

    return True

if __name__ == "__main__":
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))