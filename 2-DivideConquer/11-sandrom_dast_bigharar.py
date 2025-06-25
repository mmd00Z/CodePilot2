# https://quera.org/college/21026/chapter/81522/lesson/283089/?comments_page=1&comments_filter=ALL

def max_index(arr):
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[idx]:
            idx = i
    return idx

def get_depths(arr, current_depth):
    if len(arr) == 1:
        return [current_depth]
    if len(arr) < 1:
        return []

    i = max_index(arr)
    return get_depths(arr[:i], current_depth+1) + [current_depth] + get_depths(arr[i+1:], current_depth+1)


t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    print(*get_depths(l, 0), sep=' ')