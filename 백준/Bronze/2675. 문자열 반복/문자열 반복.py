import sys

T = int(input())
for i in range(T):
    inputs = sys.stdin.readline().rstrip().split()
    R = int(inputs[0])
    S = inputs[1]
    for j in S:
        for i in range(R):
            print(j, end='')
    
    print()