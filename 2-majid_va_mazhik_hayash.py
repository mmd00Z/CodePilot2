# https://quera.org/college/21026/chapter/81521/lesson/277997/?comments_page=1&comments_filter=ALL

n = int(input())

# markers
m = list(map(int, input().split()))

# markers' data
# key:value => color:count
m_d = {}

# update markers' data
for i in range(len(m)):
    m_d[m[i]] = 1 if m[i] not in m_d else m_d[m[i]] + 1

# find the min color
min_count = float('inf')
min_color = 0
for color, count in m_d.items():
    if count < min_count:
        min_count = count
        min_color = color
    elif count == min_count:
        min_color = min(min_color, color)

print(min_color)