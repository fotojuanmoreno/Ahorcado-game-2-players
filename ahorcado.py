import getpass
import time
from textblob import TextBlob


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

	def pide_palabra(self, nombre1, nombre2):
		self.palabra = getpass.getpass(nombre1+ ", introduce la palabra que deberá adivinar " + nombre2 + ": \n").upper()
		idioma = TextBlob(self.palabra)
		idioma = idioma.detect_language()
		if idioma != "es":
			self.palabra = ""
			print("Utiliza solo palabras en español.")
			self.pide_palabra(nombre1, nombre2)
		if len(self.palabra) > 20:
			while len(self.palabra) > 20:
				self.palabra = ""
				print("Tu palabra es demasiado larga. Prueba otra vez.")
				self.pide_palabra(nombre1, nombre2)
		elif " " in self.palabra:
			while " " in self.palabra:
				self.palabra=""
				print("No puedes introducir espacios.")
				self.pide_palabra(nombre1, nombre2)
	def reset(self):
		self.palabra = ""
		self.errores = 0
		self.palabra_visual = ""
		self.contador = 0
		self.letras = 3
		self.letras_escogidas = []

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
		jugador1.reset()
		jugador2.reset()
		jugador2.pide_palabra(jugador1.nombre, jugador2.nombre)
		jugador1.oculta_palabra()
		jugador1.pide_palabra(jugador2.nombre, jugador1.nombre)
		jugador2.oculta_palabra()

		eljuego(jugador1, jugador2)

	else:
		print("END GAME")
		time.sleep(2)


def main():

	print("\nHola y bienvenidos al juego del ahorcado para 2 jugadores.\n")

	nombre1 = input("Jugador 1, introduce tu nombre: ")
	jugador1 = jugador(nombre1, "", 0)
	nombre2 = input("Jugador 2, introduce tu nombre: ")
	jugador2 = jugador(nombre2, "", 0)

	jugador2.pide_palabra(jugador1.nombre, jugador2.nombre)
	jugador1.pide_palabra(jugador2.nombre, jugador1.nombre)
	jugador1.oculta_palabra()
	jugador2.oculta_palabra()

	eljuego(jugador1, jugador2)


if __name__ == '__main__':
	main()