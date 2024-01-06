import sys

N = int(sys.stdin.readline().strip())
numbers = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline().strip())
targets = map(int, sys.stdin.readline().strip().split())

sorted_numbers = sorted(numbers)
length = len(sorted_numbers)

for i in targets:
    l = 0
    r = length - 1
    flag = True
    while l <= r:
        m = (l + r) // 2
        val = sorted_numbers[m]

        if val == i:
            print(1, end=' ')
            flag = False
            break
        elif val < i:
            l = m + 1
        else:
            r = m - 1        
    if flag:
        print(0, end=' ')