import sys
#sys.stdin.readline().rstrip().split()

def calculate_total_length(list):
    total = 0
    for i in list:
        total += i
    return total
def is_valid(value, list, num_of_ray):
    cnt = 0
    i = 0
    sum = 0
    while i < len(list):
        if cnt >= num_of_ray:
            return False
        if sum + list[i] > value:
            cnt += 1
            sum = 0
        else:
            sum += list[i]
            i += 1
    return True
        

N, M = map(int, sys.stdin.readline().rstrip().split())
video_length = list(map(int, sys.stdin.readline().rstrip().split()))

r = calculate_total_length(video_length)
l = r // M
min = r
while l <= r:
    m = (l + r) // 2
    result = is_valid(m, video_length, M)
    if result:
        r = m - 1
        if m < min:
            min = m
    else:
        l = m + 1

print(min)