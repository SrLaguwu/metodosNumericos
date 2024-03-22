import matplotlib.pyplot as plt
import math as mt

a=-10
b=3  # tambien se puede con 2.5 para ver un grafica diferente
h=0.1 #saltos
#espacio para incluir la funcion a graficar
def f(xx):
    yy=5*((mt.sin(xx))) - mt.exp(xx)
    return yy

x = []
y = []
i = 0
n = (b-a)/h

while (i<=n):
    x.append(a+(h*i))
    y.append(f(x[i]))
    i=i+1

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()
