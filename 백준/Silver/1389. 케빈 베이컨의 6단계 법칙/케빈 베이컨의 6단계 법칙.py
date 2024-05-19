import sys
#sys.stdin.readline().rstrip().split()

def bfs(start, adj, record, status):
    status[start] = 1
    q = [(start, 0)]

    while len(q) > 0:
        val, degree = q.pop(0)
        for i in adj[val]:
            # if record[i][start] != 0:
            #     record[start][i] = record[i][start]
            #     status[i] = 1
            if status[i] == 0:
                record[start][i] = degree + 1
                record[i][start] = degree + 1
                status[i] = 1
                q.append((i, degree + 1))

        
 
N, M = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

record = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(1, N + 1):
    status = [0]*(N+1)
    bfs(i, adj, record, status)

tmpMin = 0
num = 0
for i in range(1, N + 1):
    total = sum(record[i])
    if i == 1:
        tmpMin = total
        num = 1
    else:
        if total < tmpMin:
            tmpMin = total
            num = i

print(num)