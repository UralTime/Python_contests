n = int(input())

answer = 0
if n % 2 != 0 and n!=1:
    answer += 1
while n > 1:
    n = n // 2
    answer += 1
print(answer)
