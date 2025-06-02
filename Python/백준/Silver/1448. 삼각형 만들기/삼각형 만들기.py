import sys

input = sys.stdin.readline

n = int(input())
sticks = [int(input()) for _ in range(n)]

sticks.sort()  # 오름차순 정렬

answer = -1
# 뒤에서부터 3개씩 검사 (큰 것부터)
for i in range(n - 1, 1, -1):
    a, b, c = sticks[i], sticks[i - 1], sticks[i - 2]
    if a < b + c:
        answer = a + b + c
        break

print(answer)
