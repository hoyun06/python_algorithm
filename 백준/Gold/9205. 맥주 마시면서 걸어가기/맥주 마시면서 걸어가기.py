import sys
#sys.stdin.readline().rstrip().split()

def calculateDistance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def dfs(x, y, status, store, festival, statusIndex, length):
    if 1000 >= calculateDistance(x, y, festival[0], festival[1]):
        return 1
    
    result = 0
    status[statusIndex] = 1
    for i in range(length):
        posX, posY = store[i]
        if status[i] == 0 and calculateDistance(x, y, posX, posY) <= 1000:
            tmp = dfs(posX, posY, status, store, festival, i, length)
            if tmp == 1:
                return tmp
    return result

T = int(input())
for i in range(T):
    N = int(input())
    house = list(map(int, sys.stdin.readline().rstrip().split()))
    store = [0]*N
    for j in range(N):
        tmp = list(sys.stdin.readline().rstrip().split())
        store[j] = (int(tmp[0]), int(tmp[1]))
    festival = list(map(int, sys.stdin.readline().rstrip().split()))

    status = [0]*(N+2)
    result = dfs(house[0], house[1], status, store, festival, N, len(store))
    if result == 1:
        print("happy")
    else:
        print("sad")