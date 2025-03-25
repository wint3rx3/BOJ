import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

visited = [False] * n
result_set = set()

def dfs(path, depth):
    if depth == k:
        num_str = ''.join(path)
        result_set.add(num_str)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(path + [cards[i]], depth + 1)
            visited[i] = False

dfs([], 0)
print(len(result_set))