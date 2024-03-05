import sys
#sys.stdin.readline().rstrip().split()

N = int(input())    # 1 <= N <= 100,000
                    # k 개의 로프로 w 물체 들어올리면 각 로프에는 w / k 중량
weight = [0] * N
for i in range(N):
    weight[i] = int(input())

sortedWeight = sorted(weight)
max = 0
for i in range(N):
    result = ( N - i) * sortedWeight[i]
    if max < result:
        max = result
print(max)