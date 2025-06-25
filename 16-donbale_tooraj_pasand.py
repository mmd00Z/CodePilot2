# https://quera.org/problemset/15126
# https://quera.org/college/21026/chapter/81523/lesson/280788/?comments_page=1&comments_filter=ALL

def total_ways(k, d, val_i=0, counter=1, memo={}):
    ways = 0
    start = max(0, val_i - d)
    end = val_i + d

    if counter >= k:
        return end - start + 1


    if (counter, val_i) in memo:
        return memo[(counter, val_i)]
    
    for i in range(start, end + 1):
        ways += total_ways(k, d, i, counter + 1, memo)

    memo[(counter, val_i)] = ways
    return ways

k, d = map(int, input().split())
print(total_ways(k, d) % 1000000007)


# def total_ways(k, d, val_i = 0, counter = 1):
#     ways = 0
#     start = 0 if val_i - d < 0 else val_i - d
#     end = val_i + d

#     if counter >= k:
#         return end - start + 1

#     for i in range(start, end+1):
#         ways += total_ways(k, d, i, counter+1)

#     return ways

# k, d = map(int, input().split())

# print(total_ways(k, d) % 1000000007)