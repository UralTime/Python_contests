n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
c = [0] * (n + 1)
a[1], b[1], c[1] = [int(elem) for elem in input().split()]
d = [0] * (n + 1)
d[1] = a[1]
if n >= 2:
    a[2], b[2], c[2] = [int(elem) for elem in input().split()]
    d[2] = min(d[1] + a[2], b[1])
for i in range(3, n + 1):
    a[i], b[i], c[i] = [int(elem) for elem in input().split()]
    d[i] = min(d[i - 1] + a[i], d[i - 2] + b[i - 1], d[i - 3] + c[i - 2])
print(d[n])
