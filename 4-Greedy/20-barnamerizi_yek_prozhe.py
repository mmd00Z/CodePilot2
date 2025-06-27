# https://quera.org/problemset/235088
# https://quera.org/college/21026/chapter/81524/lesson/279318/?comments_page=1&comments_filter=ALL

n = int(input())
l, r = map(int, input().split())

# goal: min(k); k * l <= n <= k * r
# n / r <= k <= n / l
#  min(k) = n // r + 1      (k <= n / l)
if n % r == 0:
    print(n // r)
elif l == r:
    print(-1)
else:
    k = n // r + 1
    print(k if k < n / l else -1)


# # Correct but not optimized code
# for i in range(1 , n // l + 1):
#     if l * i <= n <= r * i:
#         print(i)
#         exit()
# print(-1)


# # WRONG ANSWER
# min_days = 0
# flag = False
# for _ in range(r - l + 1):
#     min_days += n // r
#     overflow = n % r

#     if overflow == 0:
#         flag = True
#         break
#     elif l <= overflow <= r:
#         min_days += 1
#         flag = True
#         break
#     elif overflow < l:
#         n = overflow + r
#         r -= 1
#         min_days -= 1

# print(min_days if flag else -1)


# # WRONG ANSWER
# def get_min_count(n, l, r):
#     out = 0
#     for _ in range(r - l + 1):
#         out += n // r
#         overflow = n % r
#         if overflow == 0:
#             return out
#         elif l <= overflow:
#             return out + 1
#         elif overflow < l:
#             if r - 1 < l:
#                 return -1
#             out -= 1
#             n = overflow + r
#             r -= 1

# print(get_min_count(n, l, r))