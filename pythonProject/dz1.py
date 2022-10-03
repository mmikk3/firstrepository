#Первая задача 1 вычисления
a=3
b=10
c=15
print (a+b+c,a-b+c,(a+b)//c,a*b%c,(a**b/2)-c*3,sep=', ')
#Вторая задача 2 треугольник
a=2
b=4
c=pow(a**2+b**2,1/2)
s=1/2*a*b
print(c,s,sep=', ')
#Третья задача 3 шнурки
a=5
b=4
l=3
N=8
c1=N-1
c2=N-2
L=(c1*N)+(c2*N)+2*l
print(L)
# Задача на строки 1
a = ('hello world test1 test2')
b = a.count(' ')
print(b + 1)
# Задача на строки 2
c = ('a1b2c3d4e5f6')
print(c[2], c[-2], c[0:5], c[:-2], c[0::2], c[1::2], c[::-1], c[-1::-2], len(c), sep='\n')
# Задача 3
a= ('HhhhHHHhhhhHHHHhH')
b=a.replace(h,H)
print(b)