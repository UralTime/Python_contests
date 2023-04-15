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
index = [-1] * n
for i in range(n):
    q = binsearch_left(d, a[i])
    d[q] = a[i]
    index[q] = i
    if q > 0:
        predok[i] = index[q - 1]
try:
    j = d.index(10 ** 16)
except ValueError:
    j = len(d)
# print(j) длина НВП
pos = index[index.index(-1) - 1]
ans = []
while predok[pos] != -1:
    ans.append(str(a[pos]))
    pos = predok[pos]
ans.append(str(a[pos]))
print(' '.join(ans[::-1]))
