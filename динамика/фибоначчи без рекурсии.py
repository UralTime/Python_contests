# def fibo(n):  # n-номер требуемого числа фибоначчи
#     a = 1
#     b = 0
#     for i in range(1, n + 1):
#         a, b = b, a + b
#     return b


def fibo(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[n]
