# given row and col find number from pascal triangle

def findNumber(row, col):
    if (col == 1 or col == row): return 1
    return findNumber(row-1, col-1) + findNumber(row-1, col)


print(findNumber(5, 3))
