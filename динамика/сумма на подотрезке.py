# d[i] - префиксная сумма
a = [int(elem) for elem in input().split()]
d[-1] = 0
for i in range(len(a)):
    d[i] = d[i - 1] + a[i]
l, r = map(int, input().split())
print(d[r] - d[l - 1])

# сумма на матрице
d[i][j] = a[i][j] - d[i][0] - d[0][j] + d[0][0]
