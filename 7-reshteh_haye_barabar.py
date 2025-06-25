s1, s2 = input(), input()

def is_equal(s1, s2):
    if s1 == s2:
        return True

    n = len(s1)
    if n % 2 == 1:
        return s1 == s2
    
    return (is_equal(s1[n//2:], s2[n//2:]) and is_equal(s1[:n//2], s2[:n//2])) or (is_equal(s1[n//2:], s2[:n//2]) and is_equal(s1[:n//2], s2[n//2:]))


print("YES" if is_equal(s1, s2) else "NO")