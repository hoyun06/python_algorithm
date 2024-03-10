import sys
#sys.stdin.readline().rstrip().split()

N = sys.stdin.readline().rstrip()

N = sorted(N)[::-1]
if N[-1] != '0':
    print(-1)
else:
    sum = 0
    for i in N:
        sum += int(i)
    
    if sum % 3 == 0:
        print(''.join(N))
    else:
        print(-1)