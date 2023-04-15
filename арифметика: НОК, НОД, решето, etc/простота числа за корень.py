# Простота числа за корень
n = int(input())
i = 2
isPrime = True
while i*i<=n:
    if n%i==0:
        isPrime = False
    i+=1
print('prime' if isPrime else 'composite')