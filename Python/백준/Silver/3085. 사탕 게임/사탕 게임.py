def max_candies(board, n):
    max_count = 1

    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    return max_count

def solve(board, n):
    answer = 0
    for i in range(n):
        for j in range(n):
            # 오른쪽과 교환
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                answer = max(answer, max_candies(board, n))
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원복

            # 아래쪽과 교환
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                answer = max(answer, max_candies(board, n))
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원복

    return answer

# 입력
n = int(input())
board = [list(input().strip()) for _ in range(n)]

# 출력
print(solve(board, n))
