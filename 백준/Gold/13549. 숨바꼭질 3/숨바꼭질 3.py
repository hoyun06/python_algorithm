import sys
#sys.stdin.readline().rstrip().split()

def bfs(status, start, target):
    if start == target:
        return 0
    q = [(start, 0)]
    status[start] = 1


    while len(q) > 0:
        pos, time = q.pop(0)
        
        if pos > 0 and 2*pos < MAX and status[pos*2] == 0:
            if pos*2 == target:
                return time
            q.append((pos*2, time))
            status[pos*2] = 1
        if pos > 0 and status[pos - 1] == 0:
            if pos - 1 == target:
                return time + 1
            q.append((pos - 1, time + 1))
            status[pos - 1] = 1
        if pos < MAX - 1 and status[pos + 1] == 0:
            if pos + 1 == target:
                return time + 1
            q.append((pos + 1, time + 1))
            status[pos + 1] = 1

        

N, K = map(int, sys.stdin.readline().rstrip().split())
MAX = 100001
status = [0]*MAX

print(bfs(status, N, K))