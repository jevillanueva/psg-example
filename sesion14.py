def cuadrado(numero):
    """Retorna el cuadrado de un numero

    Args:
        numero (int): Numero a procesar
    """
    print(numero**2)




print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)