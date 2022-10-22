itera=True

while itera==True:
	print("Bienvenido a la isla. Tu misión será encontrar el tesoro.")
	print("Estás en un sendero y encuentras dos caminos.")
	camino = input("Izquierda o derecha ")
	caminoMin = camino.lower()
	if caminoMin == "derecha":
		print("Caíste en un agujero. Game Over")
		continua= input("¿Continuar? ")
		continuaMin=continua.lower()
		if continuaMin=="no":
			print("Gracias por jugar.")
			exit(0)
		elif continuaMin=="si":
			continue
	elif caminoMin == "izquierda":
		print("Llegas a una zona volcánica")
		subir = input("¿Tomas otro camino o subes al volcán? (Contestar con: otro o subir) ")
		subirMin=subir.lower()
		if subirMin == "otro":
			print("Caes en un barranco. Game Over")
			continua= input("¿Continuar?" )
			continuaMin=continua.lower()
			if continuaMin=="no":
				print("Gracias por jugar.")
				exit(0)
			elif continuaMin=="si":
				continue
		elif subirMin == "subir":
			print("Llegas al volcán")
			quedarse = input("Te quedas o decides seguir tu camino. (Contestar con: quedarse o seguir) ")
			quedarseMin=quedarse.lower()
			if quedarseMin == "quedarse":
				print("El volcán hace erupción. Game Over.")
				continua = input("¿Continuar?" )
				continuaMin=continua.lower()
				if continuaMin == "no":
					print("Gracias por jugar.")
					exit(0)
				elif continuaMin == "si":
					continue
			elif quedarseMin == "seguir":
				print("Te topas con un aldeano")
				aldeano = input("¿Lo atacas, hablas o comercias con él? (Responde: atacar, hablar o comerciar) ")
				aldeanoMin=aldeano.lower()
				if aldeanoMin == "atacar":
					print("Te ataca con una espada. Game Over.")
					continua=input("¿Continuar?")
					continuaMin=continua.lower()
					if continuaMin=="no":
						print("Gracias por jugar.")
						exit(0)
					elif continuaMin=="si":
						continue
				elif aldeanoMin == "comerciar":
					print("El aldeano te cambia un rubí por tu camisa.")
					rubi=True
				if aldeanoMin == "hablar" or aldeanoMin=="comerciar":
					print("Te dice que hay un lago cerca.")
					if aldeanoMin=="hablar":
						rubi=False
					print("Caminas hasta el lago")
					nadar=input("¿Nadar o esperar? ")
					nadarMin=nadar.lower()
					if nadarMin=="nadar":
						print("Atacado por una tribu. Game Over")
						continua=input("¿Continuar? ")
						continuaMin=continua.lower()
						if continuaMin == "no":
							print("Gracias por jugar.")
							exit(0)
						elif continuaMin == "si":
							continue
					elif nadarMin=="esperar":
						print("Encuentras una tienda")
						if rubi==True:
							print("Compras un set completo de pirata y te pones una nueva camisa")
						print("Te das cuenta de que al lado hay una casa")
						puerta = input("¿Cuál puerta: roja, azul o amarilla? ")
						if puerta=="roja":
							print("Eres quemado. Game Over")
							continua=input("¿Continuar? ")
							continuaMin=continua.lower()
							if continuaMin =="no":
								print("Gracias por jugar")
								exit(0)
							elif continuaMin == "si":
								continue
						elif puerta == "azul":
							print("Devorado por bestias. Game Over")
							continua=input("¿Continuar? ")
							continuaMin=continua.lower()
							if continuaMin=="no":
								print("Gracias por jugar")
								exit(0)
							elif continuaMin == "si":
								continue
						elif puerta == "amarilla":
							print("¡Has ganado!")
							exit(0)
						else: 
							print("Game Over")
							continua=input("¿Continuar? ")
							continuaMin=continua.lower()
							if continuaMin=="no":
								print("Gracias por jugar.")
								exit(0)
							elif continuaMin=="si":
								continue










