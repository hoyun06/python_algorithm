import sys


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break;

    sang = set([int(sys.stdin.readline()) for _ in range(N)])
    sun = set([int(sys.stdin.readline()) for _ in range(M)])
    
    if N == 0 or M == 0:
        print(0)
        continue
    
    cnt = 0
    
    for i in sang:
        if i in sun:
            cnt += 1
    print(cnt)