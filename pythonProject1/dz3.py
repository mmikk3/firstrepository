#Написать фильтр с лямбда функцией определяющей четное или нечетное число
result=list(filter(lambda x:x%2==0,[90,10,50,77,85,56]))
print(f'Четные числа:',result)
#Сделать список который с функции мап переводит каждое число из списка в строку
num=[1,2,3,4,5,6]
c=list(map(lambda x: print(x), num))
#С помощью функции фильтер отфильтровать из изсходного списка строк только те строки которые являются палиндромами
p=['abcda', 'abccba', 'bkf', 'kjdsh', 'pki', 'okl', 'ikp']
l=list(filter(lambda x:x!=x[::-1],p))
print(list(l))
#Дан словарь, вывести новый словарь,поменяв местами ключи
d = {'alf': 2, 'apdf': 4, 'grrg': 9}
#выражение-генератор
def genf():
    for i in d:
        yield dict({d[i]:i})
c=genf()
print(next(c))
print(next(c))
print(next(c))
#генератор списка
o= [dict({d[i]:i}) for i in d]
print(o)
#Сделать функцию находящую факториал числа
from math import factorial
def func(n):
    n=factorial(n)
    return n
print(func(5))
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
print(factorial_recursive(5))
#Задача на отгадай число
import random
usertry=0
a=0
while usertry<=10:
    a=random.randint(1,10)
    usertry=int(input('введите отгадываемое число'))
    if a==usertry:
        print('вы угадали')
        if str(input('Продолжить !да или !нет'))=='да':
            continue
        else:
            if str(input('Продолжить !да или !нет'))=='нет':
                break
    else:
        print('Не угадали,хотите попробовать еще раз?')
        if str(input('Продолжить !да или !нет')) == 'нет':
            print('программа завершена')
            break


#Декоратор времени затраченного на ф-цию
def my_decorator_time(function):
    def wrapper():
        start=datetime.now()     
        result=function()
        return result
        print(datetime.time()-start)
    return wrapper






