def cubeRoot(n):
    for i in range(0, 11):
        if i * i * i == n:
            return i


cubes = set()
for i in range(0, 11):
    cubes.add(i * i * i)
n = int(input())
for elem in cubes:
    second = n - elem
    if second in cubes:
        print(cubeRoot(elem), cubeRoot(second))
        break
else:
    print('impossible')
