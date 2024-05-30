import sys
#sys.stdin.readline().rstrip().split()

def bfs(start, status, relocator, diceRoll):
    q = [(start, diceRoll)]
    status[start] = 1
    
    while len(q) > 0:
        val, roll = q.pop(0)
        for i in range(1, 7):
            target = val + i
            if target == 100:
                return roll + 1
            if status[target] == 0:
                if relocator[target] != 0:
                    q.append((relocator[target], roll + 1))
                    status[relocator[target]] = 1
                else:
                    q.append((target, roll + 1))
                
                status[target] = 1
            

N, M = map(int, sys.stdin.readline().rstrip().split())
relocator = [0]*100

for i in range(N + M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    relocator[x] = y

status = [0]*100
print(bfs(1, status, relocator, 0))