#!/usr/bin/env python3

# completing holesum project in python
    # TODO
    # FILE IO
    # Data Structure selection: 2D array

# CL Arg python3 ./holesum.py ./test/test4

from sys import argv

def main():
    args = argv[1:]
    
    if 1 != len(args):
        print('usage: <filename> ')
        return 1
    
    matrix = []
    
    file = open(args[0], "r")
    
    for line in file:
        row = []
        for letter in line:
            #print(letter, end='')
            if '1' == letter or '0' == letter:
                row.append(letter)
        matrix.append(row)
    
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            print(matrix[i][j], end="")    
        print()
    print()
    num_holes = 0
    largets_hole = 0
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            hole_size = dfs(matrix, len(matrix), len(row), i, j)    
            if (hole_size != 0):
                num_holes += 1
                if largets_hole < hole_size:
                    largets_hole = hole_size   
    
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            print(matrix[i][j], end="")    
        print()
    print()
    
    print(f"number of holes = {num_holes}")
    print(f"largest hole = {largets_hole}")
    
    
def dfs(matrix, rows, cols, idx_row, idx_col) -> int:
    if (idx_row < 0 or idx_col < 0):
        return 0
    if (rows <= idx_row or cols <= idx_col):
        return 0
    if ("1" == matrix[idx_row][idx_col]):
        return 0

    count = 1
    matrix[idx_row][idx_col] = '1'
    
    count += dfs(matrix, rows, cols, idx_row + 1, idx_col)
    count += dfs(matrix, rows, cols, idx_row - 1, idx_col)
    count += dfs(matrix, rows, cols, idx_row, idx_col + 1)
    count += dfs(matrix, rows, cols, idx_row, idx_col - 1)
    
    return count
        
if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print_exc()
