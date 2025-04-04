def find_nth_decreasing_number(n):
    decreasing_numbers = []

    def dfs(current, last_digit):
        decreasing_numbers.append(int(current))
        for next_digit in range(0, last_digit):
            dfs(current + str(next_digit), next_digit)

    for i in range(10):
        dfs(str(i), i)

    decreasing_numbers.sort()

    if n < len(decreasing_numbers):
        return decreasing_numbers[n]
    else:
        return -1

n = int(input())
print(find_nth_decreasing_number(n))