import sys

N = int(input())
budget_requests = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())

budget_requests = sorted(budget_requests)
max = -1
l = 1
r = budget_requests[-1]
while l <= r:
    m = (l + r) // 2
    sum = 0
    for i in budget_requests:
        if i < m:
            sum += i
        else:
            sum += m

    if sum <= M and m > max:
        max = m
        l = m + 1
    else:
        r = m - 1

print(max)