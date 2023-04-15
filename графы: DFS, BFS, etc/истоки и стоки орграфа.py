n = int(input())
a = [0] * (n + 1)
stocks = []
istoks = []
for i in range(1, n + 1):
    a[i] = [0] + [int(elem) for elem in input().split()]
    if a[i] == [0] * (n + 1):
        stocks.append(i)
for j in range(1, n + 1):
    ist = True
    for i in range(1, n + 1):
        if a[i][j] != 0:
            ist = False
    if ist:
        istoks.append(j)
print(len(istoks))
print('\n'.join([str(i) for i in istoks]))
print(len(stocks))
print('\n'.join([str(i) for i in stocks]))
