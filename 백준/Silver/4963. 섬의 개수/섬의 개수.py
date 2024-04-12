import sys
#sys.stdin.readline().rstrip().split()

def processVertical(r, c, rowMax, landMap, status, q):
    if r - 1 >= 0 and landMap[r - 1][c] == 1 and status[r - 1][c] == 0:
            q.append((r - 1, c))
            status[r - 1][c] = 1
    if r < rowMax - 1 and landMap[r + 1][c] == 1 and status[r + 1][c] == 0:
        q.append((r + 1, c))
        status[r + 1][c] = 1
             
def processHorizontal(r, c, colMax, landMap, status, q):
    if c - 1 >= 0 and landMap[r][c - 1] == 1 and status[r][c - 1] == 0:
        q.append((r, c - 1))
        status[r][c - 1] = 1
    if c < colMax - 1 and landMap[r][c + 1] == 1 and status[r][c + 1] == 0:
        q.append((r, c + 1))
        status[r][c + 1] = 1

def processDiagonal(r, c, rowMax, colMax, landMap, status, q):
    if r - 1 >= 0:
        if c - 1 >= 0 and landMap[r - 1][c - 1] == 1 and status[r - 1][c - 1] == 0:
            q.append((r - 1, c - 1))
            status[r - 1][c - 1] = 1
        if c < colMax - 1 and landMap[r - 1][c + 1] == 1 and status[r - 1][c + 1] == 0:
            q.append((r - 1, c + 1))
            status[r - 1][c + 1] = 1
    if r < rowMax - 1:       
        if c - 1 >= 0 and landMap[r + 1][c - 1] == 1 and status[r + 1][c - 1] == 0:
            q.append((r + 1, c - 1))
            status[r + 1][c - 1] = 1 
        if c < colMax - 1 and landMap[r + 1][c + 1] == 1 and status[r + 1][c + 1] == 0:
            q.append((r + 1, c + 1))
            status[r + 1][c + 1] = 1  


def bfs(r, c, rowMax, colMax, landMap, status):
    q = [(r, c)]
    status[r][c] = 1

    while len(q) > 0:
        row, col = q.pop(0)
        processVertical(row, col, rowMax, landMap, status, q)
        processHorizontal(row, col, colMax, landMap, status, q)
        processDiagonal(row, col, rowMax, colMax, landMap, status, q)


while True:
    COL, ROW = map(int, sys.stdin.readline().rstrip().split())
    if COL == 0 and ROW == 0:
        break
    
    landMap = []
    status = [[0 for j in range(50)] for i in range(50)]
    for i in range(ROW):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        landMap.append(tmp)

    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if landMap[i][j] == 1 and status[i][j] == 0:
                bfs(i, j, ROW, COL, landMap, status)
                cnt += 1

    print(cnt)