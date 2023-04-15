price = [0] * 101
n = int(input())
c = [0]
for elem in input().split():
    c.append(int(elem))
price[1] = c[1]
for i in range(2, n + 1):
    price[i] = min(price[i - 2], price[i - 1]) + c[i]
print(price[n])
