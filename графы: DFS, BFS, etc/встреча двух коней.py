from collections import deque

redhorse, greenhorse = input().split()
redletter, redi = redhorse[0], int(redhorse[1]) - 1
greenletter, greeni = greenhorse[0], int(greenhorse[1]) - 1
redj = ord(redletter) - ord('a')
greenj = ord(greenletter) - ord('a')
INF = 10 ** 5
dist = [[INF] * 8 for i in range(8)]
used = [[0] * 8 for i in range(8)]
dist[redi][redj] = 0
used[redi][redj] = 1
dist[greeni][greenj] = 0
used[greeni][greenj] = 2
q = deque()
q.append((redi, redj))
q.append((greeni, greenj))
isanswer = False
answer = set()
while q and not isanswer:
    x, y = q.popleft()
    for v, u in [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2), (x + 1, y - 2), (x + 1, y + 2),
                 (x + 2, y - 1), (x + 2, y + 1)]:
        if 0 <= v < 8 and 0 <= u < 8:
            if used[v][u] == 0:
                used[v][u] = used[x][y]
                dist[v][u] = dist[x][y] + 1
                q.append((v, u))
            elif used[v][u] != used[x][y]:
                if dist[v][u] == dist[x][y] + 1:
                    dist[v][u] = dist[x][y] + 1
                    isanswer = True
                    answer.add(dist[v][u])
if not isanswer:
    print(-1)
else:
    print(min(answer))
