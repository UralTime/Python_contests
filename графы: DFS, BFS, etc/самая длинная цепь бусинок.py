from collections import deque

n = int(input())
sosedi = [[] for i in range(n + 1)]
for i in range(n - 1):
    k, l = map(int, input().split())
    sosedi[k].append(l)
    sosedi[l].append(k)
if n == 1:
    print(1)
else:
    # BFS от произвольной вершины
    ver = 1
    q = deque()
    dist = [-10 ** 10] * (n + 1)
    dist[ver] = 1
    d = 1
    q.append(ver)
    while q:
        v = q.popleft()
        for u in sosedi[v]:
            if dist[u] == -10 ** 10:
                dist[u] = dist[v] + 1
                d = dist[u]
                q.append(u)
    ver = dist.index(max(dist))
    # BFS от самой дальней вершины
    q = deque()
    dist = [-10 ** 10] * (n + 1)
    dist[ver] = 1
    d = 1
    q.append(ver)
    while q:
        v = q.popleft()
        for u in sosedi[v]:
            if dist[u] == -10 ** 10:
                dist[u] = dist[v] + 1
                d = dist[u]
                q.append(u)
    print(max(dist))
