import sys
#sys.stdin.readline().rstrip().split()

N, L = map(int, sys.stdin.readline().rstrip().split())
leak = list(map(int, sys.stdin.readline().rstrip().split()))

leak = sorted(leak)
cnt = 0
i = 0
while i < N:
    if i == N - 1:
        cnt +=1
        break

    val = leak[i] + L - 1
    while i < N and leak[i + 1] <= val:
        i += 1
        if i == N - 1:
            break
    cnt += 1
    i += 1

print(cnt)        