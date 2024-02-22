import sys
#sys.stdin.readline().rstrip().split()

N = int(input())
l = 1
r = N
min = 0
while l <= r:
    m = (l + r) // 2
    if m*m == N:
        print(m)
        break
    elif m*m > N:
        r = m - 1
    else:
        l = m + 1