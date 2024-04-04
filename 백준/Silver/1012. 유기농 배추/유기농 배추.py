import sys
#sys.stdin.readline().rstrip().split()

def bfs(posList, i, j, n, m):
    q = [(i,j)]
    posList[i][j] = 0
    while len(q) > 0:
        x, y = q.pop(0)
        if x > 0 and posList[x - 1][y] == 1:
            q.append((x - 1, y))
            posList[x - 1][y] = 0
        if x < n - 1 and posList[x + 1][y] == 1:
            q.append((x + 1, y))
            posList[x + 1][y] = 0
        if y > 0 and posList[x][y - 1] == 1:
            q.append((x, y - 1))
            posList[x][y - 1] = 0
        if y < m - 1 and posList[x][y + 1] == 1:
            q.append((x, y + 1))
            posList[x][y + 1] = 0


T = int(input())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    rows = N
    cols = M
    pos = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        pos[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if pos[i][j] == 1:
                bfs(pos, i, j, N, M)
                cnt += 1

    print(cnt)