# https://quera.org/problemset/211017
# https://quera.org/college/21026/chapter/81523/lesson/280789/?comments_page=1&comments_filter=ALL

n = int(input())
a = list(map(int, input().split()))
q = int(input())

dp = [0] * n

for i in range(1, n-1):
    if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]


for i in range(q):
    l, r = map(lambda x : int(x) - 1, input().split())
    
    print(dp[r-1] - dp[l] + 2 if l != r else 1)

# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())

# for _ in range(q):
#     l, r = map(int, input().split())

#     max_len = 1
#     next_operator = True
#     for i in range(l, r):
#         if next_operator and a[i] > a[i-1]:
#             next_operator = not next_operator
#             max_len += 1
#         elif not next_operator and a[i] < a[i-1]:
#             next_operator = not next_operator
#             max_len += 1

#     print(max_len)