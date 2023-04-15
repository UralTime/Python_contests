def dfs(v):
    global can
    global used
    global col
    used[v] = True
    for i in range(len(sosedi[v])):
        u = sosedi[v][i]
        if col[u] == 0:
            col[u] = -col[v]
        elif col[u] == col[v]:
            can = False
        if not used[u]:
            dfs(u)


n, m = map(int, input().split())
used = [False] * (n + 1)
sosedi = [[] for i in range(n + 1)]
col = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    sosedi[x].append(y)
    sosedi[y].append(x)
can = True
for i in range(1, n + 1):
    if not used[i]:
        col[i] = 1
        dfs(i)
if not can:
    print('NO')
else:
    print('YES')
    for i in range(1, n + 1):
        if col[i] == 1:
            print(i)