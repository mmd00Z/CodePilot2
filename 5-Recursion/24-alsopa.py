# https://quera.org/college/21026/chapter/81525/lesson/281925/?comments_page=1&comments_filter=ALL

def get_ways(current_sum, i, i_max, n, x, memo={}):
    if current_sum == x:
        return 1
    elif current_sum > x or i > i_max:
        return 0
    else:
        return get_ways(current_sum + (i + 1) ** n, i+1, i_max, n, x) + get_ways(current_sum, i+1, i_max, n, x)
    

x = int(input())
n = int(input())

print(get_ways(0, 0, x ** (1/n), n, x))