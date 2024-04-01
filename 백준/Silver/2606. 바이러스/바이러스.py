import sys
#sys.stdin.readline().rstrip().split()

status = [0] * 101
edge = [[]] * 101

N = int(input())
E = int(input())

for i in range(E):
    f, t = map(int, sys.stdin.readline().rstrip().split())
    if len(edge[f]) == 0:
        edge[f] = [t]
    else:
        edge[f].append(t)

    if len(edge[t]) == 0:
        edge[t] = [f]
    else:
        edge[t].append(f)

cnt = 0
queue = []
queue.append(1)
status[1] = 1
while len(queue) > 0:
    val = queue.pop(0)
    for i in edge[val]:
        if status[i] == 0:
            cnt += 1
            status[i] = 1
            queue.append(i)
    
    status[val] = 2

print(cnt)