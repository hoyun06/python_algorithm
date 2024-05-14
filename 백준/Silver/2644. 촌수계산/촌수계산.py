import sys
#sys.stdin.readline().rstrip().split()

def dfs(start, relation, status, target, cnt):
    status[start] = 1
    
    for i in relation[start]:
        if i == target:
            return cnt
        if status[i] == 0:
            tmp = dfs(i, relation, status, target, cnt + 1)
            if tmp != -1:
                return tmp
    return -1

N = int(input())
S, T = map(int, sys.stdin.readline().rstrip().split())
M = int(input())

relation = [[] for i in range(N + 1)]
status = [0 for i in range(N + 1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    relation[x].append(y)
    relation[y].append(x)

print(dfs(S, relation, status, T, 1))