# логарифм введённого числа по основанию 2 с округлением вверх
n = int(input())
b = ''
answer = 0
while n > 0:
    b = str(n % 2) + b
    n = n // 2
if b.count('1') == 1:
    answer -= 1
print(answer + len(b))
