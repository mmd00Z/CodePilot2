# https://quera.org/college/21026/chapter/81521/lesson/277996/?comments_page=1&comments_filter=ALL

inp = input()

max_0 = 0
start = -1
end = -1

for i in range(len(inp)):
    if inp[i] == '0':
        if start < 0:
            start = i
        end = i
        max_0 = max(end - start + 1, max_0)
    else:
        start = -1

print(max_0)