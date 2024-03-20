import sys
#sys.stdin.readline().rstrip().split()

T = int(input())
for i in range(T):
    N = int(input())

    grade = [0] * 100001
    min = N + 1
    for j in range(N):
        port, inter = map(int, sys.stdin.readline().rstrip().split())
        grade[port] = inter

    cnt = 0
    for j in range(1, N + 1):
        interview = grade[j]
        if interview > min:
            continue
        cnt = cnt + min - interview - 1
        min = interview

    print(N - cnt)