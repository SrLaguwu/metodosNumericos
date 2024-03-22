import math as mt

a=-5 # elemento de entrada
b=-2  # elemento de entrada


# funcion : 5sen(x)-e(elevado a la x)
def f(xx):
    yy=5*((mt.sin(xx))) - mt.exp(xx)
    return yy

Es =0.05 #tolerancia
Ea = 1 #error aproximado inicial
c = []
i = 0


while (Es<Ea):
    m=(a+b)/2
    c.append(m)
    if (f(c[-1]) == 0 ):
        Ea = 0
    else:
        if((f(a))*(f(c[-1]))<0):
            b = c[-1]
        else:
            a = c[-1]

    if(i>0):
        Ea = 100 * abs(((c[-1]-c[-2])/c[-1]))

    i=i+1

print("La raiz es: ", str(c[-1]), " con un error de: ", str(Ea))
