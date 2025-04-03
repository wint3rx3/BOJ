def can_reach_end(board, n):
    visited = [[False]*n for _ in range(n)]
    
    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= n:
            return False
        if visited[x][y]:
            return False
        visited[x][y] = True

        if board[x][y] == -1:
            return True
        
        jump = board[x][y]
        if jump == 0:
            return False
        
        return dfs(x + jump, y) or dfs(x, y + jump)

    return dfs(0, 0)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

if can_reach_end(board, n):
    print("HaruHaru")
else:
    print("Hing")