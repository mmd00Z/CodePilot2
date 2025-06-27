# https://quera.org/problemset/235328
# https://quera.org/college/21026/chapter/81524/lesson/279302/?comments_page=1&comments_filter=ALL

n, k = map(int, input().split())

# add self to friends ==> cost += 1
costs = sorted(list(map(lambda c : int(c)+1, input().split())))

total_cost = 0
count = 0

for c in costs:
    if total_cost + c > k:
        break
    total_cost += c
    count += 1

print(count)