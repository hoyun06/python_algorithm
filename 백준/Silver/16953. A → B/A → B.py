import sys
#sys.stdin.readline().rstrip().split()

A, B = map(int, sys.stdin.readline().rstrip().split())

i = B
cnt = 1
while i > 0:
    if i == A:
        break;
    
    if i % 2 == 0:
        i = i // 2
        cnt += 1
    elif (i - 1) % 10 == 0 and i != 1:
        i = (i - 1) // 10 
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)