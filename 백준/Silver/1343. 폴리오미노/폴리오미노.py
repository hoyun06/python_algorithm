import sys
#sys.stdin.readline().rstrip().split()

AAAA = str("AAAA")
BB = str("BB")
result = str("")

board = sys.stdin.readline().rstrip()
i = 0
while i < len(board):
    if board[i] == ".":
        i += 1
        result += "."
        continue

    cnt = 0
    ind = board.find(".", i)
    if ind == -1:
        cnt = len(board) - i
    else:
        cnt = ind - i
    
    if cnt % 2 != 0:
        result = str("-1")
        break
    result += AAAA * (cnt // 4)
    if cnt % 4 != 0:
        result += BB
    
    if ind == -1:
        break
    i = ind

print(result)