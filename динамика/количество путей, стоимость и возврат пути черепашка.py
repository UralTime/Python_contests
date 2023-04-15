# Черепашка, количество путей
zapretset = set()  # вводятся запрещённые клетки
d = [[0] * (m + 1) for i in range(n + 1)]
d[1][1] = 1
for i in range(n):
    for j in range(m):
        if (i, j) not in zapretset:
            d[i][j] = d[i - 1][j] + d[i][j - 1]

# стоимость и возврат пути
# prices считываем в массив c
d = [[-1000000] * (m + 1) for i in range(n + 1)]
d[1][1] = 0
predok = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if d[i - 1][j] < d[i][j - 1]:
            d[i][j] = d[i - 1][j] + c[i][j]
            predok.append('R')
        else:
            d[i][j] = d[i][j - 1] + c[i][j]
            predok.append('D')
print(' '.join(predok))
