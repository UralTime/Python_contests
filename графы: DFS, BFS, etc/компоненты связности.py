from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(v):
    global used
    global comp
    comp.add(v)
    used[v] = True
    for u in sosedi[v]:
        if not used[u]:
            sosedi[u].remove(v)
            dfs(u)


n, m = map(int, input().split())
sosedi = [set() for i in range(n + 1)]
used = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    sosedi[x].add(y)
    sosedi[y].add(x)
count = 0
components = []
k = -1
for i in range(1, n + 1):
    if not used[i]:
        comp = set()
        dfs(i)
        components.append(0)
        k += 1
        components[k] = (len(comp), comp)
        count += 1
print(count)
for lencomp, comp in components:
    print(lencomp)
    print(*comp)
