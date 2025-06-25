# https://quera.org/problemset/281768
# https://quera.org/college/21026/chapter/81521/lesson/283969/?comments_page=1&comments_filter=ALL

n, q = map(int, input().split())
a = list(map(int, input().split()))

maxs = [0] * (n+1)
progresses = [0] * n

for i in range(n):
    maxs[i+1] = max(maxs[i], a[i])
    progresses[i] = max(0, a[i] - maxs[i])


for i in range(q):
    cmd, in1, in2 = map(int, input().split())
    in1 -= 1

    if cmd == 2:
        print(sum(progresses[in1:in2]))
        
    elif cmd == 1:
        a[in1] = in2

        if maxs[in1 + 1] != max(maxs[in1], in2):
            for j in range(in1, n):
                maxs[j+1] = max(maxs[j], a[j])
                progresses[j] = max(0, a[j] - maxs[j])


# for i in range(q):
#     cmd, in1, in2 = map(int, input().split())
#     in1 -= 1

#     if cmd == 2:
#         progress = 0
#         max_a = 0
#         for j in range(in2):
#             if j >= in1:
#                 progress += max(0, a[j] - max_a)
#             max_a = max(max_a, a[j])
#         print(progress)
#     elif cmd == 1:
#         a[in1] = in2