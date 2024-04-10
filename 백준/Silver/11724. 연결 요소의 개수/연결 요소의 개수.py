import sys
#sys.stdin.readline().rstrip().split()

N, M = map(int, sys.stdin.readline().rstrip().split())

def bfs(status, edge, start):
    q = []
    q.append(start)
    status[start] = 1

    while len(q) > 0:
        val = q.pop(0)
        for i in edge[val]:
            if status[i] == 0:
                status[i] = 1
                q.append(i)

edge = [[] for i in range(N + 1)]
status = [0] * (N + 1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    edge[u].append(v)
    edge[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if status[i] == 0:
        bfs(status, edge, i)
        cnt += 1

print(cnt)