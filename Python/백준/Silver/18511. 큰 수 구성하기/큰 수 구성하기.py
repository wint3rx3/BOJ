from itertools import product

N, K_len = map(int, input().split())
K = list(input().split())

result = 0

for length in range(1, len(str(N)) + 1):
    for num in product(K, repeat=length):
        candidate = int(''.join(num))
        if candidate <= N:
            result = max(result, candidate)

print(result)