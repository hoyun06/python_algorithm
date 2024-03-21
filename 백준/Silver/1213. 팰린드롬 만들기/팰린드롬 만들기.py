import sys
#sys.stdin.readline().rstrip().split()

sen = sys.stdin.readline().rstrip()

counter = [0] * 26
for i in sen:
    counter[ord(i) - 65] += 1

oddCounter = 0
oddChar = ''
for i in range(26):
    if counter[i] % 2 != 0:
        oddCounter += 1
        oddChar = chr(i + 65)

palindrome = str("")
if oddCounter > 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(26):
        if chr(i + 65) != oddChar:
            palindrome = palindrome + chr(i + 65) * (counter[i] // 2)
        elif counter[i] > 1:
            palindrome = palindrome + oddChar * ((counter[i] - 1) // 2)       
    
    if oddChar != '':
        palindrome = palindrome + oddChar
    
    for i in range(26):
        if chr(25 - i + 65) != oddChar:
            palindrome = palindrome + chr(25 - i + 65) * (counter[25 - i] // 2)
        elif counter[25 - i] > 1:
            palindrome = palindrome + oddChar * ((counter[25 - i] - 1) // 2) 

    print(palindrome)