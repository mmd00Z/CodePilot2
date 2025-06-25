# https://quera.org/problemset/228671
# https://quera.org/college/21026/chapter/81523/lesson/280784/?comments_page=1&comments_filter=ALL

def chek_ways(l, i, last_i, n, left_time, m):
    if i >= len(l):
        return True
    
    diff = l[i] - l[last_i]
    new_left_time = left_time - diff if n % 2 == 0 else left_time + diff

    if new_left_time < 0 or new_left_time > m:
        return False

    # pass i , select i: last_i = i, n++ (n select)
    return chek_ways(l, i+1, last_i, n, left_time, m) or chek_ways(l, i+1, i, n+1, new_left_time, m)
    

q = int(input())

for _ in range(q):
    n, m, T = map(int, input().split())
    t = [0] + list(map(int, input().split())) + [T]
    
    print("YES" if chek_ways(t, 1, 0, 0, m, m) else "NO")
