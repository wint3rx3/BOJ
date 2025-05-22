import sys

def cantor_set(n):
    if n == 0:
        return '-'
    else:
        prev = cantor_set(n - 1)
        return prev + ' ' * len(prev) + prev

for line in sys.stdin:
    n = int(line.strip())
    print(cantor_set(n))
