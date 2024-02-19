import sys


M, N = map(int, sys.stdin.readline().rstrip().split())
cracker_length = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_cracker = sorted(cracker_length)

def counter(val):
    cnt = 0
    for i in sorted_cracker:
        cnt += i // val
        if cnt >= M:
            return True
    return False

l = 1
r = sorted_cracker[-1]
max = -1
while l <= r:
    m = (l + r) // 2
    result = counter(m)
    if result:
        if m > max:
            max = m
        l = m + 1
    else:
        r = m - 1

if max == -1:
    print(0)
else:
    print(max)