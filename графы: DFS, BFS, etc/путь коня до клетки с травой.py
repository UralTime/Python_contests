from collections import deque

q = deque()
n = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
dist = [[10 ** 5] * (n + 1) for i in range(n + 1)]
predok = [[(-1, -1) for i in range(n + 1)] for i in range(n + 1)]
q.append((x0, y0))
dist[x0][y0] = 0
while len(q) != 0:
    x, y = q.popleft()
    for u, v in [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2), (x + 1, y - 2), (x + 1, y + 2),
                 (x + 2, y - 1), (x + 2, y + 1)]:
        if 0 < u <= n and 0 < v <= n:
            if dist[u][v] == 10 ** 5:
                dist[u][v] = dist[x][y] + 1
                q.append((u, v))
                predok[u][v] = (x, y)
if dist[x1][y1] != 10 ** 5:
    print(dist[x1][y1])
    if dist[x1][y1] != 0:
        k, r = x1, y1
        path = []
        while (k, r) != (x0, y0):
            path.append((k, r))
            k, r = predok[k][r]
        path.append((k, r))
        for x, y in path[::-1]:
            print(x, y)
else:
    print(0)
