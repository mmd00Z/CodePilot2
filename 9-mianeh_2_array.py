A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = sorted(A + B)
t, n, m = len(l), len(A), len(B)

print(l[t//2] if (n + m) % 2 == 1 else (l[t//2] + l[t//2 - 1]) / 2)