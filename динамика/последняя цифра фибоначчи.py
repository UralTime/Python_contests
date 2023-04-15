n = int(input())
fib = [0] * (n + 2)
fib[1] = 1
for i in range(2, n + 2):
    fib[i] = fib[i - 1] % 10 + fib[i - 2] % 10
print(fib[n + 1] % 10)
