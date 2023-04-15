# последовательность 5 10 -6 2 0
# подотрезок - набор подряд идущих элементов из последовательности 5 10 -6 2
# подпоследовательность - набор элементов из последовательности в том же порядке 5 -6 2

# наибольшая возрастающая подпоследовательность за N**2
# d[i] - длина НВП на преф.длиной i, включая i
n, a1, k, b, m = [int(elem) for elem in input().split()]
a = [10000000, a1]
for i in range(2, n + 1):
    a.append((k * a[i - 1] + b) % m)
d = [1] * (n + 1)
for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        if a[j] < a[i] and d[j] >= d[i]:
            d[i] = d[j] + 1
print(max(d))
pos = d.index(max(d))
ans = [a[pos]]
for i in range(pos - 1, 0, -1):
    if d[i] == d[pos] - 1 and a[i] < a[pos]:
        ans.append(str(a[i]))
        pos = i
print(ans[::-1])
