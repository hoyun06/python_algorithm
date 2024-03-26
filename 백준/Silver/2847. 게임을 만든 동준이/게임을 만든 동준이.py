import sys
#sys.stdin.readline().rstrip().split()

N = int(input())

score = [0] * 101
for i in range(1, N + 1):
    score[i] = int(input())

cnt = 0
for i in range(N - 1, 0, -1):
    while score[i] >= score[i + 1]:
        score[i] -= 1
        cnt += 1

print(cnt)