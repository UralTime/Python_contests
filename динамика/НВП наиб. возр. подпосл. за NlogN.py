# d[i]-минимальный элемент, на который оканчивается возрастающая последовательность длиной i
# идём по последовательности и кладём число в первую позицию, где число больше него
# позицию определяем левым бинпоиском
# ответ - индекс последнего элемента-не бесконечности
# когда обновляем - храним в отдельном массиве для каждого числа предка
def binsearch_left(a, toFind):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] < toFind:
            left = middle
        else:
            right = middle
    return right


n, a1, k, b, m = [int(elem) for elem in input().split()]
a = [a1]
for i in range(1, n):
    a.append((k * a[i - 1] + b) % m)
d = [10 ** 16] * n
predok = [-1] * n
for i in range(n):
    q = binsearch_left(d, a[i])
    d[q] = a[i]
    if q > 0:
        predok[i] = a.index(d[q - 1])
j = d.index(10 ** 16)
print(j)
pos = a.index(d[j - 1])
ans = []
while predok[pos] != -1:
    ans.append(str(a[pos]))
    pos = predok[pos]
ans.append(str(a[pos]))
print(' '.join(ans[::-1]))
