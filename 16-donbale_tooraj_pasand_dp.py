# https://quera.org/problemset/15126
# https://quera.org/college/21026/chapter/81523/lesson/280788/?comments_page=1&comments_filter=ALL

k, d = map(int, input().split())

dp = [0] * k

dp[0] = d + 1

for i in range(1, k):
    dp[i] = 


def total_ways(k, d, val_i = 0, counter = 1):
    ways = 0
    start = 0 if val_i - d < 0 else val_i - d
    end = val_i + d

    if counter >= k:
        return end - start + 1
    
    for i in range(start, end+1):
        ways += total_ways(k, d, i, counter+1)

    return ways

print(total_ways(k, d))