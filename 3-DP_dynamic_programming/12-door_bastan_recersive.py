# https://quera.org/problemset/1362
# https://quera.org/college/21026/chapter/81523/lesson/284575/?comments_page=1&comments_filter=ALL

ways = {}

def get_ways(s, i):
    if i in ways:
        return ways[i]
    if i >= len(s):
        return 0
    if s[i] == '.' or s[i] == 'B':
        ways_i = get_ways(s, i+1) + get_ways(s, i+2) + get_ways(s, i+3)
        ways[i] = ways_i
        return ways_i
    if s[i] == 'T':
        return 0
    if s[i] == 'K':
        return 1
    

n = int(input())
s = input()

print(get_ways(s, 0))