import sys
#sys.stdin.readline().rstrip().split()

N = int(input())
withdrawalTime = list(map(int, sys.stdin.readline().rstrip().split()))

sortedWithdrawalTime = sorted(withdrawalTime)
result = [0] * N
result[0] = sortedWithdrawalTime[0]

ind = 0
for i in sortedWithdrawalTime:
    if ind == 0:
        result[ind] = i
    else:
        result[ind] = result[ind - 1] + i
    ind += 1

sum = 0
for i in result:
    sum += i

print(sum)