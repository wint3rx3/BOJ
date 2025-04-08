import sys

def process_case(x, n, legos):
    target = x * 10_000_000
    legos.sort()
    left, right = 0, n - 1

    while left < right:
        total = legos[left] + legos[right]
        if total == target:
            print(f"yes {legos[left]} {legos[right]}")
            return
        elif total < target:
            left += 1
        else:
            right -= 1
    print("danger")

def main():
    input = sys.stdin.readline
    while True:
        x_str = input()
        if not x_str:
            break
        x = int(x_str)
        n = int(input())
        if n == 0:
            print("danger")
            continue

        legos = []
        for _ in range(n):
            legos.append(int(input()))

        process_case(x, n, legos)

if __name__ == "__main__":
    main()
