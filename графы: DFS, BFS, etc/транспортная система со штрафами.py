from collections import deque


def bfs(ver, punkt):
    dist = [10 ** 10] * (n + 1)
    dist[ver] = 0
    q = deque()
    q.appendleft(ver)
    while q:
        v = q.popleft()
        for u in sosedi[v]:
            if dist[u] >= dist[v] + 1:
                if u in ways[v]:
                    dist[u] = dist[v]
                    if u not in q:
                        q.appendleft(u)
                else:
                    dist[u] = dist[v] + 1
                    if u not in q:
                        q.append(u)
    return dist[punkt]


n, m = map(int, input().split())
sosedi = [set() for i in range(n + 1)]
ways = [set() for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    if x != y:
        sosedi[x].add(y)
        ways[x].add(y)
        sosedi[y].add(x)
k = int(input())
answer = []
for j in range(k):
    l, r = map(int, input().split())
    way = bfs(l, r)
    if way == 10 ** 10:
        answer.append('-1')
    else:
        answer.append(str(way))
print('\n'.join(answer))
