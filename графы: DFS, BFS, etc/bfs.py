from collections import deque

q = deque()
n = int(input())
g = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    g[i] = [0] + [int(elem) for elem in input().split()]
dist = [10 ** 10] * (n + 1)
predok = [-1] * (n + 1)
x, y = map(int, input().split())
q.append(x)
dist[x] = 0
while len(q) != 0:
    v = q.popleft()
    for i in range(len(g[v])):
        if g[v][i] == 1:
            u = i
            if dist[u] == 10 ** 10:
                dist[u] = dist[v] + 1
                q.append(u)
                predok[u] = v
if dist[y] != 10 ** 10:
    print(dist[y])
    if dist[y] != 0:
        k = y
        path = []
        while k != x:
            path.append(str(k))
            k = predok[k]
        path.append(str(x))
        print(' '.join(path[::-1]))
else:
    print(-1)
