# d[i][j]-ответ на задачу на префиксе для i элемента для рюкзака вместимостью j килограмм
n, m = map(int, input().split())
v = [0] + [int(elem) for elem in input().split()]
c = [0] + [int(elem) for elem in input().split()]
d = [[-10 ** 10] * (m + 1) for i in range(n + 1)]
for i in range(n + 1):
    d[i][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j - v[i] >= 0:
            d[i][j] = max(d[i - 1][j - v[i]] + c[i], d[i - 1][j])
        else:
            d[i][j] = d[i - 1][j]
print(max(d[n]))
