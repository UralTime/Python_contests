n = int(input())
word = [[0] * (n + 1) for i in range(4)]
word[1][1] = 1
word[2][1] = 1
word[3][1] = 1
for i in range(2, n + 1):
    word[1][i] = word[2][i - 1] + word[3][i - 1]
    word[2][i] = word[1][i - 1] + word[2][i - 1] + word[3][i - 1]
    word[3][i] = word[1][i - 1] + word[3][i - 1] + word[3][i - 1]
print(word[1][n] + word[2][n] + word[3][n])
