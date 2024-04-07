import sys
#sys.stdin.readline().rstrip().split()

def bfs(n, k, min, max, time):
    q = []
    q.append(n)
    while len(q) > 0:
        val = q.pop(0)
        if val == k:
            return time[val]

        forward = val + 1
        backward = val - 1
        jump = val*2

        if forward == k or backward == k or jump == k:
            return time[val] + 1
        
        if forward >= min and forward <= max and time[forward] == 0:
            q.append(forward)
            time[forward] = time[val] + 1
        if backward >= min and backward <= max and time[backward] == 0:
            q.append(backward)
            time[backward] = time[val] + 1
        if jump >= min and jump <= max and time[jump] == 0:
            q.append(jump)
            time[jump] = time[val] + 1



N, K = map(int, sys.stdin.readline().rstrip().split())
MIN = 0
MAX = 100000
time = [0] * 100001
print(bfs(N, K, MIN, MAX, time))