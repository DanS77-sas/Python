# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = set()

    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            value = sudoku[row][col]
            if value != 0:
                if value in seen:
                    return False
                seen.add(value)
    
    return True

if __name__ == "__main__":
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))