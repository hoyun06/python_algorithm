import sys

N, M = map(int, input().split())
matrix = []
for i in range(N):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(numbers)

sum = []
for i in range(N):
    tmp = list(range(N))
    sum.append(tmp)

for row in range(N):
    for col in range(N):
        if row == 0:
            if col == 0:
                sum[row][col] = matrix[0][0]
            else:
                sum[row][col] = sum[row][col - 1] + matrix[row][col]
        else:
            if col == 0:
                sum[row][col] = sum[row - 1][col] + matrix[row][col]
            else:
                sum[row][col] = sum[row - 1][col] + sum[row][col - 1] - sum[row - 1][col - 1] + matrix[row][col]

for i in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().rstrip().split()))
    result = sum[x2 - 1][y2 - 1]
    a = 0
    b = 0

    if x1 != 1:
        result -= sum[x1 - 2][y2 - 1]
        a = 1
    if y1 != 1:
        result -= sum[x2 - 1][y1 - 2]
        b = 1
    if a == 1 and b == 1:
        result += sum[x1 - 2][y1 - 2]
    print(result)