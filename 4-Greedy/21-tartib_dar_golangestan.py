# https://quera.org/problemset/244101
# https://quera.org/college/21026/chapter/81524/lesson/279304/?comments_page=1&comments_filter=ALL

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    total_padding = 0

    reps = [0] * 4
    for i in s: reps[i-1] += 1

    # '4's , '1's: no padding space (good boys)
    # '2's: '2' pairs together
    reps[1] %= 2
    # '3's
    if reps[0] >= reps[2]:
        reps[0] -= reps[2]
    else:
        # '1's cover the '3's padding space
        total_padding += reps[2] - reps[0]
        reps[0] = 0
        # last block doesn't make padding so if there is no unpaired '2' the last '3' doesn't count
        if reps[1] == 0:
            total_padding -= 1

    print(total_padding)