import sys
#sys.stdin.readline().rstrip().split()

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

while len(T) > 0:
    if T == S:
        break

    if T[-1] == 'B':
        T = T[::-1][1::]
    else:
        T = T[:len(T) - 1:]

if len(T) > 0:
    print(1)
else:
    print(0)