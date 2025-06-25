# https://quera.org/problemset/144080?tab=description
# https://quera.org/college/21026/chapter/81524/lesson/279303/?comments_page=1&comments_filter=ALL

n, m = map(int, input().split())
l = list(map(int, input().split()))

company = [0] * m
max_rep = 0

for i in l:
    company[i-1] += 1
    max_rep = max(max_rep, company[i-1])

# if n - max_rep < max_rep: NO
print("NO" if n / 2 < max_rep else "YES")