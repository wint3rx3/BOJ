def solve_race_case(N, X, Y, V):
    others = V[:-1]
    my_speed = V[-1]

    min_other_time = min(X / v for v in others)

    if X / my_speed < min_other_time:
        return 0

    left, right = 1, min(Y, X)
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        my_time = 1 + (X - mid) / my_speed

        if my_time < min_other_time:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))
    print(solve_race_case(N, X, Y, V))
