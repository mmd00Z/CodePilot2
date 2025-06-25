# https://quera.org/problemset/1362
# https://quera.org/college/21026/chapter/81523/lesson/284575/?comments_page=1&comments_filter=ALL

n = int(input())
s = input()
dp = [0] * n

# base: set dp[0],dp[1],dp[2]
dp[0] = 1 if s[0] == 'B' else 0
dp[1] = dp[0] if s[1] == '.' or s[1] == 'K' else 0
if 2 < n:
    dp[2] = dp[0]+dp[1] if s[2] == '.' or s[2] == 'K' else 0

for i in range(3, n):
    if s[i] == '.' or s[i] == 'K':
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(dp[n-1])