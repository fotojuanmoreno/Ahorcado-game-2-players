import getpass
import time


class jugador():
	"""docstring for jugador"""
	def __init__(self, nombre, palabra, errores):
		self.nombre = nombre
		self.palabra = palabra.upper()
		self.errores = errores
		self.palabra_visual = ""
		self.contador = 0
		self.letras = 3
		self.letras_escogidas = []
		self.marcador = 0

	def oculta_palabra(self):
		letra_oculta = "_ "
		self.palabra_visual = ""

		for l in self.palabra:
			self.palabra_visual = self.palabra_visual + letra_oculta

	def recoge_letra(self):
		valoresadmitidos = "qweértyuúüiíoópaásdfghjklzxcvbnmQWEÉRTYUÚÜIÍOÓPAÁSDFGHJKLÑZXCVBNM"

		letra = input("Turno para " + self.nombre + ". Introduce una letra: \n").upper()

		if letra in valoresadmitidos and len(letra) == 1:
			pass
		elif letra in valoresadmitidos and len(letra) != 1:
			print("Indroduce una unica letra.")
			while letra not in valoresadmitidos or len(letra) != 1:
				letra = ""
				letra = input("Turno para " + self.nombre + ". Introduce una letra: \n").upper()
		else:
			print("Ese no es un carater valido.")
			while letra not in valoresadmitidos or len(letra) != 1:
				letra = ""
				letra = input("Turno para " + self.nombre + ". Introduce una letra: \n").upper()

		self.letras = len(self.palabra)

		if letra == "A":
			self.letras_escogidas.append("Á")
		elif letra == "Á":
			self.letras_escogidas.append("A")
		elif letra == "E":
			self.letras_escogidas.append("É")
		elif letra == "É":
			self.letras_escogidas.append("E")
		elif letra == "I":
			self.letras_escogidas.append("Í")
		elif letra == "Í":
			self.letras_escogidas.append("I")
		elif letra == "O":
			self.letras_escogidas.append("Ó")
		elif letra == "Ó":
			self.letras_escogidas.append("O")
		elif letra == "U":
			self.letras_escogidas.append("Ú")
			self.letras_escogidas.append("Ü")
		elif letra == "Ú":
			self.letras_escogidas.append("U")
			self.letras_escogidas.append("Ü")
		elif letra == "Ü":
			self.letras_escogidas.append("Ú")
			self.letras_escogidas.append("U")

		self.letras_escogidas.append(letra)

		self.palabra_visual = ""
		self.contador = 0

		for l in self.palabra:
			if l in self.letras_escogidas:
				indice = self.letras_escogidas.index(l)
				letra_oculta =self.letras_escogidas[indice] + " "
				self.contador = self.contador + 1
			else:
				letra_oculta = "_ "
			self.palabra_visual = self.palabra_visual + letra_oculta

		if letra in self.palabra:
			print("\n¡Correcto! " + letra + " está en la palabra.")
		else:
			self.errores = self.errores + 1
			print("\nHas fallado...")

		print("\n------------------------------------------------\n")
		time.sleep(1)
	

	
def estilo(jugador1, jugador2):
	margen_nombre = 40 - len(jugador1.nombre)
	margen_palabra = 40 - len(jugador1.palabra_visual)
	if len(jugador1.letras_escogidas) > 0:
		print(jugador1.nombre + " ya ha utilizado:\n" + str(jugador1.letras_escogidas) + "\nErrores: "+ str(jugador1.errores) + "\n")
	if len(jugador2.letras_escogidas) > 0:
		print(jugador2.nombre + " ya ha utilizado:\n" + str(jugador2.letras_escogidas) + "\nErrores: "+ str(jugador2.errores) + "\n")
	print(" " + jugador1.nombre + " "*margen_nombre + jugador2.nombre)
	print()
	print(" " + jugador1.palabra_visual + " "*margen_palabra + jugador2.palabra_visual + "\n")

def marcador(jugador1, jugador2):
	print("\nMarcador:")
	print(jugador1.nombre + ": " + str(jugador1.marcador))
	print(jugador2.nombre + ": " + str(jugador2.marcador) + "\n")

def eljuego(jugador1, jugador2):
	while jugador1.contador < jugador1.letras and jugador1.errores < 6 or jugador2.contador < jugador2.letras and jugador2.errores < 6:
		
		estilo(jugador1, jugador2)
		if jugador2.contador != jugador2.letras and jugador2.errores < 6:
			jugador1.recoge_letra()
		elif jugador2.contador == jugador2.letras:
			print(jugador2.nombre + " ha ganado.\nLa palabra era: " + jugador2.palabra)
			print("La palabra de " + jugador1.nombre + " era: "+ jugador1.palabra)
			jugador2.marcador = jugador2.marcador + 1
			break
		elif jugador2.errores > 5:
			print(jugador2.nombre + " ha fallado demasiado.\n" + jugador1.nombre + " gana.")
			print("La palabra de " + jugador1.nombre + " era: "+ jugador1.palabra + ".\nLa de " + jugador2.nombre + ": " + jugador2.palabra)
			jugador1.marcador = jugador1.marcador + 1
			break
		
		estilo(jugador1, jugador2)
		if jugador1.contador != jugador1.letras and jugador1.errores < 6:
			jugador2.recoge_letra()
		elif jugador1.contador == jugador1.letras:
			print(jugador1.nombre + " ha ganado.\nLa palabra era: " + jugador1.palabra)
			print("La palabra de " + jugador2.nombre + " era: "+ jugador2.palabra)
			jugador1.marcador = jugador1.marcador + 1
			break
		elif jugador1.errores > 5:
			print(jugador1.nombre + " ha fallado demasiado.\n" + jugador2.nombre + " gana.")
			print("La palabra de " + jugador2.nombre + " era: "+ jugador2.palabra + ".\nLa de " + jugador1.nombre + ": " + jugador1.palabra)
			jugador2.marcador = jugador2.marcador + 1
			break

	repetir = input("¿Hace otra partidita?\nIntroduce y/n: ")

	if repetir != "n":
		marcador(jugador1, jugador2)
		jugador1.errores = 0
		jugador1.palabra_visual = ""
		jugador1.contador = 0
		jugador1.letras = 3
		jugador1.letras_escogidas = []
		jugador1.palabra = getpass.getpass(jugador1.nombre + ", introduce la palabra que deberá adivinar " + jugador2.nombre + ": \n")
		if len(jugador1.palabra) > 20:
			while len(jugador1.palabra) > 20:
				jugador1.palabra=""
				print("Tu palabra es demasiado larga. Prueba otra vez.")
				jugador1.palabra = getpass.getpass(jugador1.nombre + ", introduce la palabra que deberá adivinar " + jugador2.nombre + ": \n")
		elif " " in jugador1.palabra:
			while " " in jugador1.palabra:
				jugador1.palabra=""
				print("No puedes introducir espacios.")
				jugador1.palabra = getpass.getpass(jugador1.nombre + ", introduce la palabra que deberá adivinar " + jugador2.nombre + ": \n")
		jugador1.palabra = jugador1.palabra.upper()
		jugador1.oculta_palabra()
		
		jugador2.errores = 0
		jugador2.palabra_visual = ""
		jugador2.contador = 0
		jugador2.letras = 3
		jugador2.letras_escogidas = []		
		jugador2.palabra = getpass.getpass(jugador2.nombre + ", introduce la palabra que deberá adivinar " + jugador1.nombre + ": \n")
		if len(jugador2.palabra) > 20:
			while len(jugador2.palabra) > 20:
				jugador2.palabra=""
				print("Tu palabra es demasiado larga. Prueba otra vez.")
				jugador2.palabra = getpass.getpass(jugador2.nombre + ", introduce la palabra que deberá adivinar " + jugador1.nombre + ": \n")
		elif " " in jugador2.palabra:
			while " " in jugador2.palabra:
				jugador2.palabra=""
				print("No puedes introducir espacios.")
				jugador2.palabra = getpass.getpass(jugador2.nombre + ", introduce la palabra que deberá adivinar " + jugador1.nombre + ": \n")
		jugador2.palabra = jugador2.palabra.upper()
		jugador2.oculta_palabra()

		eljuego(jugador1, jugador2)

	else:
		print("END GAME")
		time.sleep(2)

def main():
	print("\nHola y bienvenidos al juego del ahorcado para 2 jugadores.\n")

	nombre1 = input("Jugador 1, introduce tu nombre: ")
	nombre2 = input("Jugador 2, introduce tu nombre: ")

	palabra1 = getpass.getpass(nombre1 + ", introduce la palabra que deberá adivinar " + nombre2 + ": \n")
	if len(palabra1) > 20:
		while len(palabra1) > 20:
			palabra1=""
			print("Tu palabra es demasiado larga. Prueba otra vez.")
			palabra1 = getpass.getpass(nombre1 + ", introduce la palabra que deberá adivinar " + nombre2 + ": \n")
	elif " " in palabra1:
		while " " in palabra1:
			palabra1=""
			print("No puedes introducir espacios.")
			palabra1 = getpass.getpass(nombre1 + ", introduce la palabra que deberá adivinar " + nombre2 + ": \n")

	palabra2 = getpass.getpass(nombre2 + ", introduce la palabra que deberá adivinar " + nombre1 + ": \n")
	if len(palabra2) > 20:
		while len(palabra1) > 20:
			palabra2=""
			print("Tu palabra es demasiado larga. Prueba otra vez.")
			palabra2 = getpass.getpass(nombre2 + ", introduce la palabra que deberá adivinar " + nombre1 + ": \n")
	elif " " in palabra2:
		while " " in palabra2:
			palabra2=""
			print("No puedes introducir espacios.")
			palabra2 = getpass.getpass(nombre2 + ", introduce la palabra que deberá adivinar " + nombre1 + ": \n")
	
	jugador1 = jugador(nombre1, palabra2, 0)
	jugador1.oculta_palabra()

	jugador2 = jugador(nombre2, palabra1, 0)
	jugador2.oculta_palabra()

	eljuego(jugador1, jugador2)


if __name__ == '__main__':
	main()
