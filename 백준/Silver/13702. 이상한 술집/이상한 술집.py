import sys
#sys.stdin.readline().rstrip().split()

def calculateResult(list, val):
    if val == 0:
        return 0
    sum = 0
    for i in list:
        sum += i // val
    return sum

N, K = map(int, sys.stdin.readline().rstrip().split())
if K == 0:
    print(0)
else:
    kettles = [0] * N
    for i in range(N):
        kettles[i] = int(input())
    sortedKettles = sorted(kettles)
    l = 1
    r = sortedKettles[-1]
    max = 0
    while l <= r:
        m = (l + r) // 2
        result = calculateResult(kettles, m)
        if result >= K:
            max = m
            l = m + 1
        else:
            r = m - 1
    print(max)