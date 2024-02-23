import sys
#sys.stdin.readline().rstrip().split()
def getTotal(list, val):
    sum = 0
    for i in list:
       if val < i:
            sum += i - val
    return sum

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))
sorted_trees = sorted(trees)

l = 0
r = sorted_trees[-1]
max = 0
while l <= r:
    m = (l + r) // 2
    total = getTotal(trees, m)
    if total >= M:
        l = m + 1
        max = m 
    else:
        r = m - 1

print(max)