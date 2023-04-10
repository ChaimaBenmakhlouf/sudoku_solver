M = 9


def printResult(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    """ first row of the square """
    startRow = row - row % 3
    """ first col of the square """
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == number:
                return False
    return True


def sudoku(grid, row, col):
    """ recursivity stop condition """
    if (row == M - 1 and col == M):
        return True

    """ go to next line """
    if col == M:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for number in range(1, M + 1):

        if solve(grid, row, col, number):

            grid[row][col] = number

            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


if (sudoku(grid, 0, 0)):
    printResult(grid)
else:
    print("The solution doesn't exist.")
