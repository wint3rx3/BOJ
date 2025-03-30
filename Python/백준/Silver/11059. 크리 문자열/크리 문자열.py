def is_kri_string(sub):
    half = len(sub) // 2
    sum1 = sum(int(c) for c in sub[:half])
    sum2 = sum(int(c) for c in sub[half:])
    return sum1 == sum2

def find_longest_kri_string(S):
    n = len(S)
    for length in range(n, 1, -1):
        if length % 2 != 0:
            continue
        for i in range(n - length + 1):
            if is_kri_string(S[i:i+length]):
                return length
    return 0

S = input().strip()
print(find_longest_kri_string(S))