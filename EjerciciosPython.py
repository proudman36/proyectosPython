def numeroPrimo(num):
	if num==1:
		mensaje="El número no es primo"
	elif num==2:
		mensaje="El número es primo"
	else:
		for i in range(2,num):
			residuo=num%i
			if residuo==0:
				mensaje="El número no es primo"
				break
			else:
				mensaje="El número es primo"
	return mensaje


def numPrim(num):
	primo=True
	if num==1:
		primo=False
	elif num==2:
		primo=True
	else:
		for i in range(2,num):
			residuo=num%i
			if residuo==0:
				primo=False
				break
	if primo==True:
		mensaje="El número es primo"
	elif primo==False:
		mensaje="El número no es primo"
	return mensaje

print(numPrim(int(input("Escribe un número: "))))


