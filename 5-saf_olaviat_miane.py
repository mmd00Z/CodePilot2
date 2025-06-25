import bisect

k = int(input()) - 1
l = list(map(int, input().strip().replace(' ', '')[6:-1].split(',')))
l.sort()

def insert(lst, num):
    bisect.insort(lst, num)

def remove(lst):
    if int((len(lst)-1)//2) >= 0:
        return lst.pop(int((len(lst)-0.1)//2))
    return ""

for i in range(k):
    cmd = input().strip().replace(' ', '')
    if cmd == "remove":
        print(remove(l))
    elif cmd[:6] == "insert":
        num = int(cmd[7:-1])
        insert(l, num)
    elif cmd[:5] == "build":
        l = list(map(int, cmd.strip().replace(' ', '')[6:-1].split(',')))
        l.sort()
