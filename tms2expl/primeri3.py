from math import log,cos,sin,e,pi
#Первый пример 1
x= 0.6
step=0.25
while x<=1.1:
    #TODO:logic
    for n in range(10,16):
        summa=0
        for k in range(1,n+1):
            summa+=(log(abs(x+k))**2)*(cos((k+(sin(x))**(1/5)))/(k*x))
        res=(1/45)*(3**(x+n))**(1/2)*summa
        print(f'{x=} {n=} {res=}')
    x+=step
#Второй пример 2
x=0.6
step=0.25
while x<=1.1:
    for n in range(10,16):
        summa=0
        for k in range(1,n+1):
            summa+=((x**((k+1)/k)+(e**((k-3)/k)))**0.5)/(1+log(x))
        res=sin(pi*n/(x+3))*summa
        print(f'{x=} {n=} {res=}')
    x+= step
#Пример 3
x=0.6
step=0.25
while x<=1.1:
    for n in range(10,16):
        summa=0
        for k in range(1,n+1):
            summa+=(1+(k+1)/n)/(e**k*(x**((k-1)/2))+log(x))
        res=((sin(x/n))**3/2)*summa
        print(f'{x=} {n=} {res=}')
    x+= step
#Пример 4
x=0.6
step=0.25
while x<=1.1:
    for n in range(10,16):
        summa=0
        for k in range(1,n+1):
            summa+=sin((k-1)/(k+1))**2+e**((x/k)**0.5)
        res=pi/((x**3/2)+3/(x+5))*summa
        print(f'{x=} {n=} {res=}')
    x+= step
