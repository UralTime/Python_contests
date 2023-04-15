n, a1, k, b, m = map(int, input().split())
a = [0, a1]
for i in range(2, n + 1):
    a.append((k * a[i - 1] + b) % m)
d = [1] * (n + 1)
for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        if a[j] < a[i]:
            d[i] = max(d[j] + 1, d[i])
print(max(d))
