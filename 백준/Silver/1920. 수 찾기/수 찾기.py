import sys

N = int(sys.stdin.readline())
source = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

source = sorted(source)
for i in target:
    flag = False
    l = 0
    r = len(source) - 1
    while l <= r:
        m = (l + r) // 2
        if source[m] == i:
            flag = True
            break
        elif source[m] < i:
            l = m + 1
        else:
            r = m - 1
    if flag:
        print(1)
    else:
        print(0)