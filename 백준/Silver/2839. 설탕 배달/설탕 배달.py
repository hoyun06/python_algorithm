import sys
#sys.stdin.readline().rstrip().split()

N = int(input())
weight = [-1] * (N + 1)
weight[3] = 1
for i in range(4, N + 1):
    subThree = weight[i - 3]
    subFive = weight[i - 5]
    if i == 5:
        weight[i] = 1
        continue
    if subThree == -1 and subFive == -1:
        continue
    elif subThree == -1 or subFive == -1:
        weight[i] = max(subThree, subFive) + 1
    else:
        weight[i] = min(subThree, subFive) + 1

print(weight[N])