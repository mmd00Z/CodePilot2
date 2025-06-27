# https://quera.org/college/21026/chapter/81525/lesson/281927/?comments_page=1&comments_filter=ALL

def create_table(lbp, old, n, k, count):
    if count >= k:
        return old
    
    nn = len(old[0])
    grid = [['.' for _ in range(nn*n)] for _ in range(nn*n)]

    for i in range(nn):
        for j in range(nn):
            start_i, start_j = i * n, j * n
            if old[i][j] == '.':
                for ii, jj in lbp:
                    grid[start_i+ii][start_j+jj] = '*'
            elif old[i][j] == '*':
                for ii in range(n):
                    for jj in range(n):
                        grid[start_i+ii][start_j+jj] = '*'

    return create_table(lbp, grid, n, k, count+1)
    

n, k = map(int, input().split())
pattern = [input() for _ in range(n)]

local_black_pos = []
for i in range(n):
    for j in range(n):
        if pattern[i][j] == '*':
            local_black_pos.append((i, j))

table = create_table(local_black_pos, pattern, n, k, 1)

for row in table:
    print(*row, sep='')
