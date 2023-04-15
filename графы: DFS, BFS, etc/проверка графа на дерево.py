def dfs(v):
    global used
    global tree
    used[v] = True
    for u in sosedi[v]:
        if not used[u]:
            sosedi[u].remove(v)
            dfs(u)
        else:
            tree = False


n, m = map(int, input().split())
sosedi = [set() for i in range(n + 1)]
used = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    sosedi[x].add(y)
    sosedi[y].add(x)
if n != m + 1:
    print('NO')
else:
    tree = True
    for i in range(1, n + 1):
        if not used[i]:
            dfs(i)
    if tree:
        print('YES')
    else:
        print('NO')
