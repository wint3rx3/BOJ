target = input().strip()

n = int(input())

count = 0

for _ in range(n):
    ring = input().strip()
    doubled = ring + ring
    if target in doubled:
        count += 1

print(count)