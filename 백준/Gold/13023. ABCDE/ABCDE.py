import sys
#sys.stdin.readline().rstrip().split()

def dfs(start, status, link, degree):
    if degree >= 4:
        return 1
    status[start] = 1
    for val in link[start]:
        if status[val] == 0:
            tmp = dfs(val, status, link, degree + 1)
            if tmp == 1:
                return 1
    status[start] = 0
    return 0
    

N, M = map(int, sys.stdin.readline().rstrip().split())
link = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    link[a].append(b)
    link[b].append(a)

for i in range(N):
    status = [0]*N
    result = dfs(i, status, link, 0)
    if result == 1:
        print(1)
        break
    if i == N - 1:
        print(0)