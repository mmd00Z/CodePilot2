# https://quera.org/problemset/252334

c = int(input())

for _ in range(c):
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    g = list(map(int, input().split()))

    ans = [0] * w

    for val in a:
        i = 0
        while i < w and val >= g[i]:
            cnt = val // g[i]
            ans[i] += cnt * g[i]
            val %= g[i]
            i += 1

    print(*ans)


# c = int(input())

# for _ in range(c):
#     n, w = map(int, input().split())
#     a = list(map(int, input().split()))
#     g = list(map(int, input().split()))
    
#     for x in g:
#         out = 0
#         for i in range(n):
#             out += a[i] - a[i] % x if a[i] >= x else 0
#             a[i] %= x
#         print(out, end=' ')
#     print()
