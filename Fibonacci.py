conta0=0
conta1=1
conta2=1
num=int(input("Escriba un número entero por favor "))
while num<0:
    print("Ingrese un número del 0 en adelante.")
    num=input("Escriba un número entero por favor ")
if num==0:
    print(num)
elif num==1:
    print(conta0)
    print(num)
else:
    print(conta0)
    print(conta1)
    print(conta1)
    for i  in range(num-2):
        conta1+=conta2
        conta2=conta1-conta2
        print(conta1)