import sys

N = int(sys.stdin.readline())
up = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
down = list(map(int, sys.stdin.readline().split()))

up = sorted(up)
sorted_down = sorted(down)

pair = {}
for i in down:
    pair[i] = 0

i = 0
j = 0
while i < N and j < M:
    if up[i] < sorted_down[j]:
        i += 1
    elif up[i] == sorted_down[j]:
        i += 1
        pair[sorted_down[j]] += 1
    else:
        j += 1

for i in down:
    print(pair[i], end=' ')