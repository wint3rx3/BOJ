import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    visible = list(map(int, input().split()))
    
    graph = defaultdict(list)

    for _ in range(M):
        a, b, t = map(int, input().split())

        # 핵심 예외 처리:
        if (visible[a] == 1 and a != N - 1) or (visible[b] == 1 and b != N - 1):
            continue

        graph[a].append((t, b))
        graph[b].append((t, a))

    INF = float('inf')
    dist = [INF] * N
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] < cost:
            continue
        for w, neighbor in graph[node]:
            if dist[neighbor] > cost + w:
                dist[neighbor] = cost + w
                heapq.heappush(pq, (dist[neighbor], neighbor))

    print(dist[N - 1] if dist[N - 1] != INF else -1)

if __name__ == "__main__":
    main()
