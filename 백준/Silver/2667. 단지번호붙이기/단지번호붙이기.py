import sys
#sys.stdin.readline().rstrip().split()

def bfs(posList, i, j, n, m):
    q = [(i,j)]
    posList[i][j] = 0
    cnt = 1
    while len(q) > 0:
        x, y = q.pop(0)
        if x > 0 and posList[x - 1][y] == 1:
            q.append((x - 1, y))
            posList[x - 1][y] = 0
            cnt += 1
        if x < n - 1 and posList[x + 1][y] == 1:
            q.append((x + 1, y))
            posList[x + 1][y] = 0
            cnt += 1
        if y > 0 and posList[x][y - 1] == 1:
            q.append((x, y - 1))
            posList[x][y - 1] = 0
            cnt += 1
        if y < m - 1 and posList[x][y + 1] == 1:
            q.append((x, y + 1))
            posList[x][y + 1] = 0
            cnt += 1
    return cnt


N = int(input())
apartments = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    for j in range(N):
        if tmp[j] == '1':
            apartments[i][j] = 1

result = []
for i in range(N):
    for j in range(N):
        if apartments[i][j] == 1:
            result.append(bfs(apartments, i, j, N, N))

result = sorted(result)
print(len(result))
for i in result:
    print(i)