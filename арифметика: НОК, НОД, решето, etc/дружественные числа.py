def sumdels(n):
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
    return sum + 1


oldSd = set()
k = int(input())
for i in range(1, k + 1):
    sd = sumdels(i)
    if sumdels(sd) == i:
        if i != sd and i not in oldSd and sd <= k:
            print(i, sd)
            oldSd.add(sd)
