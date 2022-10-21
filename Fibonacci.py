cont0=0
cont1=1
cont2=1
num = int(input("Ingrese un número entero por favor. "))
while num<0:
    print("Ingrese un número del 0 en adelante")
    num = print("Ingrese un número entero por favor. ")
if num==0:
    print(num)
elif num == 1:
    print(cont0)
    print(num)
else:
    print(cont0)
    print(cont1)
    print(cont2)
    for i in range(num-2):
        cont1+=cont2
        cont2=cont1-cont2
        print(cont1)