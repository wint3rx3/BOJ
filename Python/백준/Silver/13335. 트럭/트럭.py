import sys
from collections import deque

input = sys.stdin.readline
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
time = w
current_weight = 0

while trucks:
    current_weight -= bridge.popleft()
    
    if current_weight + trucks[0] <= l:
        truck = trucks.pop(0)
        bridge.append(truck)
        current_weight += truck
    else:
        bridge.append(0)
    
    time += 1

print(time)