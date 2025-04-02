import sys
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    _, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

room_heap = []

for start, end in lectures:
    if room_heap and room_heap[0] <= start:
        heapq.heappop(room_heap)
    heapq.heappush(room_heap, end)

print(len(room_heap))
