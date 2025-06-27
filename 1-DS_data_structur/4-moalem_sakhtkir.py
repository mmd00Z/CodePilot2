from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

min_cost = float("inf")
costs = [0] * (n-k+1)
wort_case = []
dq = deque()  

for i in range(n):
    window_start = i - k + 1

    while dq and dq[0] < window_start:
        dq.popleft()

    curr_value = a[i] - (i - window_start + 1)

    while dq and (a[dq[-1]] - (dq[-1] - window_start + 1)) <= curr_value:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        max_val = a[dq[0]] - (dq[0] - window_start + 1)
        wort_case.append(max_val)


for i in range(k):
    costs[0] += (i+1) - a[i]

for i in range(1, n-k+1):
    costs[i] = costs[i-1] + a[i-1] - a[i+k-1]


for i in range(n-k+1):
    if costs[i] < min_cost and wort_case[i] <= 0:
        min_cost = costs[i]

print(min_cost if min_cost != float("inf") else -1)



# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# min_cost = float("inf")

# if n * k > 40 * 10**9:
#     costs = [0] * (n-k+1)
#     for i in range(k):
#         costs[0] += (i+1) - a[i]
#     for i in range(1, n-k+1):
#         costs[i] = costs[i-1] + a[i-1] - a[i+k-1]
#     for c in costs:
#         if c < min_cost and c > -1:
#             min_cost = c
# else:
#     for i in range(len(a)-k+1):
#         if a[i] > 1: continue
#         cost = 0
#         for j in range(k):
#             if a[i+j] > j+1:
#                 cost = -1
#                 break
#             cost += j+1 - a[i+j]
#         if cost != -1:
#             min_cost = min(min_cost, cost)

# print(min_cost if min_cost != float("inf") else -1)