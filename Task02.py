# Домашнее задание-4
# Задача-2
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def getListMult(x):
    list = []
    listMult = [list.append(i) for i in range(1, x+1) if x % i == 0]
    return list

def primeNum(x):
    primeList = []
    for i in range(2, x):
        while x % i == 0:
            x /= i
            primeList.append(i)
    return primeList

x = int(input("Введите натуральное число: "))
list1 = getListMult(x)
print(f'Множители числа {x} : {list1}')
list2 = primeNum(x)
print(f'Простые множители числа {x} :{list2}')
