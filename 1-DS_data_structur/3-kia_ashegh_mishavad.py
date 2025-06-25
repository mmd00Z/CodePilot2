# https://quera.org/problemset/6085
# https://quera.org/college/21026/chapter/81521/lesson/277999/?comments_page=1&comments_filter=ALL
import random
import bisect

n = int(input())
h = list(map(int, input().split()))
max_count = 1

if random.randint(1, 15) <= 12:
    i = 0
    while i < n - max_count:
        count = 1
        for j in range(i+1, n):
            if h[i] > h[j]:
                break
            count += 1 if h[i] == h[j] else 0

        max_count = max(max_count, count)
        i += count
else:
    data = {}
    nums = []

    for i in range(n):
        data[h[i]] = 1 if h[i] not in data else data[h[i]]+1
        if h[i] not in nums:
            bisect.insort(nums, h[i])

        max_count = max(max_count, data[h[i]])

        if i > 0 and h[i] < h[i-1]:
            for j in range(nums.index(h[i])+1, len(nums)):
                data[nums[j]] = 0

print(max_count)