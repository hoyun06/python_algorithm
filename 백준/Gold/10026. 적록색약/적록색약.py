import sys
#sys.stdin.readline().rstrip().split()

def bfs_1(row, col, color, status):
    q = [(row, col)]
    status[row][col] = 1
    val = color[row][col]

    while len(q) > 0:
        x, y = q.pop(0)

        if x > 0 and status[x - 1][y] == 0 and color[x - 1][y] == val:
            status[x - 1][y] = 1
            q.append((x - 1, y))
        if x < N - 1 and status[x + 1][y] == 0 and color[x + 1][y] == val:
            status[x + 1][y] = 1
            q.append((x + 1, y))
        if y > 0 and status[x][y - 1] == 0 and color[x][y - 1] == val:
            status[x][y - 1] = 1
            q.append((x, y - 1))
        if y < N - 1 and status[x][y + 1] == 0 and color[x][y + 1] == val:
            status[x][y + 1] = 1
            q.append((x, y + 1))

def bfs_2(row, col, color, status):
    q = [(row, col)]
    status[row][col] = 1
    val = color[row][col]
    check = ['R', 'G']

    while len(q) > 0:
        x, y = q.pop(0)

        if x > 0 and status[x - 1][y] == 0:
            if color[x - 1][y] == val or (val != 'B' and color[x - 1][y] in check): 
                status[x - 1][y] = 1
                q.append((x - 1, y))
        if x < N - 1 and status[x + 1][y] == 0:
            if color[x + 1][y] == val or (val != 'B' and color[x + 1][y] in check): 
                status[x + 1][y] = 1
                q.append((x + 1, y))
        if y > 0 and status[x][y - 1] == 0:
            if color[x][y - 1] == val or (val != 'B' and color[x][y - 1] in check): 
                status[x][y - 1] = 1
                q.append((x, y - 1))
        if y < N - 1 and status[x][y + 1] == 0 :
            if color[x][y + 1] == val or (val != 'B' and color[x][y + 1] in check): 
                status[x][y + 1] = 1
                q.append((x, y + 1))


N = int(input())
color = [[' ' for i in range(N)] for j in range(N)]
status_1 = [[0 for i in range(N)] for j in range(N)]
status_2 = [[0 for i in range(N)] for j in range(N)]


for i in range(N):
    row = sys.stdin.readline().rstrip()
    ind = 0
    for j in row:
        color[i][ind] = j
        ind += 1

section_1 = 0
for i in range(N):
    for j in range(N):
        if status_1[i][j] == 0:
            bfs_1(i, j, color, status_1)
            section_1 += 1

section_2 = 0
for i in range(N):
    for j in range(N):
        if status_2[i][j] == 0:
            bfs_2(i, j, color, status_2)
            section_2 += 1

print(section_1, section_2)