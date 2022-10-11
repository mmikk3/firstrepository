#Узнать простое число или нет при помощи рекурсии
a = 3
def recursive(x,y=None):
    if y==None:
        y=x-1
    while y>=2:
        if x%y==0:
            print('число не явл простым')
            return False
        else:
            return recursive(x,y-1)
    else:
        print('число явля простым')


recursive(a)
#Найти НОД при помощи рекурсии
def nod(x,y):
    if y==0:
        return x
    else:
        return nod(y,x%y)

nod(10,15)
print(nod(10,15))
#Перевести из 10-ой системы в двоичную
k = []
def dvoi(n):
    if n==0:
        return k
    k.append(n%2)
    dvoi(n//2)
dvoi(1234)
k.reverse()
print(k)