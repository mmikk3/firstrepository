# Задача 1
from math import pow,cos,sin,pi,sqrt,radians
a = 2
b=4
y=(pow(a,2)/3)+((a**2+4)/b)+((a**2+4)**0.5)/4+((a**2+4)**3/2)/4
print(y)
#Задача 2
x=2
y=cos(x)+sin(x)
tg=sin(x)/cos(x)
ctg=cos(x)/sin(x)
print(y,ctg,tg)
#Задача 3
y=pow(x,5)+pow(x,4)+pow(x,3)+pow(x,2)+pow(x,2)+x+1
print(y)
#Задача 4
c=3
y=(0.5*x**2)/a+x
p=(a+b)/(b+(a+c/(b+c)))
m=pow((pow(cos(x**2),2)+pow(sin((2*x)-1),2)),1/3)
print(y,p,m)
#ВТОРАЯ ЧАСТЬ
#Задача по кредиту
s=float(input('Введите сумму займа'))
p=0.2
n=int(input('Введите срок займа'))
m=(s*p*pow(1+p,n))/((pow(1+p,n)-1)*12)
print('Месячная выплата состовляет:',m)
#Задача про планеты
r1=30
r2=50
v1=144000
v2=120000
l1=2*pi*r1*1000000/v1
l2=2*pi*r2*1000000/v2
a=l1>l2
print(cos(radians(180)))