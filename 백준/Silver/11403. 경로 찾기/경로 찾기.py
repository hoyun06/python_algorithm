import sys
#sys.stdin.readline().rstrip().split()

def bfs(start, adjMat, status, result):
    q = []
    q.append(start)
    status[start] = 1

    while len(q) > 0:
        val = q.pop(0)
        for i in adjMat[val]:
            if i == start:
                result[start][start] = 1
            if status[i] == 0:
                status[i] = 1
                result[start][i] = 1
                q.append(i)

N = int(input())
adjMat = [[] for i in range(N)]
result = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()) )
    for j in range(N):
        if row[j] == 1:
            adjMat[i].append(j)

for i in range(N):
        status = [0 for j in range(N)]
        bfs(i, adjMat, status, result)

for i in range(N):
    for j in range(N):
          print(result[i][j], end=" ")
    print()