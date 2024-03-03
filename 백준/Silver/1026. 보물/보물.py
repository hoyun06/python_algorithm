import sys
#sys.stdin.readline().rstrip().split()

N = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A = sorted(A)
B = sorted(B)
B = B[::-1]

min = 0
for i in range(N):
    min +=  A[i] * B[i]
print(min)