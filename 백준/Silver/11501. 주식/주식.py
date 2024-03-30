import sys
#sys.stdin.readline().rstrip().split()

T = int(input())
for i in range(T):
    N = int(input())
    counter = [0] * 10001
    stockPrice = list(map(int, sys.stdin.readline().rstrip().split()))
    stockPriceDescOrder = sorted(stockPrice)[::-1]
    
    for i in stockPrice:
        counter[i] += 1
    
    i = 0
    j = 0
    cnt = 0
    sum = 0
    profit = 0
    while i < len(stockPrice):
        while counter[stockPriceDescOrder[j]] == 0:
            j += 1
        val = stockPriceDescOrder[j]
        if stockPrice[i] != val:
            cnt += 1
            sum += stockPrice[i]
            counter[stockPrice[i]] -= 1
            i += 1
        else:
            profit += (cnt * val - sum)
            counter[stockPriceDescOrder[j]] -= 1
            j += 1
            sum = 0
            cnt = 0
            i += 1

    print(profit)