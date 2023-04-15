n, m = map(int, input().split())
price = [[0] * (m + 1) for i in range(n + 1)]
price[0] = [10 ** 10] * (m + 1)
for i in range(n + 1):
    price[i][0] = 10 ** 10
c = [0] * (n + 1)
for i in range(1, n + 1):
    c[i] = [int(elem) for elem in input().split()]
    c[i].append(0)
    c[i][1:] = c[i][:m]
price[1][1] = c[1][1]
for k in range(1, n + 1):
    for j in range(1, m + 1):
        if not (k == 1 and j == 1):
            price[k][j] = min(price[k - 1][j], price[k][j - 1]) + c[k][j]
print(price[n][m])
