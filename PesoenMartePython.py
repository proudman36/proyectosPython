def pesoMarte(pes):
	peso_marte=0.279*pes
	return peso_marte

def pesoNeptuno(pes):
	peso_neptuno=1.1*pes
	return peso_neptuno

print("Programa de peso en Marte y Neptuno")

peso=float(input("Ingrese su peso: "))

print(pesoMarte(peso))
print(pesoNeptuno(peso))