import sys
import collections
#sys.stdin.readline().rstrip().split()

def bfs(q, tomatoes, initialTomatoCnt):
    day = -1
    tomatoCnt = initialTomatoCnt
    while len(q) > 0:
        r, c = q.popleft()
        if r > 0 and tomatoes[r - 1][c] == 0:
            q.append((r - 1, c))
            tomatoes[r - 1][c] = tomatoes[r][c] + 1
            day = tomatoes[r - 1][c]
            tomatoCnt += 1
        if r < ROW - 1 and tomatoes[r + 1][c] == 0:
            q.append((r + 1, c))
            tomatoes[r + 1][c] = tomatoes[r][c] + 1
            day = tomatoes[r + 1][c]
            tomatoCnt += 1
        if c > 0 and tomatoes[r][c - 1] == 0:
            q.append((r, c - 1))
            tomatoes[r][c - 1] = tomatoes[r][c] + 1
            day = tomatoes[r][c - 1]
            tomatoCnt += 1
        if c < COL - 1 and tomatoes[r][c + 1] == 0:
            q.append((r, c + 1))
            tomatoes[r][c + 1] = tomatoes[r][c] + 1
            day = tomatoes[r][c + 1]
            tomatoCnt += 1
    
    return (day - 1, tomatoCnt)


COL, ROW = map(int, sys.stdin.readline().rstrip().split())

tomatoes = [[0 for i in range(COL)] for j in range(ROW)]

emptyCnt = 0
initialTomatoCnt = 0
q = collections.deque([])
for i in range(ROW):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(COL):
        if row[j] == 1:
            initialTomatoCnt += 1
            q.append((i, j))
        elif row[j] == -1:
            emptyCnt += 1
        tomatoes[i][j] = row[j]

if emptyCnt + initialTomatoCnt == ROW * COL:
    print(0)
else:
    day, tomatoCnt = bfs(q, tomatoes, initialTomatoCnt)
    if emptyCnt + tomatoCnt != ROW * COL:
        print(-1)
    else:
        print(day)