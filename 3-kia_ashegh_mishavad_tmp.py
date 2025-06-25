# https://quera.org/problemset/6085
# https://quera.org/college/21026/chapter/81521/lesson/277999/?comments_page=1&comments_filter=ALL

n = int(input())
h = list(map(int, input().split()))

max_count = 1
max_rn = 0

# nnn = 100000
# data = [0] * nnn
# zero = [0] * nnn

# for i in range(n):
#     data[h[i]] += 1
#     max_count = max(max_count, data[h[i]])
#     max_rn = max(max_rn, h[i])
#     # review
#     if h[i] < h[i-1]:
#         data[h[i]+1:] = zero[h[i]+1:]

# print(max_count)


# i = 0
# while i < n - max_count:
#     count = 1
#     for j in range(i+1, n):
#         if h[i] > h[j]:
#             break
#         count += 1 if h[i] == h[j] else 0

#     max_count = max(max_count, count)
#     i += count


# new_step = 0
# for i in range(n):
#     if i < new_step: continue
#     if n - i < max_count: break

#     count = 1
#     for j in range(i+1, n):
#         if h[i] > h[j]:
#             break
#         count += 1 if h[i] == h[j] else 0

#     max_count = max(max_count, count)
#     new_step = i + count

# nnn = 100000
# data = [0] * nnn
# zero = [0] * nnn
# last_min_wall = h[0]

# for i in h:
#     data[i] += 1
#     max_count = max(max_count, data[i])
#     max_rn = max(max_rn, i)

#     data[i+1:] = zero[i+1:]



# import bisect

# n = int(input())
# h = list(map(int, input().split()))

# max_count = 1

# data = {}
# nums = []

# for i in range(n):
#     data[h[i]] = 1 if h[i] not in data else data[h[i]]+1
#     if h[i] not in nums:
#         bisect.insort(nums, h[i])

#     max_count = max(max_count, data[h[i]])

#     if i > 0 and h[i] < h[i-1]:
#         for j in range(nums.index(h[i])+1, len(nums)):
#             data[nums[j]] = 0

# print(max_count)