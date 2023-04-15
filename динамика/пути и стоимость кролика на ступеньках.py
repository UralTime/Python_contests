# кролик: варианты путей до n-ой ступеньки
ways = [0] * (n + 1)
ways[1] = 1
ways[2] = 2
for i in range(3, n + 1):
    ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
print(ways[n])

# кролик: стоимость поднятся до n-ой ступеньки от 0-ой, где за подъём на i-ую ступеньку платится c[i]
price = [0] * (n + 1)
price[1] = c[1]
for i in range(2, n + 1):
    price[i] = min(price[i - 2], price[i - 1]) + c[i]
print(price[n])

# восстановление пути кузнечика, который прыгает с нуля до n
i = n
path = []
while i > 1:
    path.append(i)
    if d[i - 1] > f[i - 2]:
        i = i - 1
    else:
        i = i - 2
path.append(0)
print(path[::-1])
