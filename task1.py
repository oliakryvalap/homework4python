#Даны два неупорядоченных набора целых чисел (может быть, 
#с повторениями). Выдать без повторений в порядке возрастания 
#все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
#Наборы (списки) чисел можно считать заданными и не вводить с 
#клавиатуры

#Примеры/Тесты:
#Input1: 2 4 6 8 10 12 10 8 6 4 2
#Input2: 3 6 9 12 15 18
#Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#Input1: 2 4 6 8 10 10 8 6 4 2
#Input2: 3 9 12 15 18
#Output: Повторяющихся чисел нет
#set1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
#set2 = [3, 9, 12, 15, 10]

from random import randint
n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(s_set)