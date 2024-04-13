import sys
#sys.stdin.readline().rstrip().split()

def processStatus(boundary, altitude, status):
    for i in range(N):
        for j in range(N):
            if altitude[i][j] > boundary:
                status[i][j] = 1

def bfs(x, y, status, n):
    q = [(x, y)]
    status[x][y] += 1

    while len(q) > 0:
        i, j = q.pop(0)

        if i >= 1 and status[i - 1][j] == 1:
            q.append((i - 1, j))
            status[i - 1][j] += 1
        
        if i < n - 1 and status[i + 1][j] == 1:
            q.append((i + 1, j))
            status[i + 1][j] += 1
        
        if j >= 1 and status[i][j - 1] == 1:
            q.append((i, j - 1))
            status[i][j - 1] += 1
        
        if j < n - 1 and status[i][j + 1] == 1:
            q.append((i, j + 1))
            status[i][j + 1] += 1

N = int(input())
altitude = []
maxValue = 0
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    altitude.append(tmp)
    localMax = max(tmp)
    if localMax > maxValue:
        maxValue = localMax

result = 1
for i in range(1, maxValue):
    status = [[0 for k in range(N)] for j in range(N)]
    processStatus(i, altitude, status)
    cnt = 0
    for j in range(N):
        for k in range(N):
            if status[j][k] == 1:
                bfs(j, k, status, N)
                cnt += 1
    if cnt > result:
        result = cnt

print(result)