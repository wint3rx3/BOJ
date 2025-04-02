T = int(input())

for _ in range(T):
    n = int(input())
    pos = 0
    result = []
    while n > 0:
        if n & 1:
            result.append(str(pos))
        n >>= 1
        pos += 1
    print(' '.join(result))
