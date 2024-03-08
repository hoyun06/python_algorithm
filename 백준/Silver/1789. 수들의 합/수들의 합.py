import sys
#sys.stdin.readline().rstrip().split()

S = int(input())

i = 1
sum = 0
while True:
    sum += i
    if S > sum:
        i += 1
    elif S == sum:
        print(i)
        break
    else:
        print(i - 1)
        break