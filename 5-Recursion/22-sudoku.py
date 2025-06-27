# https://quera.org/problemset/9743
# https://quera.org/college/21026/chapter/81525/lesson/281923/?comments_page=1&comments_filter=ALL

def get_empty(table):
    empty = []
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                empty.append((i, j))
    return empty


def get_options(ii, jj, table):
    opts = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if table[i][jj] in opts:
            opts.remove(table[i][jj])

    for j in range(9):
        if table[ii][j] in opts:
            opts.remove(table[ii][j])    
    row_box = ii // 3
    column_box = jj // 3

    for i in range(row_box * 3, row_box * 3 + 3):
        for j in range(column_box * 3, column_box * 3 + 3):
            if table[i][j] in opts:
                opts.remove(table[i][j])
    return opts


def solve_sudoku(table, empty, counter):
    if counter >= len(empty):
        return table
    
    i, j = empty[counter]
    opts = get_options(i, j, table)

    if len(opts) == 0:
        return False
    
    for o in opts:
        table[i][j] = o
        ans = solve_sudoku(table.copy(), empty, counter+1)
        if ans != False:
            return ans
        table[i][j] = 0
    
    return False


table = [list(map(int, input().split())) for _ in range(9)]

table = solve_sudoku(table.copy(), get_empty(table), 0)

if table:
    for r in table:
        print(*r, sep=' ')
else:
    print("No solution exists")



# UNASSIGNED = 0
# N = 9

# def find_unassigned_location(grid):
#     for row in range(N):
#         for col in range(N):
#             if grid[row][col] == UNASSIGNED:
#                 return row, col
#     return None

# def used_in_row(grid, row, num):
#     return num in grid[row]

# def used_in_col(grid, col, num):
#     return any(grid[row][col] == num for row in range(N))

# def used_in_box(grid, box_start_row, box_start_col, num):
#     for row in range(3):
#         for col in range(3):
#             if grid[box_start_row + row][box_start_col + col] == num:
#                 return True
#     return False

# def is_safe(grid, row, col, num):
#     return (not used_in_row(grid, row, num) and
#             not used_in_col(grid, col, num) and
#             not used_in_box(grid, row - row % 3, col - col % 3, num) and
#             grid[row][col] == UNASSIGNED)

# def solve_sudoku(grid):
#     location = find_unassigned_location(grid)
#     if not location:
#         return True
#     row, col = location

#     for num in range(1, 10):
#         if is_safe(grid, row, col, num):
#             grid[row][col] = num
#             if solve_sudoku(grid):
#                 return True
#             grid[row][col] = UNASSIGNED

#     return False

# def print_grid(grid):
#     for row in grid:
#         print(" ".join(str(num) for num in row))

# grid = []
# for _ in range(9):
#     row = list(map(int, input().split()))
#     grid.append(row)

# if solve_sudoku(grid):
#     print_grid(grid)
# else:
#     print("No solution exists")
