def main(n):
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 2
        count += 1
    return -1

# 입력 받기
n = int(input())
print(main(n))