import sys
#sys.stdin.readline().rstrip().split()

def bfs(start, status, child, childCnt, parent):
    q = [start]
    status[start] = 1

    while len(q) > 0:
        val = q.pop(0)
        for i in parent[val]:
            if i != -1:
                childCnt[i] -= 1
        for i in child[val]:
            if status[i] == 0:
                q.append(i)
                status[i] = 1

        childCnt[val] = -1

N = int(input())
child = [[] for i in range(N)]
childCnt = [0]*N
parentInput = list(map(int, sys.stdin.readline().rstrip().split()))
parent = [[] for i in range(N)]

ind = 0
for i in parentInput:
    parent[ind].append(i)
    if i != -1:
        child[i].append(ind)
        childCnt[i] += 1
    ind += 1

TARGET = int(input())

status = [0]*N
bfs(TARGET, status, child, childCnt, parent)

cnt = 0
for i in childCnt:
    if i == 0:
        cnt += 1
print(cnt)