import sys
#sys.stdin.readline().rstrip().split()

N = int(input())
l = 0
r = N
min = 0
while l <= r:
    m = (l + r) // 2
    if m*m >= N:
        min = m
        r = m - 1
    else:
        l = m + 1

print(min)