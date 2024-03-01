import matplotlib.pyplot as plt

A= "HOLA COMO ESTAN "
B = "MUCHACHO"


LISTA1=[]
LISTA1
LISTA1.append(2)
LISTA1
[2]
LISTA1.append(15)
LISTA1
LISTA1.append("Hola")
LISTA1
LISTA1[2]
print(LISTA1)
print(A+B)
print(4* (A+B))

f=input("ingrese un valor ")
f= int(f)

x=[]
y=[]
# if ((x>0) and (x<2)):
#     print("Usted es un bebe")
# elif((x>=2) and (x<12)):
#     print("Usted es un niño")
# elif((x>=12) and (x<18)):
#     print("Usted es un adolescente")
# elif((x>=18) and (x<25)):
#     print("Usted es un Joven adulto")
# elif((x>=25) and (x<60)):
#     print("Usted es un adulto")
# elif((x>=60)):
#     print("Usted es un adulto mayor")
# else:
#     print("Valor incorrecto")

for i in range(0,f):
    # print(i)
    x.append(i)
    y.append((i**2)+5)
print(x)
print(y)

fig, ax = plt.subplots()
# ax.scatter(x,y)
# ax.plot(x,y)
ax.fill_between(x,y)
plt.show()
