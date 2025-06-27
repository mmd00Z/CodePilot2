# https://quera.org/problemset/603
# https://quera.org/college/21026/chapter/81525/lesson/281924/?comments_page=1&comments_filter=ALL

def get_ways(loc, n, memo = {}):
    if loc == n:
        return 1
    elif loc > n:
        return 0
    else:
        if loc in memo:
            return memo[loc]
        memo[loc] = get_ways(loc+1, n) + get_ways(loc+2, n) + get_ways(loc+5, n)
        return memo[loc]

print(get_ways(0, int(input())))


# def f(n):
#     if n == 0:
#         return 1
#     if n < 2:
#         return f(n - 1)
#     elif n < 5:
#         return f(n - 1) + f(n - 2)
#     else:
#         return f(n - 1) + f(n - 2) + f(n - 5)

# n = int(input())
# print(f(n))


# n = int(input())
# dp = [0] * (n+1)
# dp[0] = 1

# for i in range(1, n+1):
#     dp[i] += dp[i-1] if i-1 >= 0 else 0
#     dp[i] += dp[i-2] if i-2 >= 0 else 0
#     dp[i] += dp[i-5] if i-5 >= 0 else 0

# print(dp[n])
