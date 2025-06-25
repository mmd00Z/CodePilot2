def solve():
    import bisect
    input_data = input().split()

    n = int(input_data[0])
    a = list(map(int, input().split()))
    
    # محاسبه آرایه‌های L و R با استفاده از استک (برای next smaller element)
    L = [-1] * n
    R = [n] * n
    stack = []
    for i in range(n):
        # پیدا کردن اولین شاخص به چپ که مقدارش کمتر از a[i] باشد
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        L[i] = stack[-1] if stack else -1
        stack.append(i)
    
    stack = []
    for i in range(n-1, -1, -1):
        # پیدا کردن اولین شاخص به راست که مقدارش کمتر از a[i] باشد
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        R[i] = stack[-1] if stack else n
        stack.append(i)
    
    # ساخت دیکشنری برای نگهداری لیست اندیس‌ها برای هر ارتفاع
    pos = {}
    for i, val in enumerate(a):
        if val not in pos:
            pos[val] = []
        pos[val].append(i)
    
    ans = 0
    # برای هر اندیس i، تعداد occurrence های a[i] در بازه‌ی [L[i]+1, R[i]-1] را بیابیم.
    for i in range(n):
        X = a[i]
        left_bound = L[i] + 1
        right_bound = R[i] - 1
        # لیست اندیس‌های مربوط به X
        lst = pos[X]
        # پیدا کردن اولین اندیسی که >= left_bound است
        lo = bisect.bisect_left(lst, left_bound)
        # پیدا کردن اولین اندیسی که > right_bound است
        hi = bisect.bisect_right(lst, right_bound)
        candidate = hi - lo
        if candidate > ans:
            ans = candidate
    
    print(ans)
    
if __name__ == '__main__':
    solve()
