# Вывести все делители числа, кроме единицы и его самого
#Вывести сумму всех делителей + 1
for n in range(1,40):
    i = 2
    sum = 0
    dels = []
    while i * i <= n:
        if n % i == 0:
            dels.append(i)
            sum += i
        i += 1
    if len(dels) != 0:
        pos = len(dels) - 1
        if dels[pos] == n ** 0.5:
            pos -= 1
        for j in range(pos, -1, -1):
            dels.append(n // dels[j])
            sum += n // dels[j]
    print(sum)
    ##for elem in dels:
    ##   print(elem, end=' ')
# print(sum+1)