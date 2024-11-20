n = int(input('Число: '))
result = 0
for i in range(1, 20):
    for j in range(i + 1, 20):
        if n % (j + i) == 0:
            result = str(result) + str(i) + str(j)


print('Пароль:',int(result))
