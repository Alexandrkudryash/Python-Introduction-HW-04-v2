# Домашнее задание-4
# Задача-4
# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
   koefs.append(randint(1, 100))
# print(koefs)
ans = list()
# print(ans)
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
        # print(ans)
    elif k == 0:
        ans.append(f'{koefs[i]}')
        # print(ans)
    else:
        ans.append(f'{koefs[i]}*x**{k}')
        flag = randint(0, 1)
        # print(ans)
    if flag == 1:
        ans.append('+')
        # print(ans)
    elif flag == 0:
        ans.append('-')
        # print(ans)
    k -= 1

ans.pop(-1)
ans.append('=0')
# print(ans)
# fout = open('Task04-output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()

# if printed all steps:
# Insert equation power: 5
# [50, 63, 74, 49, 44, 99]
# []
# ['50*x**5']
# ['50*x**5', '-']
# ['50*x**5', '-', '63*x**4']
# ['50*x**5', '-', '63*x**4', '+']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-', '44*x']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-', '44*x', '-']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-', '44*x', '-', '99']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-', '44*x', '-', '99', '-']
# ['50*x**5', '-', '63*x**4', '+', '74*x**3', '+', '49*x**2', '-', '44*x', '-', '99', '=0']
