import sys

N, M = map(int, input().split())
numbers = sys.stdin.readline().rstrip().split()
sum = list(range(N))
sum[0] = int(numbers[0])

for i in range(1, N):
    sum[i] = sum[i - 1] + int(numbers[i])
    
for i in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    if start == 1:
        print(sum[end - 1])
    else:
        print(sum[end - 1] - sum[start - 2])