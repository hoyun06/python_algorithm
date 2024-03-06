import sys
#sys.stdin.readline().rstrip().split()

S = sys.stdin.readline().rstrip()
zCount = 0
oCount = 0

if S[0] == '0':
    isZero = True
    zCount += 1
else:
    isZero = False
    oCount += 1

for i in range(1, len(S)):
    if S[i] == '0':
        if isZero:
            continue
        else:
            zCount += 1
            isZero = True
    else:
        if not isZero:
            continue
        else:
            oCount += 1
            isZero = False

print(min(zCount, oCount))