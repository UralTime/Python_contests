n = int(input())
x = [0] + [int(elem) for elem in input().split()]
x.sort()
d = [10 ** 10] * (n + 1)
d[1] = 10 ** 10
d[2] = x[2] - x[1]
for i in range(3, n + 1):
    d[i] = min(d[i - 1], d[i - 2]) + x[i] - x[i - 1]
print(d[n])
