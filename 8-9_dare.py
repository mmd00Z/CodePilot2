# https://quera.org/college/21026/chapter/81522/lesson/277580/?comments_page=1&comments_filter=ALL&submissions_page=1


def mod_exp(base, exp, mod):
    if exp == 0: return 1
    
    base %= mod
    a = 1
    while exp > 1:
        if exp % 2 == 1:
            a *= base
            a %= mod
        base = (base ** 2) % mod
        exp //= 2

    return (base * a) % mod

def cacl_comb(x):
    return (8 * mod_exp(9, x - 1, 1000000007)) % 1000000007

t = int(input())

for i in range(t):
    x = int(input())
    print(cacl_comb(x))


# # GPT genereted
# def mod_exp(base, exp, mod):
#     result = 1
#     base = base % mod
#     while exp > 0:  # مقایسه با 
#         if (exp % 2) == 1:  # اگر exp فرد است
#             result = (result * base) % mod
#         exp = exp >> 1  # تقسیم exp بر 2
#         base = (base * base) % mod
#     return result



# demo (not optimazed)
# def cacl_comb(x):
#     return (8 * (9**(x-1))) % 1000000007

# t = int(input())

# for i in range(t):
#     x = int(input())

# print(cacl_comb(x))