# print ("Inicio")
# for i in range(5): # rango (0,5,1)
#     print(i)
# print ("Fin")

# Ejemplo 1, sumar los números del 1 al 10 de 2 en 2
# print ("Ejemplo 1")
# suma = 0
# for i in range(1, 11, 2): # 1, 3, 5, 7, 9
#     #suma = suma + i #suma += i
#     suma += i
# print(suma)

# Ejemplo 2, crear un árbol de navidad de 6 niveles

# print ("Ejemplo 2")
# for i in range(0, 6):
#     print(" "*(5-i) + "*"*i*2+"*")

# print ("Ejemplo 3")
# for i in range(1, 11):
#     print(i**2, end=",")

# Ejemplo 4, crear una lista de números pares del 1 al 10 [1,2,3,...]

# print ("Ejemplo 4")
# pares = []
# for i in range(0, 1000, 2):
#     pares.append(i)
# print(pares)

# pares = list(range(0, 11, 2))
# print (pares)


# Valeria Fernandez
#3:43 PM
# for i in range(1,11):
#     print(i**3,end="," if i<10 else "")
# #Mauricio Ramirez Salamanca
# # 3:43 PM
# #imprime los 10 primeros números de la serie de números cúbicos
# print ("--")
# #números cúbicos
# cubico = []

# for i in range(10):
#     cubico.append((i+1)**3)
# print(cubico)

# print ("--")


# #Cammy Alexandra Santander Velarde
# #3:44 PM
# for i in range(1, 11):
#     print(i**3, end=" ")

# print ("--")
# # Drakmer Alain Rodriguez Chicchi
# # 3:44 PM

# for i in range(1, 11, 1):
#     print (i**3 , end=",")

# print ("--")

# for fruta in ['🍎','🍌','🍇','🍉']:
#     print(fruta)

#Ejemplo 5, imprimir los elementos de una lista fiestas

# Ejemplo 5, imprimir los elementos de una lista fiestas

# print ("Ejemplo 5")
# fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
# for objeto in fiesta:
#     print(objeto)

# print ("Ejemplo 6")
# frutas =  ('🍅','🍇','🍈','🍉','🍊')
# for fruta in frutas:
#     print(fruta, end=", ")

# print ("Ejemplo 7")
# frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
# #frutas = (('🍅','Tomate'),('🍇','Uva'))
# for clave in frutas:
#     valor = frutas[clave]
#     print(clave, valor)

# print ("Ejemplo 8")
# ciclo_vida = '🥚🐣🐥🐤🐔🍗'
# for etapa in ciclo_vida:
#     print(etapa, end="->")

#Ejemplo 9, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

# print ("Ejemplo 9")
# animales = ['🐶','🐱','🐰','🐭']
# for animal in animales:
#     print(animal)

#Ejemplo 10, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

# print ("Ejemplo 10")
# animales = ['🐶','🐱','🐰','🐭']
# for i in range(len(animales)):
#     print(animales[i])

# Ejemplo 11, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

# print ("Ejemplo 11")
# #animales = ['🐶','🐱','🐰','🐭']
# frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
# print (list(enumerate(frutas)))
# for i, fruta in enumerate(frutas):
#     print(i, fruta, frutas[fruta])

# Luciana Saavedra Ayarde
# 4:20 PM
# esferas = '⚽🏀🏐🎱'
# for i, elemento in enumerate(esferas):
#     print(elemento*(i+1))
# # Mauricio Ramirez Salamanca
# # 4:20 PM
# cadenas = '⚽🏀🏐🎱'
# for cadena in cadenas:
#     print(cadena*(cadenas.index(cadena)+1))
# # ADRIANA MARIBEL QUISPE CARRILLO
# # 4:20 PM
# pelotas = '⚽🏀🏐🎱'

# for i in range(len(pelotas)):
#     print(pelotas[i] * (i + 1))

# Ejemplo 12, imprimir los números mientras sean menores o igual a 5 empezando desde 0

# print ("Ejemplo 12")
# i = -10
# while i <= 5:
#     print(i)
#     i = i + 1
# print ("FIN")

# print ("Ejemplo 13")
# suma = 0
# numero = int(input("Ingrese un número: "))
# while numero != 0:
#     suma += numero
#     numero = int(input("Ingrese un número: "))
# print(suma)

# Richard Choquerive Ramos
# 4:44 PM
# numero = int(input("Ingrese un número: "))
# while numero >= 0:
#     print(numero)
#     numero -= 1
# print("Fin del contador")

# frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
# print ("Ejemplo 14")
# for fruta in frutas:
#     if fruta == '🐛':
#         break
#     print(fruta)
# print ("Ewww")

# frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
# print ("Ejemplo 14")
# i = ""
# while i != '🐛':
#     i = frutas.pop(0)
#     if i == '🐛':
#         break
#     print(i)
# print ("Eww")

# print ("Ejemplo 15")
# contador = 0
# while True:
#     print(contador)
#     contador += 1


# print ("Ejemplo 16")
# while True:
#     texto = input("Ingrese un texto: ")
#     if texto == 'salir':
#         break
#     print(texto.upper())
# print ("Fin")

#Ejemplo 17, Crear una lista de los números pares del 2 al 10

# print ("Ejemplo 17")
# pares = [i**2 for i in range(2, 11, 2)]
# print(pares)

#Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional

# # print ("Ejemplo 18")
# # pares = [i for i in range(2, 11) if i % 2 == 1]
# # print(pares)

# #$Ejemplo 19, Crear un diccionario números 2 al 10 donde si es par vale "Par" y si es impar valga "Impar"

# # print ("Ejemplo 19")
# # pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
# # print(pares)

# print ("Ejercicio 5")
# impares = tuple(i for i in range(1, 11) if i % 2 != 0)
# print(impares)

# print ("Ejemplo 21")
# while True:
#     numero = int(input("Ingrese un número: "))
#     if numero == 0:
#         break
#     print(f"Tabla del {numero}")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero*i}")
# print ("Fin")

print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)