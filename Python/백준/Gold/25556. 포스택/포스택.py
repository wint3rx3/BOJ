def main(n, arr):
    stacks = [[0] for _ in range(4)]

    for num in arr:
        placed = False
        for stack in stacks:
            if stack[-1] < num:
                stack.append(num)
                placed = True
                break
        if not placed:
            return "NO"

    return "YES"

n = int(input())
arr = list(map(int, input().split()))

print(main(n, arr))