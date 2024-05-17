import sys
#sys.stdin.readline().rstrip().split()

def bfs(x, y, section):
    q = []
    section[x][y] = 1
    q.append((x, y))
    area = 1

    while len(q) > 0:
        vx, vy = q.pop(0)
        if vx > 0 and section[vx - 1][vy] == 0:
            q.append((vx - 1, vy))
            section[vx - 1][vy] = 1
            area += 1
        if vy > 0 and section[vx][vy - 1] == 0:
            q.append((vx, vy - 1))
            section[vx][vy - 1] = 1
            area += 1
        if vx < M - 1 and section[vx + 1][vy] == 0:
            q.append((vx + 1, vy))
            section[vx + 1][vy] = 1
            area += 1
        if vy < N - 1 and section[vx][vy + 1] == 0:
            q.append((vx, vy + 1))
            section[vx][vy + 1] = 1
            area += 1

    return area

M, N, K = map(int, sys.stdin.readline().rstrip().split())
section = [[0 for i in range(N)] for j in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for j in range(M - y2, M - y1):
        for k in range(x1, x2):
            section[j][k] = 1

result = []
for i in range(M):
    for j in range(N):
        if section[i][j] == 0:
            result.append(bfs(i, j, section))

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")