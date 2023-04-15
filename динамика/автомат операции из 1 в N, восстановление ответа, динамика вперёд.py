# неправильное решение, правильное смотри в 'калькулятор, восстановление ответа' динамикой назад
n = int(input())
oper = [10 ** 6] * (n + 2)
predok = [0] * (n + 2)
oper[1] = 0
for i in range(1, n + 1):
    if oper[i] + 1 < oper[i + 1]:
        oper[i + 1] = oper[i] + 1
        predok[i + 1] = i
    if i * 2 < n + 1 and oper[i] * 2 < oper[i * 2]:
        oper[i * 2] = oper[i] + 1
        predok[i * 2] = i
    if i * 3 < n + 1 and oper[i] * 3 < oper[i * 3]:
        oper[i * 3] = oper[i] + 1
        predok[i * 3] = i
# print(oper[n])
path = []
j = n
while j > 1:
    if j - predok[j] == 1:
        path.append('1')
    elif j // predok[j] == 2 and j % predok[j] == 0:
        path.append('2')
    else:
        path.append('3')
    j = predok[j]
print(''.join(path[::-1]))
