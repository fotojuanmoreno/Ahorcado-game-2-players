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

		letra_oculta = "_ "
		self.palabra_visual = ""

		for l in self.palabra:
			self.palabra_visual = self.palabra_visual + letra_oculta
		#print(palabra_visual)
		#self.palabra = self.palabra_visual

	def recoge_letra(self):
		#print("\nTurno para " + self.nombre + ": ")
		#if len(self.letras_escogidas) >= 1:
			#print("\nYa has usado: \n" + str(self.letras_escogidas))
		#print("\n" + self.palabra_visual + "\n")
		letra = input("Turno para " + self.nombre + ". Introduce una letra: \n").upper()

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
			#print("\nErrores: " + str(self.errores))
		#print("contador: " + str(self.contador))

		#print("\n" + self.palabra_visual + "\n")
		print("------------------------------------------------\n")
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
	#print(str(jugador1.palabra))
	jugador1.oculta_palabra()
	jugador2 = jugador(nombre2, palabra1, 0)
	#print(str(jugador2.palabra))
	jugador2.oculta_palabra()
	#print("Comienza " + jugador1.nombre)
	while jugador1.contador < jugador1.letras and jugador1.errores < 6 or jugador2.contador < jugador2.letras and jugador2.errores < 6:
		estilo(jugador1, jugador2)
		if jugador2.contador != jugador2.letras and jugador2.errores < 6:
			jugador1.recoge_letra()
		elif jugador2.contador == jugador2.letras:
			print(jugador2.nombre + " ha ganado.")
			break
		elif jugador2.errores > 5:
			print(jugador2.nombre + " ha fallado demasiado.\nTú ganas.")
			break
		estilo(jugador1, jugador2)
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

