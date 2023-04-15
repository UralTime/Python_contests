fib = [0] * 50
fib[1] = 1
n = int(input())
for i in range(2, n + 2):
    fib[i] = fib[i - 2] + fib[i - 1]
print(fib[n+1])
