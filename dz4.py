# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:59:52 2023

@author: user
"""
"""
list_1=[]
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)
"""
    
    
"""Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями).
 Выдать без повторений в порядке возрастания все те числа, которые встречаются 
 в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
 m — кол-во элементов второго множества.
 Затем пользователь вводит сами элементы множеств.
 """
"""
def MakeList():
    n = int(input(print("введи размер списка= ")))
    name=[]
    for i in range(n):
        elem=int(input(print("введи элемент ", i ," =")))
        name.append(elem)
    return name
 
 
# n = input(print("введи n= "))
# n= int(n)
# set_1=[]
# for i in range(n):
#     elem=input(print("введи элемент ", i ," ="))
#     set_1.append(elem)

# m = input(print("введи m= "))
# m2= int(m)
# set_2=[]
# for i in range(m):
#     elem=input(print("введи элемент ", i ," ="))
#     set_2.append(elem)


list_1=MakeList()
print(list_1)
list_2=MakeList()
print(list_2)

list_ad=list()
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            list_ad.append(list_2[j])
        #else: print(i," ", j)
print(list_ad)

for i in range(len(list_ad)):
    for j in range(len(list_ad[j+1:])):
        if list_ad[i] >= list_ad[j]:
            ad = list_ad[j]
            list_ad[j] = list_ad[i]
            list_ad[i] = ad    

print(list_ad)   

set_sort=set(list_ad)
print(set_sort) 
"""       


'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке
растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
'''
from random import randrange
n= int(input(print('N= ')))
max_berry= int(input(print('max_berry= ')))
list_1=list()
for i in range(n):
    list_1.append(randrange(max_berry+1))
print(list_1)

list_summ=list()
for i in range(len(list_1)):
    if i+1==n:
        list_summ.append(list_1[i-1]+list_1[i]+list_1[0])
    else:
        list_summ.append(list_1[i-1]+list_1[i]+list_1[i+1])
print(list_summ)

S=list_summ[0]
for i in range(len(list_summ)):
    if S< list_summ[i]:
        S=list_summ[i]
print('Максимальное число ягод с одного хода =',S)
        