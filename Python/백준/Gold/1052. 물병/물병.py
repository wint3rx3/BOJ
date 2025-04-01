def count_ones(n):
    return bin(n).count('1')

def min_additional_bottles(N, K):
    if K >= N:
        return 0
    
    added = 0
    while count_ones(N) > K:
        added += 1
        N += 1
    return added

N, K = map(int, input().split())
print(min_additional_bottles(N, K))
