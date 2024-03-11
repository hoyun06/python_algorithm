import sys
#sys.stdin.readline().rstrip().split()

def calculateMin(v1, v2):
    if v1 == -1 and v2 == -1:
        return -1
    elif v1 == -1 or v2 == -1:
        return max(v1, v2)
    else:
        return min(v1, v2)

n = int(input())
if n == 1 or n == 3:
    print(-1)
elif n == 2 or n == 5:
    print(1)
elif n == 4:
    print(2)
else:
    dp = [-1] * 100001
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n + 1):
        result = calculateMin(dp[i - 2], dp[i - 5])
        if result == -1:
            dp[i] = -1
        else:
            dp[i] = result + 1
    print(dp[n])