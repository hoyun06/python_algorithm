import sys
#sys.stdin.readline().rstrip().split()

def processQueueAndStatus(q, x, y, degree, status, maximum):
    q.append(((x, y), degree))
    status[x][y] = 1
    if maximum < degree:
        return degree
    return maximum

def bfs(x, y, status):
    q = [((x,y), 0)]
    status[x][y] = 1
    maximum = 0

    while len(q) > 0:
        val = q.pop(0)
        row, col = val[0]
        degree = val[1] + 1

        if row > 0 and treasure[row - 1][col] == 'L' and status[row - 1][col] == 0:
            maximum = processQueueAndStatus(q, row - 1, col, degree, status, maximum)
        if col > 0 and treasure[row][col - 1] == 'L' and status[row][col - 1] == 0:
            maximum = processQueueAndStatus(q, row, col - 1, degree, status, maximum)
        if row < ROW - 1 and treasure[row + 1][col] == 'L' and status[row + 1][col] == 0:
            maximum = processQueueAndStatus(q, row + 1, col, degree, status, maximum)
        if col < COL - 1 and treasure[row][col + 1] == 'L' and status[row][col + 1] == 0:
            maximum = processQueueAndStatus(q, row, col + 1, degree, status, maximum)
    return maximum

ROW, COL = map(int, sys.stdin.readline().rstrip().split())
treasure = [['' for i in range(COL)]  for j in range(ROW)]
for i in range(ROW):
    row = sys.stdin.readline().rstrip()
    ind = 0
    for j in row:
        treasure[i][ind] = j
        ind += 1

max = 0
for i in range(ROW):
    for j in range(COL):
        if treasure[i][j] == 'L':
            status = [[0 for k in range(COL)] for l in range(ROW)]
            result = bfs(i, j, status)
            if result > max:
                max = result

print(max)