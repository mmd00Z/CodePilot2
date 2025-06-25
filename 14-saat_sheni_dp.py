# https://quera.org/problemset/228671
# https://quera.org/college/21026/chapter/81523/lesson/280784/?comments_page=1&comments_filter=ALL

def chek_ways(n, m, T, t):
    # 
    dp = []
    
    

q = int(input())

for _ in range(q):
    n, m, T = map(int, input().split())
    t = [0] + list(map(int, input().split())) + [T]
    
    print("YES" if chek_ways(n, m, T, t) else "NO")
