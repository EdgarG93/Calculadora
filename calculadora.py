#Funciones
def suma(n1, n2):
	print(f'Resultado: {n1+ n2}\n')
	
def resta(n1, n2):
	print(f'Resultado: {n1- n2}\n')
	
def multiplicacion(n1, n2):
	print(f'Resultado: {n1* n2}\n')
	
def division(n1, n2):
	try:
		print(f'Resultado es: {n1/ n2}\n')
	except ZeroDivisionError:
		print(f'Resultado es: Indefinido\n')

while True:	

	print(f'Bienvenido a la Calculadora')

	menu = [1,2,3,4]
	
	try:
		opcion = int(input('Seleccione una opción: \n1) Sumar \n2) Restar \n3) Multiplicar\n4) Dividir \n5) Salir > '))

		if opcion == 5:
				print('\nSaliendo...')
				break

		if opcion in menu:
			
			n1= float(input('\nIngresa el primer numero: '))
			n2 = float(input('Ingresa el segundo numero: '))
		
			if opcion == 1:
				suma(n1,n2)
				
			elif opcion == 2:
				resta(n1,n2)
				
			elif opcion == 3:
				multiplicacion(n1,n2)
				
			else:
				division(n1,n2)

		else:
			print(f'\nOpcion invalida\n')

	except ValueError:
		print(f'\nOpcion invalida\n')