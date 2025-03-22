import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    list1 = [int(input()) for _ in range(N)]
    list2 = [int(input()) for _ in range(M)]

    i = j = cnt = 0

    while i < N and j < M:
        if list1[i] == list2[j]:
            cnt += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    print(cnt)