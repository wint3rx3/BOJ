H, W = map(int, input().split())
grid = [input() for _ in range(H)]

for row in grid:
    result = []
    cloud_time = -1

    for j in range(W):
        if row[j] == 'c':
            cloud_time = 0
            result.append(0)
        elif cloud_time == -1:
            result.append(-1)
        else:
            cloud_time += 1
            result.append(cloud_time)

    print(' '.join(map(str, result)))
