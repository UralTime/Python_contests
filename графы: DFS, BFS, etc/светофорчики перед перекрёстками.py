n, m = map(int, input().split())
sosedi = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    sosedi[x].append(y)
    sosedi[y].append(x)
for k in range(1, n + 1):
    print(len(sosedi[k]), end=' ')
