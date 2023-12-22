s = input()
position = [-1] * 26
for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    if position[index] == -1:
        position[index] = i

for i in range(26):
    print(position[i], end=' ')