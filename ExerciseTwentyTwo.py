"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
# Задаем длину массива
n = int(input('Введите количество элементов в первом множестве: '))
m = int(input('Введите количество элементов во втором множестве: '))

# 2 действие. Создаем списки
myListOne = list()
myListTwo = list()
countN = 1
countM = 1

while countN <= n:
    element = int(input(f'Введите элемент #{countN}: '))
    myListOne.append(element)
    countN = countN + 1


while countM <= m:
    element = int(input(f'Введите элемент #{countM}: '))
    myListTwo.append(element)
    countM = countM + 1


# 3 действие. Создаем список, чтобы добавить туда повторяющиеся элементы из двух других списков
myList = list()

for i in myListOne:
    for j in myListTwo:
        if i == j:
            myList.append(i)


mySet = set(myList)
myFinish = list(mySet)
myFinish.sort()  # не работает сортировка
print(myFinish)
