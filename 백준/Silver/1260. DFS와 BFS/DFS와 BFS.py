import sys
#sys.stdin.readline().rstrip().split()

def dfs(val, statusList, edgeList):
    statusList[val] = 1
    print(val, end=" ")   

    for i in edgeList[val]:
        if statusList[i] == 0:
            dfs(i, statusList, edgeList)
    
    statusList[val] = 2

def bfs(val, statusList, edgeList):
    queue = []
    queue.append(val)
    print(val, end=" ")
    statusList[val] = 1
    while len(queue) > 0:
        v = queue.pop(0)
        for i in edgeList[v]:
            if statusList[i] == 0:
                print(i, end=" ")
                statusList[i] = 1
                queue.append(i)
    
        statusList[v] = 2

status = [0] * 1001
edge = [[]] * 1001

N, M, V = map(int, sys.stdin.readline().rstrip().split())

for i in range(M):
    f, t = map(int, sys.stdin.readline().rstrip().split())
    if len(edge[f]) == 0:
        edge[f] = [t]
    else:
        edge[f].append(t)

    if len(edge[t]) == 0:
        edge[t] = [f]
    else:
        edge[t].append(f)

for i in range(1, N + 1):
    edge[i] = sorted(edge[i])
    

dfs(V, status, edge)
status = [0] * 1001
print()
bfs(V, status, edge)
