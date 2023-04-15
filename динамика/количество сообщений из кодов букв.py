s = input()
d = [1] * (len(s))
zan = 0
for i in range(len(s) - 1):
    if s[i] not in '123':
        d[i + 1] = d[i]
        zan = 0
    else:
        if s[i] != '3' or s[i + 1] in '0123':
            d[i + 1] = (d[i] - zan) * 2 + zan
            zan = d[i] - zan
        else:
            d[i + 1] = d[i]
            zan = 0
print(d[len(s) - 1])
