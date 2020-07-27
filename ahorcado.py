import getpass
import time

#palabra_visual = ""

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


	def oculta_palabra(self):
		#global palabra_visual

		letra_oculta = " _"
		self.palabra_visual = ""

		for l in self.palabra:
			self.palabra_visual = self.palabra_visual + letra_oculta
		#print(palabra_visual)
		#self.palabra = self.palabra_visual

	def recoge_letra(self):
		print("\nTurno para " + self.nombre + ": ")
		if len(self.letras_escogidas) >= 1:
			print("\nYa has usado: \n" + str(self.letras_escogidas))
		print("\n" + self.palabra_visual + "\n")
		letra = input("\n" + self.nombre + " introduce una letra: \n").upper()

		self.letras = len(self.palabra)

		if letra == "A":
			self.letras_escogidas.append("Á")
		elif letra == "E":
			self.letras_escogidas.append("É")
		elif letra == "I":
			self.letras_escogidas.append("Í")
		elif letra == "O":
			self.letras_escogidas.append("Ó")
		elif letra == "U":
			self.letras_escogidas.append("Ú")
			self.letras_escogidas.append("Ü")

		self.letras_escogidas.append(letra)
		

		self.palabra_visual = ""
		self.contador = 0

		for l in self.palabra:
			if l in self.letras_escogidas:
				indice = self.letras_escogidas.index(l)
				letra_oculta = " " + self.letras_escogidas[indice]
				self.contador = self.contador + 1
			else:
				letra_oculta = " _"
			self.palabra_visual = self.palabra_visual + letra_oculta

		if letra in self.palabra:
			pass
		else:
			self.errores = self.errores + 1
			print("\nErrores: " + str(self.errores))
		print("contador: " + str(self.contador))

		print("\n" + self.palabra_visual + "\n")
		print("------------------------------------------------")
		time.sleep(2)
	


def main():
	print("Hola y bienvenidos al juego del ahorcado para 2 jugadores.")
	nombre1 = input("Jugador 1, introduce tu nombre: ")
	nombre2 = input("Jugador 2, introduce tu nombre: ")
	palabra1 = getpass.getpass(nombre1 + ", introduce la palabra que deberá adivinar " + nombre2 + ": \n")
	palabra2 = getpass.getpass(nombre2 + ", introduce la palabra que deberá adivinar " + nombre1 + ": \n")
	jugador1 = jugador(nombre1, palabra2, 0)
	#print(str(jugador1.palabra))
	jugador1.oculta_palabra()
	jugador2 = jugador(nombre2, palabra1, 0)
	#print(str(jugador2.palabra))
	jugador2.oculta_palabra()
	#print("Comienza " + jugador1.nombre)
	while jugador1.contador < jugador1.letras and jugador1.errores < 6 or jugador2.contador < jugador2.letras and jugador2.errores < 6:
		if jugador2.contador != jugador2.letras and jugador2.errores < 6:
			jugador1.recoge_letra()
		elif jugador2.contador == jugador2.letras:
			print(jugador2.nombre + " ha ganado.")
			break
		elif jugador2.errores > 5:
			print(jugador2.nombre + " ha fallado demasiado.\nTú ganas.")
			break

		if jugador1.contador != jugador1.letras and jugador1.errores < 6:
			jugador2.recoge_letra()
		elif jugador1.contador == jugador1.letras:
			print(jugador1.nombre + " ha ganado.")
			break
		elif jugador1.errores > 5:
			print(jugador1.nombre + " ha fallado demasiado.\nTú ganas.")
			break

	print("END GAME")



		


if __name__ == '__main__':
	main()

