import sys
#sys.stdin.readline().rstrip().split()

def getResult(list, val):
    cnt = 0
    for i in list:
        cnt += i // val
    return cnt

K, N = map(int, sys.stdin.readline().rstrip().split())
trees = [0] * K
for i in range(K):
    trees[i] = int(input())
sorted_trees = sorted(trees)

l = 1
r = sorted_trees[-1]
length = 0

while l <= r:
    m = (l + r) // 2
    result = getResult(trees, m)
    if result < N:
        r = m - 1
    else:
        length = m
        l = m + 1

print(length)