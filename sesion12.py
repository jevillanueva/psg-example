# print ("Inicio")
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 5
# print (numero % 2)
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# print ("Fin")

# print ("Inicio")
# condicion = True
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# else:
#     # Bloque de código
#     print ("No cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 4
# print (numero % 2)
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# else:
#     print ("El número es impar")
# print ("Fin")

# print ("Inicio Anidado")
# condicion_1 = False
# condicion_2 = True
# if condicion_1:
#     print ("Cumple condición 1")
#     if condicion_2:
#         print ("Cumple condición 2")
#     else:
#         print ("No cumple condición 2")
# else:
#     print ("No cumple condición 1")
# print ("Fin")

# print ("Inicio Par, Impar o Cero")
# numero = 0
# if numero != 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")

# print ("Inicio Positivo, Negativo o Cero")
# numero = 0
# if numero > 0:
#     print ("El número es positivo")
# elif numero < 0:
#     print ("El número es negativo")
# else:
#     print ("El número es cero")
# print ("FIN")

# ADRIANA MARIBEL QUISPE CARRILLO

# numero = 0

# if numero == 0:
#     print("es cero")
# elif numero % 2 == 0:
#     print("es par")
# else:
#     print("es impar")

# # Luciana Saavedra Ayarde

# numero = 1
# if numero == 0:
#     print ("El número es cero")
# elif numero % 2 == 0:
#     print ("El número es par")
# else:
#     print ("El número es impar")
# # Andrómeda Bolivia - Drakmer Rodriguez

# numero = 2
# if numero == 0:
#     print ("Es cero")
# elif numero % 2 == 0:
#     print ("Es par")
# else:
#     print ("Es impar")


#
# print ("Inicio Ternario Par, Impar")
# numero = 2
# opt_par = "El número es par"
# opt_impar = "El número es impar"
# resultado = opt_par if numero % 2 == 0 else opt_impar
# print (resultado)
# print ("Fin")

# # Andrómeda Bolivia - Drakmer Rodriguez

# print ("Inicio Ternario Par, Impar")
# num = 8
# res = "Es impar" if num % 2 != 0 else "Es par"
# print (res)
# print ("Fin")
# # Luciana Saavedra Ayarde

# print("Inicio Ternario Par, Impar")
# numero = 3
# resultado = (
#     "El número es par"
#     if numero % 2 == 0
#     else "El número es impar"
# )
# print(resultado)
# print("Fin")

# entero = 10000000
# print (bool(entero))

# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor:
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

# print ("Truthiness Flotantes")
# dividendo = float(input("Dividendo: "))
# divisor = float(input("Divisor: "))
# print (dividendo,divisor)
# if divisor != 0.0:
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

# print ("Truthiness Tuplas")
# tupla = tuple(input("Tupla: "))
# print (tupla)
# if tupla: # len(tupla) != 0 or tupla != ()
#     print ("La tupla no está vacía")
# else:
#     print ("La tupla está vacía")
# print ("Fin")

# print ("Truthiness Listas")
# lista = list(input("Lista: "))
# print (lista)
# if lista: # len(lista) != 0 or lista != []
#     print ("La lista no está vacía")
# else:
#     print ("La lista está vacía")
# print ("Fin")
# print ("Truthiness Diccionarios")


# diccionario = {}
# clave = input("Clave: ")
# valor = input("Valor: ")
# if clave:
#   diccionario = {clave:valor}
# print (diccionario)
# if diccionario:
#     print ("El diccionario no está vacío")
# else:
#     print ("El diccionario está vacío")
# print ("Fin")

# print ("Truthiness None")
# valor = None
# print (valor, type(valor))
# if valor: # valor != None
#     print ("El valor no es None")
# else:
#     print ("El valor es None")
# print ("Fin")

# entero = int(input("Entero: "))
# resultado = "Diferente de 0" if entero else "Igual a 0"
# print (resultado)

# cadena = input("Cadena: ")
# resultado = cadena if cadena else "valor por defecto"
# print (resultado)

# Luciana Saavedra Ayarde
# 4:53 PM
# disp_temperatura = 25
# if disp_temperatura > 30:
#     print ("Ventilador encendido")
# elif disp_temperatura < 20:
#     print ("Ventilador apagado")
# else: print ("La temperatura debe ser mayor a 30 o menor a 20 para encender o apagar el ventilador")
# # Andrómeda Bolivia - Drakmer Rodriguez
# # 4:54 PM
# t = int(input("Temperatura: "))
# if t > 30:
#     print ("ventilador encendido")
# elif t < 20:
#     print ("ventilador apagado")
# else:
#     print ("No hace nada el ventilador")

# temperatura=float(input("Ingrese temperatura en C: "))
# #---
# if temperatura>30:
#     ventilador="Encendido"
# elif temperatura<20:
#     ventilador="Apagado"
# else:
#     ventilador="Invalido"
# #---
# print(f"Ventilador: {ventilador}")

# cesta = ['🍑','🍓','🍉','🍎']
# print (cesta)
# resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
# print (resultado)
# print (cesta)

"""
Ejercicio por una carpeta de retos fuera de plazo:

Trabajas en un laboratorio de análisis de sangre. Tienes que determinar si un
paciente tiene anemia o no.

Para que un paciente tenga anemia, debe cumplir con las siguientes condiciones:
- Si el paciente es hombre, su nivel de hemoglobina debe ser menor a 13.5 g/dL.
- Si el paciente es mujer, su nivel de hemoglobina debe ser menor a 12 g/dL.
- Si el paciente es niñ@, su nivel de hemoglobina debe ser menor a 11 g/dL.
Para hacer tu trabajo mas fácil creaste un programa que recibe por teclado los
siguientes datos:
- Sexo del paciente (hombre, mujer).
- Edad del paciente (niño: 0-12 años, adulto: 13 años o más).
- Nivel de hemoglobina (en g/dL).
- El programa debe imprimir "Anemia" si el paciente tiene anemia,
    y "No Anemia" si no la tiene.

Restricciones:
- NO puedes utilizar sentencias de control (if, for, while).
- NO puedes utilizar funciones (def).

"""

sexo = input("Sexo: ").lower()
edad = int(input("Edad: "))
nivel = float(input("Nivel Hemoglobina g/dL: "))
umbral = (
    13.5 * (sexo == "hombre" and edad >= 13)
    + 12 * (sexo == "mujer" and edad >= 13)
    + 11 * (edad < 13)
)
anemia = nivel < umbral
estados = ["No", ""]
print(f"{estados[anemia]}Anemia")