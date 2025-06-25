# https://quera.org/college/21026/chapter/81522/lesson/283082/?comments_page=1&comments_filter=ALL

n = int(input())
l = list(map(int, input().split()))
k = int(input())

print(sorted(l, reverse=True)[k-1])