import sys
#sys.stdin.readline().rstrip().split()

N , M = map(int, sys.stdin.readline().rstrip().split()) 
price = []

for i in range(M):
    package, piece = map(int, sys.stdin.readline().rstrip().split())
    price.append([package, piece])

packageMin = price[0][0]
pieceMin = price[0][1]
for i in range(1, M):
    localList = price[i]
    if localList[0] < packageMin:
        packageMin = localList[0]
    if localList[1] < pieceMin:
        pieceMin = localList[1]

if N < 6:
    if packageMin < N * pieceMin:
        print(packageMin)
    else:
        print(N * pieceMin)
else:
    quotient = N // 6
    onlyPackage = (quotient + 1) * packageMin
    mix = (packageMin * quotient) + (N - 6 * quotient) * pieceMin
    onlyPiece = N * pieceMin
    print(min(onlyPackage, mix, onlyPiece))