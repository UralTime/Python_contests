from collections import deque

n, m = map(int, input().split())
INF = 10 ** 5
dist = [[INF] * m for i in range(n)]
q = deque()
for i in range(n):
    j = 0
    for elem in input().split():
        if elem == '1':
            dist[i][j] = 0
            q.append((i, j))
        j += 1
while q:
    x, y = q.popleft()
    for u, v in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
        if 0 <= u < n and 0 <= v < m:
            if dist[u][v] == INF:
                dist[u][v] = dist[x][y] + 1
                q.append((u, v))
for row in dist:
    print(' '.join([str(elem) for elem in row]))
