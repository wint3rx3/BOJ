def hamming_distance(dna1, dna2):
    return sum(1 for a, b in zip(dna1, dna2) if a != b)

N, M = map(int, input().split())
sequences = [input().strip() for _ in range(N)]
result = ''
distance_sum = 0

for i in range(M):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for seq in sequences:
        count[seq[i]] += 1
    max_nucleotide = max(count, key=lambda x: (count[x], -ord(x)))
    result += max_nucleotide
    distance_sum += N - count[max_nucleotide]

print(result)
print(distance_sum)