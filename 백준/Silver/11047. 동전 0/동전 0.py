import sys
#sys.stdin.readline().rstrip().split()

N, K = map(int, sys.stdin.readline().rstrip().split())
list = [0] * N
for i in range(N):
    list[i] = int(input())

list = list[::-1]
cnt = 0
for i in list:
    if K == 0:
        break
    cnt += K // i
    K %= i
print(cnt)