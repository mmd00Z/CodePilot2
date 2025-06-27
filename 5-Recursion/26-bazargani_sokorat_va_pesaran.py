# https://quera.org/problemset/9744
# https://quera.org/college/21026/chapter/81525/lesson/281926/?comments_page=1&comments_filter=ALL

import itertools

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')
best_assignment = []

for perm in itertools.permutations(range(n)):
    total_cost = sum(cost[i][perm[i]] for i in range(n))
    if total_cost < min_cost:
        min_cost = total_cost
        best_assignment = list(perm)

for job in best_assignment:
    print(job)


# min_sum = float("inf")
# min_comb = []

# def calc_min_comb(current_sum, e, n, count = 0, used_i = []):
#     global min_sum, min_comb
#     if len(used_i) >= n:
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_comb = used_i
#         print(used_i)
#         return
    
#     for i in range(n):
#         if i not in used_i:
#             calc_min_comb(current_sum + e[i][count], e, n, count+1, used_i + [i])
            

# n = int(input())
# employees = []
# for _ in range(n):
#     employees.append(list(map(int, input().split())))

# calc_min_comb(0, employees, n)

# print(*min_comb, sep='\n')
