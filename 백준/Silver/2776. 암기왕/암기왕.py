import sys

T = int(input())
for t in range(T):
    N = int(input())
    note_1 = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(input())
    note_2 = list(map(int, sys.stdin.readline().rstrip().split()))
    sorted_note1 = sorted(note_1)
    sorted_note2 = sorted(note_2)
    i = 0
    j = 0
    match = {}
    while i < N and j < M:
        if sorted_note1[i] < sorted_note2[j]:
            i += 1
            match[sorted_note2[j]] = 0
            continue
        elif sorted_note1[i] > sorted_note2[j]:
            match[sorted_note2[j]] = 0
            j += 1
            continue
        match[sorted_note2[j]] = 1
        j += 1

    if i >= N:
        while j < M:
            match[sorted_note2[j]] = 0
            j += 1
    
    for n in note_2:
        print(match[n])