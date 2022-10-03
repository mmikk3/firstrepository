import math
from math import factorial
summa=0
n=1
part_4=1
eps=0.0001
x=3
while abs(part_4)>eps:
    part_4=(x**n)/factorial(n)
    summa+=part_4
    n+=1
print(summa)
#Пример 5
part_5=1
summa=0
x=0.5
n=1
while abs(part_5)>10:
    part_5=((-1)**(n+1))*(x**n)/n
    summa+=part_5
    n+=1
print(summa)
#Пример 3
part_3=0
summa=0
x=0.4
k=0
m=0.5
while abs(part_3)>eps:
    part_3=((m**k)*math.log(1+x,k))/math.factorial(k)
    summa+=part_3
    n+=1
print(summa)

