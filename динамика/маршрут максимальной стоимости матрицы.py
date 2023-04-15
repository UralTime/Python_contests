n, m = map(int, input().split())
price = [[0] * (m + 1) for i in range(n + 1)]
price[0] = [-10 ** 10] * (m + 1)
for i in range(n + 1):
    price[i][0] = -10 ** 10
c = [0] * (n + 1)
for i in range(1, n + 1):
    c[i] = [int(elem) for elem in input().split()]
    c[i].append(0)
    c[i][1:] = c[i][:m]
price[1][1] = c[1][1]
predok = [[0, 0] * (m + 1) for i in range(n + 1)]
for k in range(1, n + 1):
    for j in range(1, m + 1):
        if not (k == 1 and j == 1):
            if price[k - 1][j] > price[k][j - 1]:
                predok[k][j] = (k - 1, j)
                price[k][j] = price[k - 1][j] + c[k][j]
            else:
                price[k][j] = price[k][j - 1] + c[k][j]
                predok[k][j] = (k, j - 1)
print(price[n][m])
i = n
j = m
path = []
while i > 1 or j > 1:
    if predok[i][j] == (i - 1, j):
        path.append('D')
    else:
        path.append('R')
    i, j = predok[i][j]
print(' '.join(path[::-1]))
