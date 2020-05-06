""" Ejercicio 3

Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 
hasta ese número separados por comas. """

def numeros_impares(numero):

    for i in range(1,numero+1,2):
        print(i, end = ' ')


if __name__ == '__main__':
    numero = int(input('Ingrese un número entero positivo: '))
    numeros_impares(numero)