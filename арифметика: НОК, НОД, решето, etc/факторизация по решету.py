def Factorization_Resheto(N):
    global a
    a = [-1]*(N+1)
    i = 2
    while i*i <= N:
        if a[i]:
            for j in range(i*i, N + 1, i):
                a[j] = i
        i+=1

Factorization_Resheto(100)#10000000
x = int(input())
while a[x]!=-1:
    print(a[x])
    x/=a[x]
print(x)